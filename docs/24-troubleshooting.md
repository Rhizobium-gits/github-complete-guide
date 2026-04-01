# 24. トラブルシューティング — よくあるエラーと解決法

## 認証エラー

### `Permission denied (publickey)`

```
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.
```

**原因**: SSH鍵が設定されていない、または正しく登録されていない

**解決法**:
```bash
# SSH鍵の確認
ls -la ~/.ssh/

# SSH接続テスト
ssh -T git@github.com

# 鍵がない場合は作成
ssh-keygen -t ed25519 -C "your-email@example.com"

# エージェントに追加
ssh-add ~/.ssh/id_ed25519

# 公開鍵をGitHubに登録
cat ~/.ssh/id_ed25519.pub
# → GitHub Settings → SSH keys に貼り付け
```

### `remote: Invalid username or password`

```
remote: Invalid username or password.
fatal: Authentication failed
```

**原因**: パスワード認証は廃止された。PATまたはSSHが必要。

**解決法**:
```bash
# GitHub CLIで認証し直す
gh auth login

# または PAT を使う
# GitHub → Settings → Developer settings → Personal access tokens
```

### `403 Forbidden`

**原因**: トークンの権限不足

**解決法**: PATのスコープに `repo` が含まれているか確認。

## push/pullエラー

### `rejected – non-fast-forward`

```
! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs
```

**原因**: リモートに自分が持っていないコミットがある

**解決法**:
```bash
# まずpullしてからpush
git pull --rebase
git push

# または（確認してから）
git fetch origin
git log HEAD..origin/main  # リモートの変更を確認
git rebase origin/main
git push
```

### `fatal: refusing to merge unrelated histories`

**原因**: 共通の祖先がない2つのリポジトリをマージしようとしている

**解決法**:
```bash
git pull origin main --allow-unrelated-histories
```

### `Your branch is behind 'origin/main'`

```bash
# リモートの変更を取り込む
git pull

# リベースで取り込む（推奨）
git pull --rebase
```

## ブランチ関連

### `error: Your local changes would be overwritten`

```
error: Your local changes to the following files would be overwritten by checkout
```

**原因**: 未コミットの変更がある状態でブランチを切り替えようとした

**解決法**:
```bash
# 方法1: 変更を退避
git stash
git switch other-branch
# 戻ったら復元
git switch original-branch
git stash pop

# 方法2: 変更をコミット
git add .
git commit -m "WIP: save progress"
git switch other-branch
```

### `error: branch 'x' not found`

```bash
# リモートブランチを取得
git fetch origin

# リモートブランチ一覧を確認
git branch -r

# リモートブランチを元にローカルブランチを作成
git switch -c branch-name origin/branch-name
```

## コミット関連

### 間違ったブランチにコミットした

```bash
# 1. コミットを取り消し（変更は残る）
git reset --soft HEAD~1

# 2. 正しいブランチに切り替え
git stash
git switch correct-branch
git stash pop

# 3. 正しいブランチでコミット
git add .
git commit -m "正しいメッセージ"
```

### コミットメッセージを間違えた

```bash
# 直前のコミットメッセージを修正（まだpushしていない場合）
git commit --amend -m "正しいメッセージ"
```

### 大きなファイルをコミットしてしまった

```bash
# 直前のコミットの場合
git reset --soft HEAD~1
echo "large-file.zip" >> .gitignore
git add .gitignore
git commit -m "Add .gitignore"

# 過去のコミットの場合
# BFG Repo-Cleanerを使う
brew install bfg
bfg --strip-blobs-bigger-than 100M
git reflog expire --expire=now --all
git gc --prune=now --aggressive
```

## .gitignore 関連

### `.gitignore` が効かない

**原因**: 既に追跡されているファイルは `.gitignore` に追加しても無視されない

**解決法**:
```bash
# 追跡を解除
git rm --cached ファイル名

# フォルダの場合
git rm -r --cached フォルダ名

# コミット
git add .gitignore
git commit -m "Remove tracked files that should be ignored"
```

## ネットワーク関連

### `Connection timed out`

```bash
# SSHの設定でポート443を使う
cat >> ~/.ssh/config << 'EOF'
Host github.com
  Hostname ssh.github.com
  Port 443
  User git
EOF

# テスト
ssh -T git@github.com
```

### クローンが遅い

```bash
# 浅いクローン（最新のみ）
git clone --depth 1 git@github.com:owner/repo.git

# 特定ブランチだけ
git clone --single-branch -b main git@github.com:owner/repo.git
```

## その他

### `detached HEAD`

```
You are in 'detached HEAD' state.
```

**原因**: ブランチではなくコミットを直接チェックアウトした

**解決法**:
```bash
# ブランチに戻る
git switch main

# 現在の状態を新しいブランチとして保存したい場合
git switch -c new-branch-name
```

### LF/CRLF 改行コードの問題

```bash
# macOS/Linux
git config --global core.autocrlf input

# Windows
git config --global core.autocrlf true
```

### `fatal: not a git repository`

```bash
# 現在のディレクトリがGitリポジトリか確認
git status

# リポジトリでない場合は初期化
git init

# または正しいディレクトリに移動
cd /path/to/your/repo
```

## 困ったときのコマンド

```bash
# 現在の状態を把握
git status
git log --oneline -10
git remote -v
git branch -a

# 最後の手段: 全てを元に戻す（未コミットの変更が消える）
git checkout .           # ファイルの変更を元に戻す
git clean -fd            # 未追跡ファイルを削除

# 核オプション: リモートの状態に完全に戻す
git fetch origin
git reset --hard origin/main
```

> ⚠️ `reset --hard` と `clean -fd` は変更が完全に失われる。使う前にバックアップを。

## 付録へ

→ [付録A: Gitコマンド早見表](appendix-a-cheatsheet.md)
→ [付録B: 用語集](appendix-b-glossary.md)
