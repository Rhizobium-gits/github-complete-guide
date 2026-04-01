# 06. 基本ワークフロー — add, commit, push, pull

## Gitの3つのエリア

```
作業ディレクトリ        ステージングエリア        ローカルリポジトリ        リモートリポジトリ
(Working Dir)         (Staging/Index)        (Local Repo)           (Remote/GitHub)
┌──────────┐          ┌──────────┐           ┌──────────┐           ┌──────────┐
│ ファイルを │  git add  │ コミット  │ git commit │ ローカルに │  git push  │ GitHubに  │
│ 編集する   │ ───────→ │ 対象を選択│ ────────→  │ 記録される │ ────────→  │ 反映される│
│           │          │          │            │           │            │          │
│           │          │          │            │           │  git pull   │          │
│           │          │          │            │           │ ←────────  │          │
└──────────┘          └──────────┘           └──────────┘           └──────────┘
```

## 基本の流れ

```bash
# 1. 状態を確認
git status

# 2. ファイルを編集（エディタで作業）

# 3. 変更をステージに追加
git add ファイル名

# 4. コミット（ローカルに記録）
git commit -m "変更内容の説明"

# 5. プッシュ（GitHubに反映）
git push
```

## git status — 状態の確認

現在のリポジトリの状態を表示する最も重要なコマンド。

```bash
git status
```

```
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:           ← ステージ済み（緑）
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md

Changes not staged for commit:      ← 変更あるがステージされてない（赤）
  (use "git add <file>..." to update what will be committed)
        modified:   src/main.py

Untracked files:                    ← 新規ファイル（赤）
  (use "git add <file>..." to include in what will be committed)
        new-file.txt
```

```bash
# 短縮表示
git status -s
#  M README.md      ← ステージ済みの変更
# M  src/main.py    ← 未ステージの変更
# ?? new-file.txt   ← 未追跡ファイル
```

## git add — ステージング

コミットに含めるファイルを選択する。

```bash
# 特定のファイルをステージ
git add README.md

# 複数ファイルをステージ
git add file1.py file2.py

# 特定のディレクトリ内の全ファイル
git add src/

# カレントディレクトリの全変更をステージ
git add .

# 全変更をステージ（削除も含む）
git add -A

# 変更の一部だけをステージ（対話的に選択）
git add -p
```

### ステージの取り消し

```bash
# 特定ファイルのステージを解除
git restore --staged README.md

# 全ファイルのステージを解除
git restore --staged .
```

## git commit — コミット

ステージした変更をローカルリポジトリに記録する。

```bash
# メッセージ付きコミット
git commit -m "Add user authentication feature"

# 複数行メッセージ
git commit -m "Add user authentication

- Implement login/logout endpoints
- Add password hashing
- Create user session management"

# エディタでメッセージを書く
git commit
# → 設定したエディタが開く

# add + commit を同時に（追跡済みファイルのみ）
git commit -am "Fix typo in README"
```

### 良いコミットメッセージの書き方

**基本ルール:**
- 1行目: 50文字以内の要約
- 2行目: 空行
- 3行目以降: 詳細な説明（必要な場合）

**慣例的なプレフィックス:**

| プレフィックス | 用途 | 例 |
|-------------|------|-----|
| `feat:` | 新機能 | `feat: Add dark mode support` |
| `fix:` | バグ修正 | `fix: Resolve login timeout issue` |
| `docs:` | ドキュメント | `docs: Update API reference` |
| `style:` | コードスタイル | `style: Format with prettier` |
| `refactor:` | リファクタリング | `refactor: Extract helper functions` |
| `test:` | テスト | `test: Add unit tests for auth` |
| `chore:` | 雑務 | `chore: Update dependencies` |

```bash
# 良い例
git commit -m "fix: Prevent crash when user input is empty"

# 悪い例
git commit -m "fix"
git commit -m "update"
git commit -m "asdfgh"
```

### コミットの修正

```bash
# 直前のコミットメッセージを修正
git commit --amend -m "新しいメッセージ"

# 直前のコミットにファイルを追加
git add forgotten-file.py
git commit --amend --no-edit
```

