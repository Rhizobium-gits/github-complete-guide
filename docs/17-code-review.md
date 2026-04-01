# 17. コードレビュー

## コードレビューとは

PRの変更内容を**他の開発者がチェックして改善を提案する**プロセス。

### なぜ必要か

- **バグの早期発見**: 本番環境に入る前に問題を見つける
- **知識の共有**: チームメンバーがお互いのコードを理解する
- **品質の向上**: 良いコードの書き方を学び合う
- **一貫性の維持**: コーディングスタイルを統一する

## レビューの仕方

### Files changed タブ

PRの「Files changed」タブで差分を確認。

<!-- screenshot: Files changedタブ -->

- 緑: 追加された行
- 赤: 削除された行
- 行をクリックしてコメントを追加

### コメントの種類

```markdown
# 通常のコメント
ここのロジック、nullチェックが必要では？

# 提案（具体的なコード修正を提示）
```suggestion
if (user != null) {
    return user.name;
}
return "Unknown";
```

# 質問
この変数名の由来は？ドメイン用語ですか？
```

### レビュー結果の送信

「Review changes」ボタンから3つの選択肢：

| 選択肢 | 意味 | アイコン |
|--------|------|---------|
| **Comment** | フィードバックのみ（承認でも拒否でもない） | 💬 |
| **Approve** | 変更を承認 | ✅ |
| **Request changes** | 修正を要求（修正されるまでマージ不可に設定可能） | ❌ |

## ブランチ保護ルール

mainブランチへの直接pushを防ぎ、レビューを必須にする。

### 設定方法

1. リポジトリ → Settings → **Branches**
2. 「Add branch protection rule」をクリック
3. Branch name pattern: `main`

<!-- screenshot: ブランチ保護設定 -->

### 主な設定項目

| 設定 | 説明 | 推奨 |
|------|------|------|
| **Require a pull request before merging** | PR経由のマージを必須 | ✅ |
| **Require approvals** | 承認レビューの数を指定 | ✅ (1-2人) |
| **Dismiss stale pull request approvals** | 新しいpush後に承認をリセット | ✅ |
| **Require review from Code Owners** | CODEOWNERSのレビューを必須 | チームによる |
| **Require status checks to pass** | CI/CDの成功を必須 | ✅ |
| **Require branches to be up to date** | mainの最新との統合を必須 | ✅ |
| **Include administrators** | 管理者にもルールを適用 | 推奨 |

```bash
# CLIでブランチ保護を設定
gh api repos/{owner}/{repo}/branches/main/protection -X PUT \
  -f "required_pull_request_reviews[required_approving_review_count]=1" \
  -F "enforce_admins=true" \
  -F "required_status_checks=null" \
  -F "restrictions=null"
```

## レビューのベストプラクティス

### レビュアーとして

1. **建設的なフィードバック**: 批判ではなく改善提案
2. **具体的に指摘**: 「ここが悪い」ではなく「こうすると良い」
3. **良い点も褒める**: モチベーション維持
4. **迅速にレビュー**: PRが長時間放置されると開発が停滞する
5. **重要度を明示**: 「Must（必須）」「Nit（些細）」「Question（質問）」

```markdown
# コメントのプレフィックス例
[Must] ここにSQLインジェクションの脆弱性があります
[Nit] 変数名は camelCase が良いかも
[Question] この実装にした理由を教えてください
[Praise] このリファクタリング素晴らしいです！
```

### PRの作成者として

1. **小さいPR**: レビューしやすい（目安: 400行以内）
2. **セルフレビュー**: 提出前に自分で見直す
3. **説明を書く**: 何を・なぜ・どう変更したか
4. **テストを含める**: テスト付きだとレビュアーが安心
5. **コンテキストを共有**: 関連するIssue番号やデザインドキュメント

## 次のステップ

→ [18. Projects](18-projects.md) でプロジェクト管理を学ぼう
