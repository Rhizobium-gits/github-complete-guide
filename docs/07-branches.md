# 07. ブランチ操作

## ブランチとは

ブランチ = 開発の「枝分かれ」。メインのコードに影響を与えずに、独立して作業できる。

```
main:    A → B → C ─────────────→ G (マージコミット)
                  \               /
feature:           D → E → F ───
                   "新機能を開発中"
```

### なぜブランチを使うのか

- **mainブランチを常に安定した状態に保てる**
- **複数の機能を同時に開発できる**
- **失敗しても本体に影響しない**
- **コードレビューの単位になる**

## ブランチの基本操作

### ブランチの一覧表示

```bash
# ローカルブランチ一覧
git branch
# * main              ← * が付いているのが現在のブランチ
#   feature/login
#   fix/typo

# リモートブランチも含めて表示
git branch -a
# * main
#   feature/login
#   remotes/origin/main
#   remotes/origin/develop

# リモートブランチのみ表示
git branch -r

# 各ブランチの最新コミットも表示
git branch -v
```

### ブランチの作成

```bash
# ブランチを作成（切り替えはしない）
git branch feature/new-feature

# ブランチを作成して切り替え
git checkout -b feature/new-feature

# 同じく（新しい書き方）
git switch -c feature/new-feature

# 特定のコミットからブランチを作成
git checkout -b hotfix/urgent abc1234

# リモートブランチを元にローカルブランチを作成
git checkout -b feature/api origin/feature/api
# または
git switch -c feature/api origin/feature/api
```

### ブランチの切り替え

```bash
# 切り替え（従来）
git checkout main

# 切り替え（新しい書き方、推奨）
git switch main

# 直前のブランチに戻る
git switch -
```

> **checkout vs switch**: `git switch` はブランチ切り替え専用コマンドとしてGit 2.23で追加された。`checkout` はファイル復元にも使えるため紛らわしかったが、`switch` はブランチ操作のみに特化している。

### ブランチの削除

```bash
# マージ済みブランチを削除
git branch -d feature/completed

# 強制削除（未マージでも削除）
git branch -D feature/abandoned

# リモートブランチの削除
git push origin --delete feature/old-branch

# 削除されたリモートブランチの参照をクリーンアップ
git fetch --prune
```

### ブランチ名の変更

```bash
# 現在のブランチ名を変更
git branch -m new-name

# 指定したブランチ名を変更
git branch -m old-name new-name
```

## ブランチの命名規則

チーム開発では命名規則を統一するのが重要。

| プレフィックス | 用途 | 例 |
|-------------|------|-----|
| `feature/` | 新機能 | `feature/user-auth` |
| `fix/` | バグ修正 | `fix/login-crash` |
| `hotfix/` | 緊急修正 | `hotfix/security-patch` |
| `release/` | リリース準備 | `release/v2.0` |
| `docs/` | ドキュメント | `docs/api-reference` |
| `refactor/` | リファクタリング | `refactor/database-layer` |
| `test/` | テスト追加 | `test/unit-coverage` |

## マージ (merge)

別のブランチの変更を取り込む操作。

### Fast-forward マージ

mainから分岐後、mainに新しいコミットがない場合。ポインタが前に進むだけ。

```
Before:
main:     A → B → C
                    \
feature:             D → E

After (git merge feature):
main:     A → B → C → D → E
```

```bash
git switch main
git merge feature/login
# Fast-forward merge
```

### 3-way マージ

mainにも新しいコミットがある場合。マージコミットが作成される。

```
Before:
main:     A → B → C → F
                  \
feature:           D → E

After (git merge feature):
main:     A → B → C → F → G (マージコミット)
                  \       /
feature:           D → E
```

```bash
git switch main
git merge feature/login
# Merge made by the 'ort' strategy.
```

### マージの取り消し

```bash
# マージ中にコンフリクトが発生して中止したい場合
git merge --abort

# マージコミットを取り消す（マージ完了後）
git revert -m 1 HEAD
```

## リベース (rebase)

ブランチの分岐点を移動させる。履歴がきれいな直線になる。

```
Before:
main:     A → B → C → F
                  \
feature:           D → E

After (git rebase main on feature):
main:     A → B → C → F
                       \
feature:                D' → E'   ← コミットが作り直される
```

```bash
# featureブランチをmainの最新に追従させる
git switch feature/login
git rebase main

# コンフリクトが発生した場合
# 1. ファイルを編集して解決
# 2. git add で解決済みにする
# 3. リベースを続行
git rebase --continue

# リベースを中止
git rebase --abort
```

### merge vs rebase

| | merge | rebase |
|---|-------|--------|
| 履歴 | マージコミットが残る | 直線的な履歴 |
| 安全性 | 安全（履歴を変更しない） | push済みのブランチでは危険 |
| 用途 | PRのマージ | ブランチの更新 |

> **ルール**: push済み（共有済み）のブランチには rebase しない。自分のローカルブランチのみに使う。

## ブランチ戦略

### GitHub Flow（シンプル、推奨）

```
main ─────────────────────────────────────→
       \           /    \            /
        feature-A       feature-B
```

1. `main` から機能ブランチを作成
2. 作業してコミット
3. プルリクエストを作成
4. レビュー＆テスト
5. `main` にマージ
6. ブランチを削除

### Git Flow（大規模プロジェクト向け）

```
main    ──────●──────────────●──────→ (リリースのみ)
              ↑              ↑
release ──────┤   release/v2 ┤
              ↑              ↑
develop ──────●──────────────●──────→ (開発の中心)
          \       /    \        /
           feat-A       feat-B
```

ブランチ構成:
- `main`: リリース済みコード
- `develop`: 開発ブランチ
- `feature/*`: 機能ブランチ
- `release/*`: リリース準備
- `hotfix/*`: 緊急修正

### Trunk-based Development

```
main ────●────●────●────●────→
         ↑    ↑    ↑    ↑
    短命ブランチ（1-2日で完了）
```

- `main` に頻繁にマージ
- ブランチは短命（1-2日以内）
- フィーチャーフラグで未完成の機能を隠す

## 実践例

```bash
# 1. mainを最新に
git switch main
git pull

# 2. 機能ブランチを作成
git switch -c feature/dark-mode

# 3. 作業してコミット
# ... ファイルを編集 ...
git add -A
git commit -m "feat: Add dark mode toggle"

# ... さらに作業 ...
git add -A
git commit -m "feat: Implement dark mode styles"

# 4. mainの最新を取り込む（コンフリクト防止）
git fetch origin
git rebase origin/main

# 5. プッシュ
git push -u origin feature/dark-mode

# 6. PRを作成
gh pr create --title "feat: Dark mode support"

# 7. マージ後、ブランチを掃除
git switch main
git pull
git branch -d feature/dark-mode
```

## 次のステップ

→ [08. コンフリクト解決](08-conflicts.md) でマージコンフリクトに対処しよう
