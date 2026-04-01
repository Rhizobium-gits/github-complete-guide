# 26. GitHubアプリの比較 — Web・Desktop・CLI・Mobile・IDE

## GitHubを操作する方法は5つある

```
┌─────────────────────────────────────────────────────────────┐
│                       GitHub (サーバー)                       │
└──────┬──────────┬──────────┬──────────┬──────────┬──────────┘
       ↕          ↕          ↕          ↕          ↕
   ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐  ┌──────┐
   │ Web  │  │Desktop│  │ CLI  │  │Mobile│  │ IDE  │
   │ UI   │  │ App  │  │ (gh) │  │ App  │  │拡張機能│
   └──────┘  └──────┘  └──────┘  └──────┘  └──────┘
   ブラウザ   専用アプリ  ターミナル  スマホ     VS Code等
```

## 比較表

| 機能 | Web UI | Desktop | CLI (gh) | Mobile | IDE拡張 |
|------|--------|---------|----------|--------|---------|
| **コード閲覧** | ◎ | ○ | △ | ○ | ◎ |
| **コード編集** | ○ | ◎ | ○ | △ | ◎ |
| **コミット** | ○ | ◎ | ◎ | ❌ | ◎ |
| **ブランチ操作** | ○ | ◎ | ◎ | △ | ◎ |
| **PR作成/レビュー** | ◎ | ○ | ◎ | ○ | ◎ |
| **Issue管理** | ◎ | ❌ | ◎ | ◎ | △ |
| **Actions管理** | ◎ | ❌ | ◎ | ○ | △ |
| **差分の視覚的比較** | ◎ | ◎ | △ | △ | ◎ |
| **コンフリクト解決** | △ | ◎ | △ | ❌ | ◎ |
| **Settings管理** | ◎ | ❌ | ○ | ❌ | ❌ |
| **Gitの学習しやすさ** | ○ | ◎ | △ | — | ○ |
| **自動化・スクリプト** | ❌ | ❌ | ◎ | ❌ | △ |
| **オフライン作業** | ❌ | ◎ | ◎ | ❌ | ◎ |

## 1. GitHub Web UI（ブラウザ）

ブラウザで `github.com` にアクセスして使う。最も多機能。

### できること

- リポジトリの作成・管理・設定
- コードの閲覧・簡単な編集
- PR/Issueの作成・管理・レビュー
- GitHub Actionsの設定・監視
- Organization・チーム管理
- プロフィール設定
- Marketplace（アプリ管理）

### Web上でのコード編集

**方法1: ファイルを直接編集**
1. ファイルを開く → 鉛筆アイコン（Edit）をクリック
2. 編集 → 「Commit changes」

**方法2: github.dev（ブラウザ版VS Code）**
- リポジトリで `.` キーを押す
- またはURLの `github.com` を `github.dev` に変更
- VS Codeと同じインタフェースでブラウザ上で編集可能

<!-- screenshot: github.dev の画面 -->

**方法3: Codespaces（クラウド開発環境）**
- 完全な開発環境がブラウザ上で起動する
- ターミナル、拡張機能、デバッガ全て使える
- 月60時間まで無料（Freeプラン）

### こんな人におすすめ

- Gitコマンドに不慣れな人
- リポジトリの設定やIssue管理が中心の人
- ちょっとした編集だけしたい人
- 他の人のリポジトリを閲覧・コメントしたい人

## 2. GitHub Desktop（デスクトップアプリ）

Git操作をGUIで行える**公式デスクトップアプリ**。

### インストール

- https://desktop.github.com/ からダウンロード
- macOS / Windows 対応（Linux非対応）

<!-- screenshot: GitHub Desktop メイン画面 -->

### 特徴

- **Gitコマンドを覚えなくていい** — ボタン操作で add, commit, push, pull, branch
- **差分の視覚的表示** — 変更箇所が色分けで一目瞭然
- **コンフリクト解決のUI** — マージコンフリクトをGUIで解決
- **ブランチ管理が直感的** — ドロップダウンで切り替え
- **履歴のグラフ表示** — コミット履歴をビジュアルに確認

### 基本操作

