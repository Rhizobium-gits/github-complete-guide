# 02. 環境構築

## Gitのインストール

### macOS

**方法1: Xcode Command Line Tools（推奨）**
```bash
xcode-select --install
```
ダイアログが表示されたら「インストール」をクリック。

<!-- screenshot: xcode-select インストールダイアログ -->

**方法2: Homebrew経由**
```bash
brew install git
```

**方法3: 公式サイトからダウンロード**
- https://git-scm.com/download/mac

### Windows

**方法1: Git for Windows（推奨）**
1. https://gitforwindows.org/ にアクセス
2. 「Download」をクリック
3. インストーラーを実行

<!-- screenshot: Git for Windows インストーラー -->

インストール時の設定（迷ったらデフォルトでOK）：
- **エディタ**: Visual Studio Code を選択推奨
- **PATH環境変数**: 「Git from the command line and also from 3rd-party software」を選択
- **改行コード**: 「Checkout Windows-style, commit Unix-style line endings」を選択

**方法2: winget（Windows 10/11）**
```powershell
winget install --id Git.Git -e --source winget
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install git
```

### Linux (Fedora/RHEL)
```bash
sudo dnf install git
```

## インストール確認

```bash
git --version
# 出力例: git version 2.44.0
```

## 初期設定（必須）

Gitを使う前に、**名前**と**メールアドレス**を設定する必要がある。これはコミットに記録される情報。

```bash
# ユーザー名を設定（GitHubのユーザー名と合わせるのが一般的）
git config --global user.name "あなたの名前"

# メールアドレスを設定（GitHubに登録したメールアドレス）
git config --global user.email "your-email@example.com"
```

> **重要**: `--global` は全てのリポジトリに適用される設定。特定のリポジトリだけ別の設定にしたい場合は `--global` を外す。

### プライバシー保護: noreplyメールの使用

GitHubは公開リポジトリのコミットからメールアドレスが見えてしまう。これを防ぐには：

1. GitHub → Settings → Emails
2. 「Keep my email addresses private」にチェック
3. 表示される `xxxxxxx+username@users.noreply.github.com` をGitの設定に使う

```bash
git config --global user.email "xxxxxxx+username@users.noreply.github.com"
```

<!-- screenshot: GitHub Email設定画面 -->

## 追加の初期設定（推奨）

```bash
# デフォルトブランチ名を main に設定（現在の標準）
git config --global init.defaultBranch main

# エディタをVS Codeに設定（コミットメッセージ編集時に使われる）
git config --global core.editor "code --wait"

# macOSの場合: .DS_Store を全リポジトリで無視
echo ".DS_Store" >> ~/.gitignore_global
git config --global core.excludesfile ~/.gitignore_global

# カラー表示を有効化
git config --global color.ui auto

# pushのデフォルト動作を設定
git config --global push.default current

# pull時にrebaseを使う（好みに応じて）
git config --global pull.rebase true
```

## 設定の確認

```bash
# 全設定を表示
git config --list

# 特定の設定を確認
git config user.name
git config user.email
```

## 設定ファイルの場所

Gitの設定は3つのレベルがある：

| レベル | フラグ | ファイルの場所 | 適用範囲 |
|--------|--------|---------------|---------|
| System | `--system` | `/etc/gitconfig` | PC全体 |
| Global | `--global` | `~/.gitconfig` | 現在のユーザー |
| Local | `--local` | `.git/config`（リポジトリ内） | そのリポジトリのみ |

優先順位: Local > Global > System

```bash
# 設定ファイルを直接編集
git config --global --edit
```

## エディタ・ターミナルの準備

### VS Code（推奨エディタ）

1. https://code.visualstudio.com/ からダウンロード・インストール
2. VS Codeを開く → `Cmd+Shift+P`（Mac）/ `Ctrl+Shift+P`（Windows）
3. 「Shell Command: Install 'code' command in PATH」を実行

**おすすめ拡張機能：**
- **GitLens** — Git履歴の可視化
- **GitHub Pull Requests** — VS Code内でPR操作
- **GitHub Copilot** — AIコーディング支援

### ターミナル

| OS | 推奨ターミナル |
|----|-------------|
| macOS | Terminal.app または iTerm2 |
| Windows | Windows Terminal + Git Bash |
| Linux | 標準ターミナル |

## 次のステップ

→ [03. GitHubアカウント作成](03-account.md) でGitHubに登録しよう
