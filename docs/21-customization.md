# 21. GitHubのカスタマイズ

## テーマ設定

### GitHub のダークモード/ライトモード

1. 右上のアイコン → **Settings**
2. 左メニュー → **Appearance**
3. テーマを選択：
   - Light default / Light high contrast
   - Dark default / Dark high contrast / Dark dimmed
   - System に同期

<!-- screenshot: テーマ設定画面 -->

## キーボードショートカット

GitHub上で `?` を押すとショートカット一覧が表示される。

### グローバル

| ショートカット | 機能 |
|-------------|------|
| `s` または `/` | 検索バーにフォーカス |
| `g` `n` | 通知ページ |
| `g` `d` | ダッシュボード |
| `?` | ショートカット一覧 |

### リポジトリ内

| ショートカット | 機能 |
|-------------|------|
| `t` | ファイルファインダー |
| `w` | ブランチ切り替え |
| `g` `c` | Codeタブ |
| `g` `i` | Issuesタブ |
| `g` `p` | Pull requestsタブ |
| `g` `a` | Actionsタブ |
| `g` `b` | Projectsタブ |
| `g` `w` | Wikiタブ |

### ファイル表示

| ショートカット | 機能 |
|-------------|------|
| `y` | パーマリンクに変換 |
| `l` | 行番号にジャンプ |
| `b` | blameビュー |
| `e` | ファイル編集 |

### PR/Issue

| ショートカット | 機能 |
|-------------|------|
| `r` | 返信（引用付き） |
| `Cmd/Ctrl + Enter` | コメント送信 |
| `Cmd/Ctrl + Shift + p` | プレビュー切り替え |

## GitHub CLI (gh) のカスタマイズ

### エイリアス

よく使うコマンドにエイリアスを設定：

```bash
# エイリアスの設定
gh alias set prc 'pr create'
gh alias set prv 'pr view --web'
gh alias set prl 'pr list'
gh alias set il 'issue list'
gh alias set ic 'issue create'

# 複雑なコマンドのエイリアス
gh alias set my-prs 'pr list --author @me'
gh alias set my-issues 'issue list --assignee @me'

# エイリアス一覧
gh alias list

# 使用例
gh prc --title "New feature"
gh my-prs
```

### 設定

```bash
# デフォルトエディタ
gh config set editor "code --wait"

# デフォルトブラウザ
gh config set browser "firefox"

# プロンプトを有効化
gh config set prompt enabled

# 設定一覧
gh config list
```

## Gitのカスタマイズ

### エイリアス（Gitコマンド）

```bash
# 基本エイリアス
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.sw switch

# ログ表示
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.ll "log --oneline -20"

# 差分
git config --global alias.df diff
git config --global alias.ds "diff --staged"

# 最後のコミットを修正
git config --global alias.amend "commit --amend --no-edit"

# ブランチクリーンアップ
git config --global alias.cleanup "!git branch --merged main | grep -v main | xargs -n 1 git branch -d"
```

使用例：
```bash
git st          # = git status
git co main     # = git checkout main
git lg          # = きれいなログ表示
git amend       # = 直前のコミットを修正
```

### .gitconfig の直接編集

`~/.gitconfig`:
```ini
[user]
    name = Your Name
    email = your@email.com

[core]
    editor = code --wait
    autocrlf = input

[init]
    defaultBranch = main

[push]
    default = current

[pull]
    rebase = true

[alias]
    st = status
    co = checkout
    br = branch
    ci = commit
    lg = log --oneline --graph --decorate --all

[color]
    ui = auto

[diff]
    tool = vscode

[difftool "vscode"]
    cmd = code --wait --diff $LOCAL $REMOTE

[merge]
    tool = vscode

[mergetool "vscode"]
    cmd = code --wait $MERGED
```

## 通知のカスタマイズ

### GitHub上の通知設定

Settings → **Notifications**:

```
Participating:        自分が関わるIssue/PRの通知
  ✅ Web + ✅ Email

Watching:             Watch中のリポジトリの通知
  ✅ Web + ❌ Email（ノイズになるのでWebのみ推奨）

GitHub Actions:       CI/CDの通知
  ✅ Failed workflows only（失敗時のみ）
```

### リポジトリごとの通知

リポジトリページの「**Watch**」ボタン：

| 設定 | 通知対象 |
|------|---------|
| **Participating and @mentions** | 自分への言及・参加中のみ |
| **All Activity** | 全ての活動 |
| **Ignore** | 完全に無視 |
| **Custom** | カスタム選択 |

## GitHub Mobile

iOS/Android アプリで外出先からも操作可能。

- Issue/PRの確認・コメント
- コードの閲覧
- 通知の管理
- マージの承認

## Saved Replies（保存済みの返信）

よく使うコメントをテンプレートとして保存。

Settings → **Saved replies**:

```
タイトル: LGTM
本文: Looks good to me! 👍 Thank you for the contribution.

タイトル: Needs tests
本文: Could you add tests for the new functionality? We want to make sure this doesn't regress.
```

## 次のステップ

→ [22. セキュリティ](22-security.md) でリポジトリのセキュリティを強化しよう
