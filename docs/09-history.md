# 09. 履歴の操作 — reset, revert, stash, cherry-pick

## 変更の取り消し・やり直し

### git revert — コミットを打ち消す（安全）

指定したコミットの変更を**打ち消す新しいコミット**を作成する。履歴は残る。

```
Before: A → B → C → D (HEAD)
After:  A → B → C → D → D' (Dの変更を打ち消すコミット)
```

```bash
# 直前のコミットを打ち消す
git revert HEAD

# 特定のコミットを打ち消す
git revert abc1234

# コミットメッセージを自動生成（エディタを開かない）
git revert --no-edit abc1234

# マージコミットを打ち消す
git revert -m 1 abc1234
```

> **revertは安全**: 履歴を書き換えないので、push済みのコミットにも安心して使える。

### git reset — コミットを巻き戻す（注意が必要）

HEAD（現在位置）を過去のコミットに戻す。3つのモードがある。

```
A → B → C → D (HEAD)
         ↑
    ここに戻したい
```

| モード | コミット | ステージ | ファイル | 用途 |
|--------|---------|---------|---------|------|
| `--soft` | 取り消す | 残る | 残る | コミットをやり直したい |
| `--mixed`（デフォルト） | 取り消す | 取り消す | 残る | addからやり直したい |
| `--hard` | 取り消す | 取り消す | 消える | 全て無かったことにしたい |

```bash
# 直前のコミットを取り消し（変更は残る）
git reset --soft HEAD~1

# 直前の3つのコミットを取り消し（変更はワーキングツリーに残る）
git reset HEAD~3

# 特定のコミットまで完全に戻す（変更が消える！）
git reset --hard abc1234
```

> ⚠️ `--hard` は変更が失われる。push済みのコミットには使わない。

### git restore — ファイルを元に戻す

```bash
# ワーキングツリーの変更を取り消す
git restore README.md

# ステージを解除（変更は保持）
git restore --staged README.md

# 特定のコミット時点の状態に戻す
git restore --source=abc1234 README.md
```

## git stash — 作業の一時退避

「今の作業を一旦脇に置いて、別の作業をしたい」時に使う。

```bash
# 現在の変更を退避
git stash

# メッセージ付きで退避
git stash save "WIP: login feature"

# 未追跡ファイルも含めて退避
git stash -u

# 退避リストを表示
git stash list
# stash@{0}: On feature/login: WIP: login feature
# stash@{1}: On main: temporary change

# 最新の退避を復元（stashリストからは削除）
git stash pop

# 最新の退避を復元（stashリストに残す）
git stash apply

# 特定の退避を復元
git stash apply stash@{1}

# 退避の内容を確認
git stash show -p stash@{0}

# 特定の退避を削除
git stash drop stash@{0}

# 全ての退避を削除
git stash clear
```

### 典型的な使い方

```bash
# 1. 機能開発中...
git stash                    # 作業を退避

# 2. 緊急のバグ修正
git switch main
git switch -c hotfix/urgent
# ... バグ修正 ...
git commit -am "fix: Critical bug"
git push

# 3. 元の作業に戻る
git switch feature/login
git stash pop                # 退避した作業を復元
```

## git cherry-pick — 特定のコミットだけ取り込む

別のブランチから特定のコミットだけを現在のブランチに適用する。

```
Before:
main:    A → B → C
feature: A → B → D → E → F

After (cherry-pick E):
main:    A → B → C → E'    ← Eのコミットだけ取り込む
feature: A → B → D → E → F
```

```bash
# 特定のコミットを取り込む
git cherry-pick abc1234

# 複数コミット
git cherry-pick abc1234 def5678

# 範囲指定（abc1234は含まず、def5678まで）
git cherry-pick abc1234..def5678

# コミットせずに変更だけ適用
git cherry-pick --no-commit abc1234
```

## git reflog — 「消えた」コミットを救出する

reflogはHEADの移動履歴を記録している。`reset --hard` で消してしまったコミットも復元できる。

```bash
# reflogを表示
git reflog
# abc1234 HEAD@{0}: reset: moving to HEAD~3
# def5678 HEAD@{1}: commit: Add feature X
# ghi9012 HEAD@{2}: commit: Fix bug Y

# 消してしまったコミットに戻る
git reset --hard def5678
```

> reflogは**ローカル専用**で、デフォルトで90日間保持される。

## git blame — 各行の最終変更者を表示

```bash
# ファイルの各行が誰によるコミットか表示
git blame README.md

# 特定の行範囲
git blame -L 10,20 README.md

# 出力例:
# abc1234 (Alice 2024-01-10 10:00:00 +0900  1) # My Project
# def5678 (Bob   2024-01-15 14:30:00 +0900  2) Description here
```

## 次のステップ

→ [10. プルリクエスト](10-pull-requests.md) でチーム開発の要を学ぼう
