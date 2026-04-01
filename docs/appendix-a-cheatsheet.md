# 付録A: Gitコマンド早見表

## 設定

```bash
git config --global user.name "名前"          # ユーザー名
git config --global user.email "email"        # メールアドレス
git config --global init.defaultBranch main   # デフォルトブランチ
git config --global core.editor "code --wait" # エディタ
git config --list                             # 設定一覧
```

## リポジトリ作成・取得

```bash
git init                                  # 新規作成
git clone URL                             # クローン
git clone --depth 1 URL                   # 浅いクローン
git clone -b branch URL                   # ブランチ指定クローン
```

## 基本操作

```bash
git status                        # 状態確認
git status -s                     # 短縮表示
git add ファイル                   # ステージング
git add .                         # 全変更をステージ
git add -p                        # 部分ステージ
git commit -m "メッセージ"         # コミット
git commit -am "メッセージ"        # add+commit（追跡済みのみ）
git commit --amend                # 直前コミット修正
```

## 差分確認

```bash
git diff                          # 未ステージの差分
git diff --staged                 # ステージ済みの差分
git diff branch1..branch2         # ブランチ間の差分
git diff --name-only              # ファイル名のみ
git diff --stat                   # 統計
```

## 履歴

```bash
git log                           # コミット履歴
git log --oneline                 # 1行表示
git log --oneline --graph --all   # グラフ表示
git log -5                        # 最新5件
git log -p                        # 変更内容付き
git log --author="名前"            # 著者絞り込み
git log --grep="キーワード"        # メッセージ検索
git log -- ファイル名              # ファイル履歴
git blame ファイル名               # 行ごとの変更者
git show コミットID                # コミット詳細
```

## ブランチ

```bash
git branch                        # ブランチ一覧
git branch -a                     # リモート含む一覧
git branch ブランチ名              # 作成
git branch -d ブランチ名           # 削除（マージ済み）
git branch -D ブランチ名           # 強制削除
git branch -m 新名前              # 名前変更
git switch ブランチ名              # 切り替え
git switch -c ブランチ名           # 作成+切り替え
git switch -                      # 前のブランチに戻る
git checkout ブランチ名            # 切り替え（従来）
git checkout -b ブランチ名         # 作成+切り替え（従来）
```

## マージ・リベース

```bash
git merge ブランチ名               # マージ
git merge --abort                 # マージ中止
git rebase ブランチ名              # リベース
git rebase --continue             # リベース続行
git rebase --abort                # リベース中止
git cherry-pick コミットID         # コミット取り込み
```

## リモート操作

```bash
git remote -v                     # リモート一覧
git remote add origin URL         # リモート追加
git remote set-url origin URL     # URL変更
git remote remove origin          # リモート削除
git fetch                         # リモート情報取得
git fetch --prune                 # 削除済みブランチ掃除
git pull                          # fetch + merge
git pull --rebase                 # fetch + rebase
git push                          # プッシュ
git push -u origin ブランチ名      # 上流設定+プッシュ
git push origin --delete ブランチ名 # リモートブランチ削除
git push --tags                   # 全タグをプッシュ
```

## 取り消し・復元

```bash
git restore ファイル名             # 変更を取り消し
git restore --staged ファイル名    # ステージ解除
git reset --soft HEAD~1           # コミット取消（変更残る）
git reset HEAD~1                  # コミット+ステージ取消
git reset --hard HEAD~1           # 完全に取り消し ⚠️
git revert コミットID              # 打ち消しコミット（安全）
git reflog                        # HEAD移動履歴
```

## 一時退避

```bash
git stash                         # 変更を退避
git stash save "メッセージ"        # メッセージ付き退避
git stash -u                      # 未追跡も含む
git stash list                    # 退避リスト
git stash pop                     # 復元+削除
git stash apply                   # 復元（リストに残す）
git stash drop stash@{0}          # 特定の退避を削除
git stash clear                   # 全削除
```

## タグ

```bash
git tag                           # タグ一覧
git tag -a v1.0 -m "メッセージ"    # 注釈付きタグ作成
git tag v1.0                      # 軽量タグ作成
git tag -d v1.0                   # タグ削除
git push origin v1.0              # タグをプッシュ
git push origin --tags            # 全タグをプッシュ
```

## ファイル操作

```bash
git mv 旧名 新名                  # 移動/名前変更
git rm ファイル名                  # 削除（追跡+ファイル）
git rm --cached ファイル名         # 追跡のみ解除
```

## GitHub CLI (gh)

```bash
# 認証
gh auth login                     # ログイン
gh auth status                    # 状態確認

# リポジトリ
gh repo create 名前 --public      # リポジトリ作成
gh repo clone owner/repo          # クローン
gh repo list                      # 一覧
gh repo view --web                # ブラウザで開く

# PR
gh pr create --title "タイトル"    # PR作成
gh pr list                        # PR一覧
gh pr view 番号                    # PR詳細
gh pr checkout 番号                # PRブランチを取得
gh pr merge 番号 --squash          # スカッシュマージ
gh pr diff 番号                    # 差分表示

# Issue
gh issue create --title "タイトル" # Issue作成
gh issue list                     # Issue一覧
gh issue view 番号                 # Issue詳細
gh issue close 番号                # クローズ

# リリース
gh release create v1.0             # リリース作成
gh release list                    # 一覧

# ワークフロー
gh run list                        # 実行一覧
gh run view ID                     # 詳細
gh run rerun ID                    # 再実行
```

## 逆引き

| やりたいこと | コマンド |
|------------|---------|
| 変更を元に戻したい | `git restore ファイル` |
| 直前のコミットを取り消したい | `git reset --soft HEAD~1` |
| 特定のコミットを打ち消したい | `git revert コミットID` |
| 今の作業を一旦退避したい | `git stash` |
| 消してしまったコミットを復元したい | `git reflog` で探す |
| 別ブランチの特定コミットだけ欲しい | `git cherry-pick コミットID` |
| ファイルの各行の変更者を知りたい | `git blame ファイル` |
| リモートURLを変更したい | `git remote set-url origin URL` |
| .gitignoreが効かない | `git rm --cached ファイル` |
| 特定のファイルの履歴を見たい | `git log -- ファイル` |
