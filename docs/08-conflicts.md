# 08. コンフリクト（競合）の解決

## コンフリクトとは

2つのブランチで**同じファイルの同じ部分**が別々に変更されたとき、Gitが自動でマージできず発生する。

```
main:     "Hello World"  →  "Hello GitHub"    ← mainで変更
                \
feature:         →  "Hello Git"               ← featureでも同じ箇所を変更

→ どちらを採用すべきかGitには判断できない = コンフリクト
```

## コンフリクトの発生する場面

- `git merge` でブランチを統合するとき
- `git pull` でリモートの変更を取り込むとき
- `git rebase` でブランチを付け替えるとき
- `git cherry-pick` で特定コミットを取り込むとき

## コンフリクトの見分け方

```bash
git merge feature/login
# Auto-merging src/app.py
# CONFLICT (content): Merge conflict in src/app.py
# Automatic merge failed; fix conflicts and then commit the result.
```

```bash
git status
# On branch main
# You have unmerged paths.
#   (fix conflicts and run "git commit")
#
# Unmerged paths:
#   (use "git add <file>..." to mark resolution)
#       both modified:   src/app.py
```

## コンフリクトマーカー

コンフリクトが発生したファイルには以下のマーカーが挿入される：

```python
def greet():
<<<<<<< HEAD
    return "Hello GitHub"
=======
    return "Hello Git"
>>>>>>> feature/login
```

| マーカー | 意味 |
|---------|------|
| `<<<<<<< HEAD` | 現在のブランチ（マージ先）の変更ここから |
| `=======` | 区切り線 |
| `>>>>>>> feature/login` | マージ元ブランチの変更ここまで |

## 解決方法

### 手動で解決

1. コンフリクトマーカーを含むファイルを開く
2. どの変更を残すか決めて編集
3. マーカー（`<<<<<<<`, `=======`, `>>>>>>>`）を全て削除

**パターン1: 片方を採用**
```python
def greet():
    return "Hello GitHub"
```

**パターン2: 両方を統合**
```python
def greet():
    return "Hello GitHub and Git"
```

**パターン3: 完全に書き直す**
```python
def greet(target="World"):
    return f"Hello {target}"
```

4. 解決したファイルをステージ＆コミット：
```bash
git add src/app.py
git commit -m "Merge feature/login: resolve greeting conflict"
```

### VS Codeで解決（推奨）

VS Codeはコンフリクトを視覚的に表示し、ワンクリックで解決できる。

<!-- screenshot: VS Codeのコンフリクト解決UI -->

表示されるボタン：
- **Accept Current Change**: HEAD（マージ先）の変更を採用
- **Accept Incoming Change**: マージ元の変更を採用
- **Accept Both Changes**: 両方を残す
- **Compare Changes**: 差分を見比べる

### コマンドで一括解決

```bash
# 全てのコンフリクトで自分の変更を採用
git checkout --ours .
git add .

# 全てのコンフリクトで相手の変更を採用
git checkout --theirs .
git add .
```

### マージを中止

```bash
# マージを中止して元の状態に戻る
git merge --abort

# リベースを中止
git rebase --abort
```

## コンフリクトを防ぐコツ

1. **こまめにpull/rebase**: mainの最新を頻繁に取り込む
2. **小さいPR**: 変更が少ないほどコンフリクトしにくい
3. **担当を分ける**: 同じファイルを同時に触らない
4. **コミュニケーション**: チームで作業範囲を共有する

```bash
# 毎朝やる習慣
git switch main
git pull
git switch feature/my-work
git rebase main
```

## 複雑なコンフリクト: rerere

`rerere` (reuse recorded resolution) = 一度解決したコンフリクトを記憶して、同じパターンなら自動解決する機能。

```bash
# rerereを有効化
git config --global rerere.enabled true
```

## 次のステップ

→ [09. 履歴の操作](09-history.md) でコミット履歴を自在に操作しよう
