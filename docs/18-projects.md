# 18. GitHub Projects（プロジェクト管理）

## GitHub Projectsとは

GitHub内蔵の**プロジェクト管理ツール**。IssueやPRをカンバンボードやテーブルで管理できる。

## Projects v2

### 作成方法

1. プロフィール → **Projects** タブ → 「**New project**」
2. テンプレートを選択：
   - **Board**: カンバンボード
   - **Table**: スプレッドシート風
   - **Roadmap**: タイムライン表示
   - **Blank**: 空のプロジェクト

<!-- screenshot: Projects作成画面 -->

### ビュー（表示形式）

| ビュー | 用途 |
|--------|------|
| **Board** | カンバン方式（Todo → In Progress → Done） |
| **Table** | スプレッドシート風（カスタムフィールドを列表示） |
| **Roadmap** | タイムライン表示（日付フィールドが必要） |

### カスタムフィールド

| フィールド型 | 例 |
|-------------|-----|
| **Text** | メモ、URL |
| **Number** | ストーリーポイント、見積もり時間 |
| **Date** | 期限、開始日 |
| **Single select** | 優先度（High/Medium/Low） |
| **Iteration** | スプリント |

<!-- screenshot: カスタムフィールド設定 -->

### IssueやPRの追加

```bash
# CLIでProjectにIssueを追加
gh project item-add PROJECT_NUMBER --owner USERNAME --url https://github.com/owner/repo/issues/42
```

ボード上で `+` をクリックしてドラフトアイテムを作成することもできる。ドラフトはIssueに変換可能。

## ワークフロー自動化

Projects → Settings → **Workflows** で自動化ルールを設定：

- **Item added** → ステータスを「Todo」に設定
- **Item closed** → ステータスを「Done」に設定
- **PR merged** → ステータスを「Done」に設定
- **Code review approved** → ステータスを「In Review」に変更

<!-- screenshot: ワークフロー設定 -->

## フィルタリングとソート

テーブルビューでの操作：

```
# ステータスでフィルタ
status:Todo

# 担当者でフィルタ
assignee:username

# ラベルでフィルタ
label:bug

# 複合条件
status:Todo,In Progress assignee:@me label:bug
```

## Organizationでの活用

Projects はOrganization レベルでも作成可能。複数リポジトリのIssueを1つのボードで管理できる。

```
Organization Project: "Q1 Roadmap"
├── repo-a の Issue
├── repo-b の Issue
└── repo-c の PR
```

## 次のステップ

→ [19. ファイルの扱い方](19-files.md) でGitHub上のファイル操作を学ぼう