```
┌──────────────────────────────────────────────┐
│  GitHub Desktop                               │
│                                               │
│  Current Repository: [my-project ▼]           │
│  Current Branch: [main ▼]                     │
│                                               │
│  ┌────────────────┐  ┌────────────────────┐  │
│  │ Changes (3)     │  │ History            │  │
│  │                 │  │                    │  │
│  │ ☑ README.md     │  │ abc123 feat: 新機能 │  │
│  │ ☑ src/app.py    │  │ def456 fix: バグ    │  │
│  │ ☐ test.py       │  │ ghi789 docs: 更新   │  │
│  │                 │  │                    │  │
│  │ [Commit to main]│  │                    │  │
│  └────────────────┘  └────────────────────┘  │
│                                               │
│  [Push origin] [Fetch origin]                 │
└──────────────────────────────────────────────┘
```

### こんな人におすすめ

- **Git初心者** — コマンドを覚えずにGitを使いたい
- **ビジュアル派** — 差分やブランチを視覚的に確認したい
- **非エンジニア** — デザイナー、ライター、研究者など

### 他のGit GUIツール

| ツール | 料金 | 特徴 |
|--------|------|------|
| **GitHub Desktop** | 無料 | シンプル、公式 |
| **Sourcetree** | 無料 | 高機能、Atlassian製 |
| **GitKraken** | 有料（$4.95/月〜） | 美しいUI、高機能 |
| **Fork** | 有料（$49.99買い切り） | 高速、macOS/Win |
| **Tower** | 有料（$69/年〜） | プロ向け、Mac/Win |
| **Sublime Merge** | 有料（$99買い切り） | 高速検索、軽量 |

## 3. GitHub CLI (`gh`)

ターミナルからGitHubを操作する**公式コマンドラインツール**。

> **Git CLI (`git`) と GitHub CLI (`gh`) は別物:**
> - `git`: ローカルのバージョン管理（add, commit, branch, merge...）
> - `gh`: GitHubのWeb機能をターミナルから操作（PR, Issue, Actions, repo...）

### インストール

```bash
# macOS
brew install gh

# Windows
winget install --id GitHub.cli

# Linux (Debian/Ubuntu)
sudo apt install gh
```

### `git` と `gh` の使い分け

```bash
# === git コマンド（ローカル操作） ===
git add .                    # ファイルをステージ
git commit -m "メッセージ"    # コミット
git push                     # プッシュ
git branch feature           # ブランチ作成
git merge feature            # マージ

# === gh コマンド（GitHub操作） ===
gh repo create               # リポジトリ作成
gh pr create                 # PR作成
gh pr merge                  # PRマージ
gh issue create              # Issue作成
gh run list                  # Actions確認
gh release create            # リリース作成
```

### よく使うコマンド集

```bash
# 認証
gh auth login                      # ログイン
gh auth status                     # 状態確認

# リポジトリ
gh repo create name --public       # 作成
gh repo clone owner/repo           # クローン
gh repo view --web                 # ブラウザで開く
gh repo list                       # 一覧

# PR
gh pr create --title "タイトル"     # 作成
gh pr list                         # 一覧
gh pr view 42                      # 詳細
gh pr checkout 42                  # ローカルに取得
gh pr merge 42 --squash            # マージ
gh pr diff 42                      # 差分

# Issue
gh issue create                    # 作成
gh issue list --assignee "@me"     # 自分のIssue
gh issue close 42                  # クローズ

# Actions
gh run list                        # 実行一覧
gh run view ID --log               # ログ確認
gh run rerun ID                    # 再実行

# エイリアス
gh alias set prc 'pr create'      # ショートカット
```

### こんな人におすすめ

- **ターミナルで全て完結させたい人**
- **操作を自動化・スクリプト化したい人**
- **効率重視のパワーユーザー**

## 4. GitHub Mobile（スマートフォンアプリ）

iOS/Androidで使える**公式モバイルアプリ**。

### インストール

- iOS: App Store で「GitHub」を検索
- Android: Google Play で「GitHub」を検索

<!-- screenshot: GitHub Mobile のメイン画面 -->

### できること

- **通知の確認・管理** — プッシュ通知でリアルタイム
- **Issue/PRの確認・コメント** — 移動中にレビュー対応
- **PRのマージ・承認** — 急ぎのマージも外出先から
- **コードの閲覧** — スマホでコード確認
- **プロフィール・Activity確認** — コントリビューション草チェック

