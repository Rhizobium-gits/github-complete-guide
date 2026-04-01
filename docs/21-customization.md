# 第21章　カスタマイズ --- GitHubを自分好みに整える

## 21.1 この章で学ぶこと

道具は使いやすいように調整してこそ、その真価を発揮します。大工が鉋（かんな）の刃を研ぎ、料理人が包丁の柄を自分の手に馴染ませるように、開発者もGitやGitHubを自分の作業スタイルに合わせてカスタマイズすべきです。

この章では、GitHubとGitをより快適に使うためのカスタマイズ方法を学びます。

- GitHubのテーマ設定（ダークモード/ライトモード）
- キーボードショートカットの活用
- GitHub CLI（gh）のエイリアス設定
- Gitコマンドのエイリアスと `.gitconfig` の書き方
- 通知の最適化 --- 情報の洪水に飲まれないために
- GitHub Mobileアプリの活用
- Saved Replies（保存済みの返信）による効率化

---

## 21.2 テーマ設定 --- ダークモード/ライトモード

長時間コードを読む開発者にとって、画面の明るさは目の疲れに直結します。GitHubでは複数のテーマが用意されており、好みや環境に合わせて選択できます。

設定方法は以下の通りです。

1. 右上のプロフィールアイコンをクリック
2. **Settings** を選択
3. 左メニューの **Appearance** をクリック
4. 好みのテーマを選択

<!-- screenshot: テーマ設定画面（Appearance） -->

選択できるテーマは以下の通りです。

| テーマ | 特徴 |
|--------|------|
| Light default | 標準的な白背景。明るい環境での作業に適している |
| Light high contrast | 白背景だがコントラストが高い。視認性を重視 |
| Dark default | 暗い背景。夜間の作業や暗い部屋での使用に適している |
| Dark high contrast | 暗い背景でコントラストが高い |
| Dark dimmed | やや明るめのダークテーマ。目に優しい |
| System に同期 | OSのダークモード設定に自動追従 |

「System に同期」を選ぶと、macOSやWindowsのシステム設定でダークモード/ライトモードを切り替えたとき、GitHubのテーマも自動的に切り替わります。日中はライトモード、夜間はダークモードを使い分けたい場合に便利です。

---

## 21.3 キーボードショートカット

GitHubのWeb画面には多数のキーボードショートカットが用意されています。マウス操作を減らすことで、ページ間の移動やファイルの検索が格段に速くなります。まず覚えるべきは **`?` キー** です。どのページにいても `?` を押すと、そのページで使えるショートカットの一覧が表示されます。

<!-- screenshot: ?キーで表示されるショートカット一覧 -->

### グローバルショートカット（どのページでも使える）

| ショートカット | 機能 |
|-------------|------|
| `?` | ショートカット一覧を表示 |
| `s` または `/` | 検索バーにフォーカスを移動 |
| `g` → `n` | 通知ページに移動 |
| `g` → `d` | ダッシュボード（ホーム画面）に移動 |

`g` → `n` のように2つのキーを続けて押す操作は「コードシーケンス」と呼ばれます。最初の `g` を押した後、一定時間内に2つ目のキーを押す必要があります。`g` は "go to"（移動する）の略と考えると覚えやすいでしょう。

### リポジトリ内ショートカット

リポジトリのページでは、各タブへの素早い移動が可能です。

| ショートカット | 機能 |
|-------------|------|
| `t` | ファイルファインダー（ファジー検索）を開く |
| `w` | ブランチ切り替えメニューを開く |
| `g` → `c` | Codeタブに移動 |
| `g` → `i` | Issuesタブに移動 |
| `g` → `p` | Pull requestsタブに移動 |
| `g` → `a` | Actionsタブに移動 |
| `g` → `b` | Projectsタブに移動 |
| `g` → `w` | Wikiタブに移動 |

### ファイル表示時のショートカット

| ショートカット | 機能 |
|-------------|------|
| `y` | パーマリンク（コミットハッシュ指定URL）に変換 |
| `l` | 行番号を入力してジャンプ |
| `b` | blameビュー（各行の変更者表示）に切り替え |
| `e` | ファイルを編集モードで開く |

### Pull RequestとIssueのショートカット

| ショートカット | 機能 |
|-------------|------|
| `r` | 選択テキストを引用して返信 |
| `Cmd/Ctrl + Enter` | コメントを送信 |
| `Cmd/Ctrl + Shift + p` | Markdownプレビューの切り替え |

特に `Cmd/Ctrl + Shift + p` は、コメントを書いている途中でMarkdownがどのように表示されるかを確認するのに便利です。

---

## 21.4 GitHub CLI (gh) のカスタマイズ --- エイリアスの設定と活用例

GitHub CLI（`gh`）は第4章で紹介した通り、ターミナルからGitHubの操作ができるツールです。よく使うコマンドにはエイリアス（短縮名）を設定しておくと、タイプ量が減って作業が効率化されます。

