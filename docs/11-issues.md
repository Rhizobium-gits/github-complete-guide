# 11. Issue管理

## Issueとは

Issue = プロジェクトの**タスク・バグ報告・機能要望・議論**を管理するチケットシステム。

GitHubのIssueは「やること」「報告すること」「議論すること」を全て1箇所で管理できる。

## Issueの作成

### Web UIから

1. リポジトリの「**Issues**」タブ
2. 「**New issue**」をクリック
3. タイトルと説明を入力
4. 必要に応じてラベル・担当者・マイルストーンを設定
5. 「**Submit new issue**」をクリック

<!-- screenshot: Issue作成画面 -->

### CLIから

```bash
# 対話形式
gh issue create

# ワンライナー
gh issue create --title "ログイン画面が表示されない" --body "## 再現手順
1. トップページにアクセス
2. ログインボタンをクリック
3. 画面が白いまま

## 期待する動作
ログインフォームが表示される

## 環境
- OS: macOS 14
- Browser: Chrome 120"

# ラベルと担当者を指定
gh issue create --title "Add dark mode" --label "enhancement" --assignee "@me"
```

## 良いIssueの書き方

### バグ報告

```markdown
## バグの概要
ログインページで「パスワードを忘れた」リンクが機能しない

## 再現手順
1. https://example.com/login にアクセス
2. 「パスワードを忘れた方はこちら」リンクをクリック
3. → 404エラーが表示される

## 期待する動作
パスワードリセットページが表示される

## 実際の動作
404 Not Found エラーが表示される

## 環境
- OS: macOS 14.2
- ブラウザ: Chrome 120.0
- アプリバージョン: v2.3.1

## スクリーンショット
（ここに画像を貼付）
```

### 機能要望

```markdown
## 概要
ダークモードに対応してほしい

## 背景・理由
- 夜間の作業が多い
- 目の疲れを軽減したい
- 他の類似ツールは対応済み

## 提案する実装
- システム設定に連動するオプション
- ユーザー設定で手動切り替えも可能に

## 追加情報
参考: https://example.com/dark-mode-design
```

## ラベル (Labels)

Issueを分類するためのタグ。色付きで視覚的に区別できる。

### デフォルトラベル

| ラベル | 色 | 用途 |
|--------|-----|------|
| `bug` | 赤 | バグ報告 |
| `enhancement` | 青 | 機能改善・追加 |
| `documentation` | 紫 | ドキュメント関連 |
| `good first issue` | 緑 | 初心者向け |
| `help wanted` | 黄 | 助けが必要 |
| `question` | ピンク | 質問 |
| `duplicate` | グレー | 重複 |
| `invalid` | グレー | 無効 |
| `wontfix` | 白 | 修正しない |

### カスタムラベルの作成

```bash
# CLIで作成
gh label create "priority:high" --color "FF0000" --description "高優先度"
gh label create "priority:low" --color "0E8A16" --description "低優先度"
gh label create "frontend" --color "1D76DB" --description "フロントエンド関連"
gh label create "backend" --color "E4E669" --description "バックエンド関連"
```

または Issues → Labels → 「New label」

<!-- screenshot: ラベル管理画面 -->

## マイルストーン (Milestones)

Issueをリリースや期限でグループ化する。

```bash
# マイルストーン作成
gh api repos/{owner}/{repo}/milestones -f title="v2.0" -f description="バージョン2.0リリース" -f due_on="2024-06-30T00:00:00Z"
```

または Issues → Milestones → 「New milestone」

- **タイトル**: v2.0、Sprint 1 など
- **期限**: オプション
- **説明**: マイルストーンの目標

進捗がパーセンテージで表示され、プロジェクトの進行状況が一目でわかる。

## Issueの管理

### CLIでの操作

```bash
# Issue一覧
gh issue list

# 特定ラベルのIssueだけ表示
gh issue list --label "bug"

# 自分に割り当てられたIssue
gh issue list --assignee "@me"

# Issueの詳細表示
gh issue view 42

# ブラウザで開く
gh issue view 42 --web

# Issueをクローズ
gh issue close 42

# Issueを再オープン
gh issue reopen 42

# コメントを追加
gh issue comment 42 --body "修正PRを出しました: #45"
```

### IssueとPRの連携

PRのdescriptionに以下を書くと、PRがマージされた時にIssueが自動クローズされる：

```
Closes #42
Fixes #42
Resolves #42
```

複数のIssueをクローズ：
```
Closes #42, closes #43, closes #44
```

## Issueテンプレート

リポジトリに `.github/ISSUE_TEMPLATE/` ディレクトリを作成してテンプレートを配置する。

### バグ報告テンプレート

```yaml
# .github/ISSUE_TEMPLATE/bug_report.yml
name: バグ報告
description: バグを報告する
title: "[Bug]: "
labels: ["bug"]
body:
  - type: textarea
    id: description
    attributes:
      label: バグの概要
      description: 何が起きていますか？
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: 再現手順
      description: バグを再現する手順
      value: |
        1. '...' に移動
        2. '...' をクリック
        3. エラーが表示される
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: 期待する動作
    validations:
      required: true
  - type: dropdown
    id: os
    attributes:
      label: OS
      options:
        - macOS
        - Windows
        - Linux
    validations:
      required: true
```

### 機能要望テンプレート

```yaml
# .github/ISSUE_TEMPLATE/feature_request.yml
name: 機能要望
description: 新機能を提案する
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: 解決したい課題
      description: この機能で何を解決したいですか？
    validations:
      required: true
  - type: textarea
    id: solution
    attributes:
      label: 提案する解決策
    validations:
      required: true
```

## ピン留め (Pinned Issues)

重要なIssueをリポジトリのIssuesタブの上部に固定表示できる（最大3つ）。

Issue → 右サイドバーの「Pin issue」

## 次のステップ

→ [12. GitHub Actions](12-github-actions.md) でCI/CDを自動化しよう
