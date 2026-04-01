# 16. Organization & Teams

## Organizationとは

**チームでリポジトリを管理するためのアカウント**。個人アカウントとは別に、共有のリポジトリ・チーム・権限を管理できる。

```
Organization: my-team
├── Team: frontend (Alice, Bob)
│   ├── repo: web-app (write)
│   └── repo: design-system (write)
├── Team: backend (Charlie, Dave)
│   ├── repo: api-server (write)
│   └── repo: database (admin)
└── Team: everyone (全員)
    └── repo: docs (write)
```

## Organizationの作成

1. GitHub右上の「**+**」→「**New organization**」
2. プランを選択（Free で十分）
3. Organization名を入力
4. メンバーを招待

<!-- screenshot: Organization作成画面 -->

```bash
# CLIから確認
gh org list
```

## メンバーの管理

### 権限ロール

| ロール | 権限 |
|--------|------|
| **Owner** | 全権限。Org設定・メンバー管理・リポジトリ削除 |
| **Member** | チームに応じた権限 |
| **Outside Collaborator** | 特定リポジトリだけにアクセス |
| **Billing Manager** | 請求情報の管理のみ |

### メンバーの招待

1. Organization → **People** → 「**Invite member**」
2. ユーザー名またはメールで検索
3. ロールを選択して招待

## Teams（チーム）

メンバーをグループ化して、リポジトリの権限をまとめて管理。

### チームの作成

1. Organization → **Teams** → 「**New team**」
2. チーム名、説明、可視性を設定
3. メンバーを追加

<!-- screenshot: チーム管理画面 -->

### チームの権限レベル

| 権限 | Read | Triage | Write | Maintain | Admin |
|------|------|--------|-------|----------|-------|
| コード閲覧 | ✅ | ✅ | ✅ | ✅ | ✅ |
| Issue管理 | ❌ | ✅ | ✅ | ✅ | ✅ |
| Push | ❌ | ❌ | ✅ | ✅ | ✅ |
| ブランチ保護管理 | ❌ | ❌ | ❌ | ✅ | ✅ |
| 設定変更 | ❌ | ❌ | ❌ | ❌ | ✅ |

### ネストされたチーム

```
Engineering (親チーム)
├── Frontend (子チーム)
├── Backend (子チーム)
└── DevOps (子チーム)
```

子チームは親チームの権限を継承する。

## Organizationのリポジトリ

```bash
# Organizationにリポジトリを作成
gh repo create my-org/new-project --public

# Organizationのリポジトリ一覧
gh repo list my-org
```

### リポジトリの可視性

| 設定 | 説明 |
|------|------|
| **Public** | 誰でも閲覧可能 |
| **Private** | Orgメンバーのみ |
| **Internal** | Enterprise内のメンバーのみ |

## CODEOWNERS

ファイルやディレクトリの担当チーム/個人を定義。PRが作成されると自動でレビュアーに追加される。

`.github/CODEOWNERS`:
```
# デフォルト
* @my-org/engineering

# フロントエンド
/src/frontend/ @my-org/frontend
*.tsx @my-org/frontend

# バックエンド
/src/api/ @my-org/backend
*.py @my-org/backend

# ドキュメント
/docs/ @my-org/docs-team

# 設定ファイル
/.github/ @my-org/devops
```

## 次のステップ

→ [17. コードレビュー](17-code-review.md) でレビューのベストプラクティスを学ぼう