### エイリアスの設定

```bash
# 基本的なエイリアス
gh alias set prc 'pr create'           # PR作成
gh alias set prv 'pr view --web'       # PRをブラウザで開く
gh alias set prl 'pr list'             # PR一覧
gh alias set il 'issue list'            # Issue一覧
gh alias set ic 'issue create'          # Issue作成

# 自分に関連するものだけ表示するエイリアス
gh alias set my-prs 'pr list --author @me'
gh alias set my-issues 'issue list --assignee @me'

# 現在のブランチのPRをチェックアウト
gh alias set prco 'pr checkout'

# 設定済みのエイリアス一覧を確認
gh alias list
```

設定したエイリアスは以下のように使います。

```bash
# gh pr create の代わりに
gh prc --title "Add login feature"

# 自分が出したPRの一覧
gh my-prs

# 自分にアサインされたIssue一覧
gh my-issues
```

### ghの設定

エイリアス以外にも、`gh config` コマンドでデフォルトの挙動をカスタマイズできます。

```bash
# デフォルトエディタをVS Codeに設定
gh config set editor "code --wait"

# デフォルトブラウザを指定
gh config set browser "firefox"

# 対話的プロンプトを有効化（確認ダイアログを表示する）
gh config set prompt enabled

# 現在の設定を一覧表示
gh config list
```

---

## 21.5 Gitのカスタマイズ --- エイリアスと.gitconfig

Git自体にもエイリアス機能があります。`git status` を毎日何十回も打つ開発者にとって、`git st` と短縮できるだけでも積み重なると大きな時間の節約になります。

### エイリアスの設定

```bash
# 基本コマンドの短縮
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.sw switch

# ログ表示（見やすいフォーマット）
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.ll "log --oneline -20"

# 差分の確認
git config --global alias.df diff
git config --global alias.ds "diff --staged"

# 直前のコミットにファイルを追加（メッセージは変えない）
git config --global alias.amend "commit --amend --no-edit"

# マージ済みブランチの一括削除
git config --global alias.cleanup "!git branch --merged main | grep -v main | xargs -n 1 git branch -d"
```

設定したエイリアスは即座に使えます。

```bash
git st          # git status と同じ
git co main     # git checkout main と同じ
git lg          # きれいなグラフ付きログ
git ds          # ステージ済みの差分を確認
git amend       # 直前のコミットを修正
```

`git lg` は特におすすめのエイリアスです。ブランチの分岐と合流がグラフで視覚的に表示されるため、リポジトリの状態を直感的に把握できます。

### .gitconfig の直接編集

エイリアスを一つずつ `git config` コマンドで設定するのが面倒な場合は、設定ファイルを直接編集することもできます。Gitのグローバル設定は `~/.gitconfig`（ホームディレクトリ直下の `.gitconfig`）に保存されています。

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
    sw = switch
    lg = log --oneline --graph --decorate --all
    ll = log --oneline -20
    df = diff
    ds = diff --staged
    amend = commit --amend --no-edit

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

いくつかの設定項目を補足します。

- **`push.default = current`**: `git push` の際にブランチ名を省略すると、現在のブランチと同名のリモートブランチにプッシュする設定です。ブランチ名を毎回指定する手間が省けます。
- **`pull.rebase = true`**: `git pull` の際にマージコミットを作らず、リベースで履歴を直線的に保つ設定です。履歴をきれいに保ちたい場合に便利です。
- **`init.defaultBranch = main`**: `git init` で新しいリポジトリを作るときのデフォルトブランチ名を `main` にする設定です。
- **`color.ui = auto`**: ターミナルが対応していれば、diffやstatusの出力に色を付ける設定です。

---

## 21.6 通知のカスタマイズ

GitHubの通知は、設定を適切に行わないと大量のメールやアラートに埋もれてしまいます。「本当に重要な通知だけ受け取る」ように最適化しましょう。

### 通知設定の場所

Settings → **Notifications** で、通知の受け取り方を細かく設定できます。

```
Participating（参加中の会話）:
  Web通知:  有効にする
  メール:   有効にする
  → 自分が関わるIssue/PRの更新は確実に受け取りたい

Watching（ウォッチ中のリポジトリ）:
  Web通知:  有効にする
  メール:   無効にする（ノイズが多くなるため）
  → WebのNotificationsページで確認すれば十分

GitHub Actions:
  失敗時のみ通知にする
  → 成功したワークフローの通知は不要
```

<!-- screenshot: 通知設定画面 -->

### リポジトリごとの通知設定

リポジトリのページ上部にある「**Watch**」ボタンで、リポジトリ単位の通知レベルを設定できます。

