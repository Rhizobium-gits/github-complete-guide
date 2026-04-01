# 15. Fork & コントリビューション（OSSへの貢献）

## Forkとは

他の人のリポジトリを**自分のアカウントにコピー**すること。コピーした先で自由に変更を加え、元のリポジトリにPRを送れる。

```
元のリポジトリ (upstream)          あなたのFork (origin)
original-author/project    →    your-name/project
     ↑                              ↓
     └──── Pull Request ────────────┘
```

## OSSへの貢献の流れ

### 1. Fork する

```bash
# CLIでFork
gh repo fork original-author/project --clone
cd project

# または Web UIで「Fork」ボタンをクリックしてからクローン
git clone git@github.com:your-name/project.git
cd project
```

<!-- screenshot: Forkボタン -->

### 2. upstreamを設定

```bash
# Fork元をupstreamとして登録
git remote add upstream git@github.com:original-author/project.git

# リモート確認
git remote -v
# origin    git@github.com:your-name/project.git (fetch)
# origin    git@github.com:your-name/project.git (push)
# upstream  git@github.com:original-author/project.git (fetch)
# upstream  git@github.com:original-author/project.git (push)
```

### 3. 最新を同期

```bash
# upstreamの最新を取得
git fetch upstream

# mainを最新に
git switch main
git merge upstream/main

# 自分のForkにもプッシュ
git push origin main
```

### 4. ブランチで作業

```bash
# 作業ブランチを作成
git switch -c fix/typo-in-readme

# 変更を加えてコミット
git add README.md
git commit -m "fix: Fix typo in installation section"

# 自分のForkにプッシュ
git push -u origin fix/typo-in-readme
```

### 5. PRを送る

```bash
gh pr create --repo original-author/project \
  --title "fix: Fix typo in README" \
  --body "READMEのインストール手順にあるタイポを修正しました"
```

または GitHub上でForkリポジトリから「Contribute」→「Open pull request」

<!-- screenshot: ForkからPRを作成 -->

### 6. レビュー対応

レビューでの修正依頼があったら：

```bash
# 同じブランチで修正
git switch fix/typo-in-readme

# 修正してコミット
git add .
git commit -m "fix: Address review feedback"
git push
# → PRに自動反映
```

## 貢献の前に確認すべきこと

### CONTRIBUTING.md

多くのプロジェクトに「貢献ガイドライン」がある。必ず先に読む。

```bash
# 確認
cat CONTRIBUTING.md
```

### Code of Conduct

行動規範。守るべきコミュニティルール。

### Issue の確認

- 「good first issue」ラベルが付いたIssueは初心者向け
- 作業前にIssueにコメントして担当を宣言する

```bash
gh issue list --repo original-author/project --label "good first issue"
```

## コントリビューションの種類

コードだけが貢献ではない：

| 種類 | 例 |
|------|-----|
| **コード** | バグ修正、新機能 |
| **ドキュメント** | README改善、翻訳 |
| **Issue報告** | バグ報告、機能提案 |
| **レビュー** | 他の人のPRをレビュー |
| **テスト** | テストケースの追加 |
| **デザイン** | UI/UXの改善 |

## 次のステップ

→ [16. Organization & Teams](16-organizations.md) で組織管理を学ぼう
