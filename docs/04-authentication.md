# 04. 認証と接続

GitHubとローカルPCを接続する方法は主に3つ。

## 接続方式の比較

| 方式 | セキュリティ | 手軽さ | 推奨度 |
|------|------------|--------|--------|
| **SSH鍵** | ◎ | 初回設定が必要 | ★★★ 推奨 |
| **HTTPS + PAT** | ○ | トークン管理が必要 | ★★☆ |
| **GitHub CLI (gh)** | ◎ | 最も簡単 | ★★★ 推奨 |

## 方法1: SSH鍵（推奨）

SSH鍵はペアで構成される：
- **秘密鍵** (`id_ed25519`): 自分のPCに保管。**絶対に他人に渡さない**
- **公開鍵** (`id_ed25519.pub`): GitHubに登録する

```
あなたのPC                          GitHub
┌────────────────┐                ┌────────────────┐
│ 秘密鍵 🔑      │ ←── 認証 ──→  │ 公開鍵 🔓      │
│ (~/.ssh/       │                │ (Settings →    │
│  id_ed25519)   │                │  SSH keys)     │
└────────────────┘                └────────────────┘
```

### SSH鍵の生成

```bash
# Ed25519鍵を生成（現在の推奨アルゴリズム）
ssh-keygen -t ed25519 -C "your-email@example.com"
```

質問が表示される：
```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/you/.ssh/id_ed25519):  ← Enterでデフォルト
Enter passphrase (empty for no passphrase):  ← パスフレーズを入力（推奨）
Enter same passphrase again:  ← もう一度入力
```

> **パスフレーズ**: SSH鍵を使うときに必要なパスワード。設定しておくと鍵が漏洩しても安全。

### SSHエージェントに鍵を登録

```bash
# SSHエージェントを起動
eval "$(ssh-agent -s)"

# macOSの場合: SSHの設定ファイルを作成/編集
cat >> ~/.ssh/config << 'EOF'
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
EOF

# 鍵をエージェントに追加
ssh-add ~/.ssh/id_ed25519        # Linux
ssh-add --apple-use-keychain ~/.ssh/id_ed25519  # macOS
```

### 公開鍵をGitHubに登録

```bash
# 公開鍵をクリップボードにコピー
pbcopy < ~/.ssh/id_ed25519.pub    # macOS
cat ~/.ssh/id_ed25519.pub         # Linux（表示してコピー）
```

1. GitHub → Settings → **SSH and GPG keys**
2. 「**New SSH key**」をクリック
3. Title: わかりやすい名前（例: `MacBook Pro 2024`）
4. Key type: Authentication Key
5. Key: コピーした公開鍵を貼り付け
6. 「**Add SSH key**」をクリック

<!-- screenshot: SSH鍵の追加画面 -->

### 接続テスト

```bash
ssh -T git@github.com
```

成功すると：
```
Hi username! You've been successfully authenticated, but GitHub does not provide shell access.
```

### SSH接続でのリポジトリ操作

```bash
# SSH URLでクローン
git clone git@github.com:username/repo.git

# 既存リポジトリのURLをSSHに変更
git remote set-url origin git@github.com:username/repo.git
```

## 方法2: HTTPS + Personal Access Token (PAT)

### PATの作成

1. GitHub → Settings → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. 「**Generate new token (classic)**」をクリック
3. 設定：
   - **Note**: トークンの用途（例: `MacBook dev`）
   - **Expiration**: 有効期限（90日推奨）
   - **Scopes**: 権限を選択

<!-- screenshot: PAT作成画面 -->

### スコープ（権限）の選び方

| スコープ | 用途 |
|---------|------|
| `repo` | プライベートリポジトリへのアクセス（基本的にこれは必須） |
| `workflow` | GitHub Actionsの管理 |
| `admin:org` | Organization管理 |
| `gist` | Gist作成 |
| `delete_repo` | リポジトリ削除 |

**最小限の推奨**: `repo` と `workflow`

### PATの使い方

```bash
# HTTPS URLでクローン
git clone https://github.com/username/repo.git
# パスワードを聞かれたらPATを入力
```

### 認証情報の保存（毎回入力しなくて済むように）

```bash
# macOS: Keychainに保存
git config --global credential.helper osxkeychain

# Windows: Windows Credential Managerに保存
git config --global credential.helper wincred

# Linux: 一定時間メモリに保存（秒数指定）
git config --global credential.helper 'cache --timeout=3600'
```

### Fine-grained PAT（新方式）

より細かく権限を制御できる新しいタイプのトークン。

1. **Developer settings → Personal access tokens → Fine-grained tokens**
2. リポジトリ単位で権限を設定可能
3. 組織のポリシーに準拠

## 方法3: GitHub CLI（最も簡単）

### インストール

```bash
# macOS
brew install gh

# Windows
winget install --id GitHub.cli

# Linux (Debian/Ubuntu)
sudo apt install gh
```

### 認証

```bash
gh auth login
```

対話形式で設定：
```
? What account do you want to log into?  GitHub.com
? What is your preferred protocol for Git operations?  SSH（推奨）
? Generate a new SSH key to add to your GitHub account?  Yes
? Title for your SSH key:  MacBook Pro
? How would you like to authenticate GitHub CLI?  Login with a web browser
```

ブラウザが開いて認証完了。

<!-- screenshot: gh auth login の画面 -->

### 認証状態の確認

```bash
gh auth status
```

```
github.com
  ✓ Logged in to github.com account username (keyring)
  - Active account: true
  - Git operations protocol: ssh
  - Token: gho_****
  - Token scopes: 'admin:org', 'gist', 'repo', 'workflow'
```

## GPG署名（コミットの本人証明）

コミットが本当に自分のものであることを暗号的に証明する機能。

### GPG鍵の生成

```bash
# GPGのインストール（macOS）
brew install gnupg

# 鍵の生成
gpg --full-generate-key
# RSA、4096ビット、有効期限なし、名前とメールを入力
```

### GitHubにGPG鍵を登録

```bash
# 鍵IDの確認
gpg --list-secret-keys --keyid-format=long

# 出力例:
# sec   rsa4096/3AA5C34371567BD2 2024-01-01
#                ^^^^^^^^^^^^^^^^ これが鍵ID

# 公開鍵をエクスポート
gpg --armor --export 3AA5C34371567BD2
```

出力された `-----BEGIN PGP PUBLIC KEY BLOCK-----` から `-----END PGP PUBLIC KEY BLOCK-----` までをGitHubに登録：

GitHub → Settings → **SSH and GPG keys** → **New GPG key**

### Gitで署名を有効化

```bash
git config --global user.signingkey 3AA5C34371567BD2
git config --global commit.gpgsign true   # 全コミットを自動署名
git config --global gpg.program gpg       # GPGプログラムのパス
```

署名されたコミットはGitHub上で「**Verified**」バッジが表示される。

<!-- screenshot: Verifiedバッジ付きコミット -->

## 複数アカウントの管理

仕事用と個人用など、複数のGitHubアカウントを使い分ける場合：

### SSH設定で分ける

`~/.ssh/config`:
```
# 個人アカウント
Host github.com-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_personal

# 仕事アカウント
Host github.com-work
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_work
```

使い分け：
```bash
# 個人
git clone git@github.com-personal:personal-user/repo.git

# 仕事
git clone git@github.com-work:work-user/repo.git
```

### リポジトリごとにユーザーを切り替え

```bash
cd /path/to/work/repo
git config user.name "Work Name"
git config user.email "work@company.com"
```

## 次のステップ

→ [05. リポジトリの作成と管理](05-repository.md) で最初のリポジトリを作ろう
