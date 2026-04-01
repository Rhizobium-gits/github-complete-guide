# 23. 外部連携（インテグレーション）

## VS Code との連携

### GitHub 拡張機能

| 拡張機能 | 用途 |
|---------|------|
| **GitHub Pull Requests and Issues** | VS Code内でPR/Issue操作 |
| **GitLens** | Git履歴の可視化、blame表示 |
| **GitHub Copilot** | AIコーディング支援 |
| **GitHub Copilot Chat** | AI対話型コーディング |
| **GitHub Actions** | ワークフロー管理 |

### VS Code でのGit操作

- **ソース管理パネル** (`Cmd+Shift+G`): add, commit, push, pull
- **ブランチ切り替え**: ステータスバーのブランチ名をクリック
- **差分表示**: 変更ファイルをクリック
- **インラインblame**: GitLensが各行の最終変更者を表示

<!-- screenshot: VS Codeのソース管理パネル -->

### github.dev（ブラウザ版VS Code）

リポジトリページで `.` キーを押すか、URLの `github.com` を `github.dev` に変更すると、ブラウザ上でVS Codeが起動する。

```
https://github.com/owner/repo → https://github.dev/owner/repo
```

軽い編集やコードレビューに便利。

## Claude Code との連携

### インストールと認証

```bash
# Claude Codeのインストール
npm install -g @anthropic-ai/claude-code

# 起動（初回は認証画面が開く）
claude
```

### GitHubリポジトリでの使用

```bash
cd my-project    # Gitリポジトリに移動
claude           # Claude Codeを起動

# Claude Codeに直接タスクを依頼
claude "このリポジトリのバグを修正して"
claude "テストを書いて"
claude "PRの説明を書いて"
```

### Claude Code でのGit操作

Claude Codeはリポジトリのコンテキストを理解し：
- コードの読み書き
- テストの実行
- コミットの作成
- PRの作成

を対話的に行える。

```bash
# 例: Claude Codeにコミットを依頼
> このファイルの変更をコミットして

# 例: PRを作成
> この変更でPRを作って
```

### VS Code拡張として

VS Code内でClaude Codeを使用可能。コマンドパレットから操作。

## GitHub Apps / OAuth Apps

### GitHub Marketplace

https://github.com/marketplace で便利なアプリを探せる：

| カテゴリ | 例 |
|---------|-----|
| CI/CD | CircleCI, Travis CI |
| コード品質 | Codecov, SonarCloud |
| プロジェクト管理 | Jira, Linear |
| セキュリティ | Snyk, Socket |
| デプロイ | Vercel, Netlify, Railway |
| チャット | Slack, Discord |

### アプリのインストール

1. GitHub Marketplace でアプリを選択
2. 「Install」をクリック
3. 権限を確認して許可
4. 対象リポジトリを選択（全リポジトリ or 特定のリポジトリ）

### インストール済みアプリの管理

Settings → **Applications** → **Installed GitHub Apps**

<!-- screenshot: インストール済みアプリ一覧 -->

## Slack連携

### GitHub for Slack

```
# Slackで以下のコマンドを実行
/github subscribe owner/repo

# 通知されるイベント
- Issues
- Pull Requests
- Deployments
- Releases
```

カスタマイズ：
```
/github subscribe owner/repo issues pulls deployments releases
/github unsubscribe owner/repo issues
```

## Webhook

特定のイベントが起きたとき、外部URLにHTTPリクエストを送信する。

### 設定

リポジトリ → Settings → **Webhooks** → 「Add webhook」

| 設定 | 説明 |
|------|------|
| **Payload URL** | リクエスト送信先URL |
| **Content type** | `application/json` |
| **Secret** | 署名検証用の秘密鍵 |
| **Events** | どのイベントでトリガーするか |

### よく使うイベント

- `push` — コードがプッシュされた
- `pull_request` — PRが作成・更新された
- `issues` — Issueが作成・更新された
- `release` — リリースが公開された
- `workflow_run` — GitHub Actionsが完了した

## GitHub API

プログラムからGitHubを操作できるREST API / GraphQL API。

### REST API の使用

```bash
# GitHub CLIで簡単に呼べる
gh api repos/owner/repo
gh api repos/owner/repo/issues

# curlの場合
curl -H "Authorization: token YOUR_TOKEN" \
  https://api.github.com/repos/owner/repo

# リポジトリ情報
gh api repos/owner/repo --jq '.stargazers_count'

# Issue一覧
gh api repos/owner/repo/issues --jq '.[].title'

# PRのコメント
gh api repos/owner/repo/pulls/42/comments
```

### GraphQL API

```bash
# GraphQLクエリ
gh api graphql -f query='
  query {
    repository(owner: "owner", name: "repo") {
      issues(first: 5, states: OPEN) {
        nodes {
          title
          url
        }
      }
    }
  }
'
```

## Gist（コードスニペット共有）

短いコードや設定ファイルを手軽に共有する機能。

```bash
# Gistを作成
gh gist create file.py --public --desc "Useful utility function"

# 複数ファイル
gh gist create file1.py file2.py

# stdinから
echo "print('hello')" | gh gist create --filename hello.py

# Gist一覧
gh gist list

# Gistを表示
gh gist view GIST_ID
```

URL: `https://gist.github.com/username/gist_id`

## 次のステップ

→ [24. トラブルシューティング](24-troubleshooting.md) でよくある問題の解決法を学ぼう