> ⚠️ `--amend` はpush済みのコミットには使わないこと（履歴が変わるため）

## git push — プッシュ

ローカルのコミットをリモート（GitHub）に送信する。

```bash
# 基本のプッシュ
git push

# 初回プッシュ（上流ブランチを設定）
git push -u origin main
# -u: 次回から git push だけで OK になる

# 特定のブランチをプッシュ
git push origin feature-branch
```

### プッシュできない場合

```bash
# リモートに新しいコミットがある場合
git push
# → error: failed to push some refs

# 解決: まずpullしてからpush
git pull
git push
```

## git pull — プル

リモートの変更をローカルに取り込む。

```bash
# 基本のプル
git pull

# 特定のブランチからプル
git pull origin main

# rebaseでプル（履歴がきれいになる）
git pull --rebase
```

### pull = fetch + merge

```bash
# pullを分解すると...
git fetch          # リモートの情報を取得（ローカルは変更されない）
git merge origin/main  # 取得した変更をマージ

# fetchだけしたい場合（安全に確認したいとき）
git fetch
git log HEAD..origin/main  # リモートの新しいコミットを確認
git merge origin/main      # 問題なければマージ
```

## git log — 履歴の確認

```bash
# 基本のログ
git log

# 1行表示
git log --oneline

# グラフ表示
git log --oneline --graph --all

# 最新5件だけ
git log -5

# 特定ファイルの履歴
git log -- README.md

# 変更内容も表示
git log -p

# 統計情報付き
git log --stat

# 著者で絞り込み
git log --author="username"

# 日付で絞り込み
git log --since="2024-01-01" --until="2024-06-30"

# メッセージで検索
git log --grep="fix"
```

### きれいなログ表示（エイリアス設定推奨）

```bash
git log --oneline --graph --decorate --all
```

```
* a1b2c3d (HEAD -> main, origin/main) feat: Add dark mode
* d4e5f6g fix: Resolve login issue
| * h7i8j9k (feature/api) feat: Add REST API
|/
* k0l1m2n Initial commit
```

## git diff — 差分の確認

```bash
# ワーキングディレクトリの変更（未ステージ）
git diff

# ステージ済みの変更
git diff --staged

# 特定ファイルの差分
git diff README.md

# コミット間の差分
git diff abc1234..def5678

# ブランチ間の差分
git diff main..feature-branch

# 変更されたファイル名のみ
git diff --name-only

# 統計のみ
git diff --stat
```

## ファイルの操作

### ファイルの移動/名前変更

```bash
# Git管理下でファイル名を変更
git mv old-name.py new-name.py

# ディレクトリの移動
git mv src/utils.py lib/utils.py
```

### ファイルの削除

```bash
# Gitの追跡とファイル自体を削除
git rm unnecessary-file.py

# Gitの追跡だけ解除（ファイルは残す）
git rm --cached secret.env
```

### 変更の取り消し

```bash
# ファイルの変更を元に戻す（未ステージの変更）
git restore README.md

# 全ファイルの変更を元に戻す
git restore .

# ステージを解除（変更は保持）
git restore --staged README.md
```

## 実践: 一連の流れ

```bash
# 1. リポジトリをクローン
git clone git@github.com:username/my-project.git
cd my-project

# 2. ブランチを作成して切り替え
git checkout -b feature/add-login

# 3. ファイルを編集（エディタで作業）
code src/auth.py

# 4. 状態確認
git status

# 5. 変更をステージ
git add src/auth.py

# 6. コミット
git commit -m "feat: Add login functionality"

# 7. さらに作業してコミット...
git add src/templates/login.html
git commit -m "feat: Add login page template"

# 8. プッシュ
git push -u origin feature/add-login

# 9. GitHubでプルリクエストを作成
gh pr create --title "Add login feature" --body "Login機能を追加"
```

## 次のステップ

→ [07. ブランチ操作](07-branches.md) でブランチを使いこなそう
