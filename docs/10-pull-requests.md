# 10. プルリクエスト (Pull Request / PR)

## プルリクエストとは

「自分のブランチの変更をmainに取り込んでください」という**提案**。コードレビュー・議論・CI/CDテストの場。

```
1. ブランチで開発 → 2. PRを作成 → 3. レビュー → 4. 修正 → 5. マージ
```

## PRの作成

### GitHub Web UIから

1. リポジトリページで「**Pull requests**」タブ
2. 「**New pull request**」をクリック
3. base: `main` ← compare: `feature/your-branch` を選択
4. 差分を確認
5. 「**Create pull request**」をクリック
6. タイトルと説明を入力

<!-- screenshot: PR作成画面 -->

### GitHub CLIから（推奨）

```bash
# 対話形式
gh pr create

# ワンライナー
gh pr create --title "feat: Add dark mode" --body "ダークモードを実装"

# ドラフトPR（まだレビュー準備できてない場合）
gh pr create --draft --title "WIP: New feature"

# レビュアーを指定
gh pr create --title "Fix bug" --reviewer alice,bob

# ラベルを付ける
gh pr create --title "Fix bug" --label "bug,priority:high"
```

### pushと同時に

```bash
git push -u origin feature/my-branch
# 出力にPR作成用のURLが表示される
# remote: Create a pull request for 'feature/my-branch' on GitHub by visiting:
# remote:   https://github.com/username/repo/pull/new/feature/my-branch
```

## PR の構成要素

| 要素 | 説明 |
|------|------|
| **Title** | PRの概要（簡潔に） |
| **Description** | 変更の詳細、背景、テスト方法 |
| **Reviewers** | レビューを依頼する人 |
| **Assignees** | PRの担当者 |
| **Labels** | 分類ラベル（bug, enhancement等） |
| **Projects** | 関連するプロジェクトボード |
| **Milestone** | 関連するマイルストーン |
| **Linked Issues** | 関連するIssue |

### 良いPR descriptionの例

```markdown
## 概要
ユーザー認証機能を実装しました。

## 変更内容
- JWT ベースの認証ミドルウェアを追加
- ログイン/ログアウト API エンドポイント
- パスワードハッシュ化 (bcrypt)

## テスト方法
1. `npm test` で全テスト通過を確認
2. `POST /api/login` で動作確認

## 関連Issue
Closes #42

## スクリーンショット
（UIの変更がある場合に添付）
```

### Issue との連携

PRの説明に以下のキーワードを使うと、マージ時にIssueが自動的にクローズされる：

```
Closes #42
Fixes #42
Resolves #42
```

## PRの確認・レビュー

### Web UIでレビュー

1. PRページの「**Files changed**」タブ
2. 変更された各行にコメント可能（`+` ボタンをクリック）
3. 「**Review changes**」をクリック
4. 3種類から選択：
   - **Comment**: コメントのみ
   - **Approve**: 承認
   - **Request changes**: 修正を要求

<!-- screenshot: PRレビュー画面 -->

### CLIでレビュー

```bash
# PRの一覧
gh pr list

# PRの詳細を表示
gh pr view 42

# PRの差分を表示
gh pr diff 42

# ブラウザでPRを開く
gh pr view 42 --web

# PRのブランチをチェックアウト（ローカルで動作確認）
gh pr checkout 42
```

## PRのマージ方法

GitHub上で3つのマージ方法が選べる：

### 1. Create a merge commit（デフォルト）

```
main:    A → B → C ──────→ M (マージコミット)
                  \        /
feature:           D → E →
```

- マージコミットが作られる
- ブランチの履歴がそのまま残る

### 2. Squash and merge

```
main:    A → B → C → DE (D+Eが1つのコミットに)
```

- 全コミットを1つにまとめてマージ
- 履歴がきれいになる
- 細かいWIPコミットをまとめたい時に便利

### 3. Rebase and merge

```
main:    A → B → C → D' → E'
```

- リベースしてからマージ
- マージコミットが作られない
- 直線的な履歴になる

### CLIでマージ

```bash
# マージコミット
gh pr merge 42 --merge

# スカッシュマージ
gh pr merge 42 --squash

# リベースマージ
gh pr merge 42 --rebase

# マージ後にブランチを削除
gh pr merge 42 --squash --delete-branch
```

## ドラフトPR

まだレビュー準備ができていないが、作業の進捗を共有したい場合に使う。

```bash
# ドラフトPRを作成
gh pr create --draft --title "WIP: New feature"

# ドラフトを解除（レビュー準備完了）
gh pr ready 42
```

<!-- screenshot: ドラフトPR -->

## PRテンプレート

リポジトリに `.github/pull_request_template.md` を作成すると、PR作成時に自動的にテンプレートが適用される。

```markdown
<!-- .github/pull_request_template.md -->
## 概要
<!-- 変更の概要を書いてください -->

## 変更の種類
- [ ] バグ修正
- [ ] 新機能
- [ ] 破壊的変更
- [ ] ドキュメント更新

## テスト方法
<!-- テスト手順を書いてください -->

## チェックリスト
- [ ] テストを追加/更新した
- [ ] ドキュメントを更新した
- [ ] セルフレビューを行った
```

## 次のステップ

→ [11. Issue管理](11-issues.md) でタスク管理を学ぼう