| 設定 | 通知対象 |
|------|---------|
| **Participating and @mentions** | 自分が参加中の会話と、@メンションされた場合のみ |
| **All Activity** | リポジトリ内のすべての活動（Issue作成、PR作成、コメントなど） |
| **Ignore** | このリポジトリからの通知を完全に無視 |
| **Custom** | Issue、PR、Release、Discussion などから受け取りたいものを選択 |

おすすめの設定方針は以下の通りです。

- **自分のリポジトリ**: All Activity（すべてを把握したい）
- **チームのリポジトリ**: Participating and @mentions（関係するものだけ）
- **参考にしているOSSリポジトリ**: Custom → Releases only（新バージョンだけ知りたい）
- **もう関わらないリポジトリ**: Ignore

通知が溜まりすぎたときは、GitHubの通知ページ（https://github.com/notifications）で「Mark all as read」を使って一括既読にできます。未読の通知を溜め込んでも何も良いことはありません。定期的にトリアージ（仕分け）する習慣をつけましょう。

---

## 21.7 GitHub Mobile

GitHub Mobileは、iOS/Androidに対応した公式アプリです。外出先でもスマートフォンからGitHubの主要な操作を行えます。

GitHub Mobileでできる主な操作は以下の通りです。

- **Issue / PRの確認とコメント**: 通勤中や移動中にIssueの内容を確認し、コメントを返すことができます
- **コードの閲覧**: ファイルの中身を読むことができます（ただし編集はWeb版の方が快適です）
- **通知の管理**: プッシュ通知でリアルタイムに更新を受け取り、既読/未読の管理ができます
- **マージの承認**: Pull Requestのレビューを行い、Approveやマージができます
- **Discussionsへの参加**: ディスカッションの閲覧と投稿

特に便利なのは通知機能です。重要なPull Requestへのコメントや、CIの失敗通知をリアルタイムで受け取れるため、すぐに対応が必要な問題を見逃しにくくなります。

アプリのインストールは、App Store（iOS）またはGoogle Play Store（Android）から「GitHub」を検索してください。ログインにはWebブラウザ経由の認証が使われ、2FAにも対応しています。

---

## 21.8 Saved Replies

IssueやPull Requestのレビューでは、同じような内容のコメントを繰り返し書くことがあります。例えば、「LGTM（Looks Good To Me）」や「テストを追加してください」といったメッセージです。こうした定型文を毎回手入力するのは非効率です。

**Saved Replies（保存済みの返信）** は、よく使うコメントをテンプレートとして保存しておき、ワンクリックで挿入できる機能です。

### 設定方法

1. **Settings** → **Saved replies** を開く
2. テンプレートのタイトルと本文を入力して保存

### 便利なテンプレート例

```
タイトル: LGTM
本文:
LGTM! Thank you for the contribution.

タイトル: Needs tests
本文:
Could you add tests for the new functionality?
We want to make sure this doesn't regress in the future.

タイトル: Duplicate
本文:
This appears to be a duplicate of #___. Closing in favor of the original issue.
Please add any additional context to the original issue.

タイトル: Stale
本文:
This issue has been inactive for a while. If the problem still exists,
please provide updated information. Otherwise, this will be closed.
```

Saved Repliesを使うには、IssueやPRのコメント欄の右上にあるメニューアイコンから選択するか、`Ctrl + .`（macOSでは `Cmd + .`）のショートカットで挿入できます。

チーム全体で同じSaved Repliesを使うことはできません（ユーザーごとの設定です）が、チーム内で「こういうテンプレートを使おう」というガイドラインを共有しておくと、コミュニケーションの一貫性が保たれます。

---

## 21.9 まとめ

この章では、GitHubとGitを自分好みにカスタマイズする方法を学びました。

- **テーマ設定**: ダークモード、ライトモード、システム同期などから選べる。Appearance設定で変更
- **キーボードショートカット**: `?` キーで一覧表示。`t`（ファイル検索）、`g` → `i`（Issues移動）、`y`（パーマリンク変換）などが特に便利
- **GitHub CLI エイリアス**: `gh alias set` で頻用コマンドを短縮。`gh prc` で PR作成、`gh my-prs` で自分のPR一覧など
- **Git エイリアス**: `git config --global alias.st status` のように設定。`~/.gitconfig` を直接編集すると一括設定が楽
- **通知のカスタマイズ**: Participating はWeb+メール、Watching はWebのみ、Actions は失敗時のみが推奨設定。リポジトリごとのWatch設定で粒度を調整
- **GitHub Mobile**: iOS/Android対応。通知のリアルタイム受信とIssue/PRへのコメントが外出先でも可能
- **Saved Replies**: 定型コメントをテンプレート化。レビューの効率とコミュニケーションの一貫性が向上

カスタマイズに「正解」はありません。自分の作業スタイルに合わせて少しずつ調整し、快適な開発環境を作り上げていきましょう。

---

次の章 → [第22章　セキュリティ --- リポジトリを安全に保つ](22-security.md)