### できないこと

- コードの編集・コミット
- リポジトリの設定変更
- GitHub Actionsのワークフロー編集
- Organizationの管理

### こんな人におすすめ

- **通知をすぐチェックしたい人**
- **外出先でレビュー対応が必要な人**
- **草を毎日チェックしたい人**

## 5. IDE拡張機能（VS Code, JetBrains等）

エディタやIDEにGitHub連携機能を追加する。**コードを書きながらGit/GitHub操作ができる。**

### VS Code

#### 標準のGit機能（拡張不要）

VS Codeには最初からGit連携が組み込まれている：

- **ソース管理パネル** (`Cmd+Shift+G` / `Ctrl+Shift+G`)
  - 変更ファイルの一覧
  - ステージング（+ ボタン）
  - コミットメッセージ入力 → コミット
  - Push / Pull / Sync
- **ステータスバー**
  - 現在のブランチ名（クリックで切り替え）
  - 同期状態（↑ push数 ↓ pull数）
- **ファイル差分表示**
  - 変更ファイルをクリック → 左右分割で差分表示
- **インラインの変更表示**
  - エディタ内で変更箇所がガター（左端）に色表示

<!-- screenshot: VS Codeのソース管理パネル -->

#### おすすめ拡張機能

| 拡張機能 | 用途 |
|---------|------|
| **GitHub Pull Requests and Issues** | PRの作成・レビュー・Issue管理をVS Code内で |
| **GitLens** | 各行の最終変更者・日時を表示、ブランチ比較 |
| **GitHub Copilot** | AIによるコード補完 |
| **GitHub Copilot Chat** | AIとの対話でコーディング |
| **Git Graph** | ブランチのグラフを視覚的に表示 |
| **GitHub Actions** | ワークフローの状態確認 |

#### Claude Code（VS Code拡張 / CLI）

VS Code内でAIと対話しながら開発：

- コードの読み書き・レビュー
- テストの生成・実行
- コミットメッセージの自動生成
- PR/Issueの作成支援
- バグの特定・修正

```
Claude Codeの操作イメージ:
┌──────────────────────────────────────────┐
│ VS Code                                  │
│ ┌────────────────┐  ┌────────────────┐   │
│ │ エディタ        │  │ Claude Code    │   │
│ │                │  │                │   │
│ │ def calc(x):   │  │ > このバグを     │   │
│ │   return x * 2 │  │   直して        │   │
│ │                │  │                │   │
│ │                │  │ 修正しました:   │   │
│ │                │  │ return x ** 2  │   │
│ └────────────────┘  └────────────────┘   │
└──────────────────────────────────────────┘
```

### JetBrains (IntelliJ, PyCharm, WebStorm等)

JetBrains IDEにもGit/GitHub連携が標準搭載：

- **VCS メニュー** → Git操作全般
- **Git ツールウィンドウ** → ログ、ブランチ、リモート
- **GitHub連携** → PR作成・レビュー（プラグイン不要）
- **コンフリクト解決** → 3ペインのマージツール

### こんな人におすすめ

- **コーディングとGit操作を切り替えずにやりたい人**
- **PRレビューをコード横に見ながらやりたい人**
- **AI支援（Copilot / Claude Code）を使いたい人**

## どれを使うべきか？

### 初心者の場合

```
1. GitHub Web UI でアカウント作成・リポジトリ作成
2. GitHub Desktop でGitの基本操作を覚える
3. 慣れてきたら VS Code のGit機能に移行
4. さらに慣れたら git CLI + gh CLI へ
```

### 開発者の日常使い

```
メインの作業:      VS Code（コード編集 + Git操作）
PR/Issue管理:      gh CLI or Web UI
外出先:            GitHub Mobile
リポジトリ設定:     Web UI
自動化:            gh CLI（スクリプト）
```

### おすすめの組み合わせ

| レベル | 組み合わせ |
|--------|----------|
| **入門** | Web UI + GitHub Desktop |
| **初級** | VS Code + Web UI |
| **中級** | VS Code + gh CLI + Web UI |
| **上級** | ターミナル (git + gh) + VS Code |

## 次のステップ

→ [付録A: Gitコマンド早見表](appendix-a-cheatsheet.md)
→ [付録B: 用語集](appendix-b-glossary.md)
