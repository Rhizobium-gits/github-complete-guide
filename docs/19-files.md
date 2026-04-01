# 19. ファイルの扱い方 — Raw URL, 画像, LFS, サブモジュール

## GitHub上のファイル表示

### ファイルのURL構造

```
https://github.com/{owner}/{repo}/blob/{branch}/{path}
                                  ^^^^
                                  blob = ファイル表示
```

| URL要素 | 意味 | 例 |
|---------|------|-----|
| `blob` | ファイルの中身を表示 | `/blob/main/README.md` |
| `tree` | ディレクトリを表示 | `/tree/main/src/` |
| `raw` | ファイルの生データ | `/raw/main/data.csv` |
| `blame` | 各行の変更者を表示 | `/blame/main/app.py` |
| `commits` | ファイルのコミット履歴 | `/commits/main/app.py` |

### 特定の行へのリンク

ファイル表示画面で行番号をクリック → URLに `#L42` が追加される。

```
# 42行目へのリンク
https://github.com/owner/repo/blob/main/src/app.py#L42

# 42行目〜50行目のハイライト
https://github.com/owner/repo/blob/main/src/app.py#L42-L50
```

> PRやIssueでコードを参照する時に便利。

### パーマリンク（永続リンク）

ブランチ指定のURLはファイルが変更されると内容が変わる。特定コミットのURLなら永続的：

```
# ブランチ指定（内容が変わりうる）
https://github.com/owner/repo/blob/main/app.py

# コミットハッシュ指定（永続リンク）
https://github.com/owner/repo/blob/abc1234/app.py
```

ファイル表示画面で `y` キーを押すとパーマリンクに変換される。

## Raw URL（生データ）

ファイルの「生の内容」を直接取得するURL。

```
# 通常の表示URL
https://github.com/owner/repo/blob/main/data.csv

# Raw URL（生データ）
https://raw.githubusercontent.com/owner/repo/main/data.csv
```

### Rawの使い道

```bash
# スクリプトを直接ダウンロード・実行
curl -O https://raw.githubusercontent.com/owner/repo/main/install.sh

# .gitignore テンプレートをダウンロード
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore

# CSVデータを直接読み込み（Python）
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/owner/repo/main/data.csv")
```

## 画像の保存と表示

### 方法1: リポジトリに画像を保存

```
my-repo/
├── docs/
│   ├── images/         ← 画像フォルダ
│   │   ├── screenshot1.png
│   │   └── diagram.svg
│   └── guide.md
└── README.md
```

Markdownでの参照：
```markdown
<!-- 相対パス（推奨） -->
![スクリーンショット](docs/images/screenshot1.png)

<!-- READMEからの相対パス -->
![ダイアグラム](./docs/images/diagram.svg)
```

### 方法2: Issueにドラッグ＆ドロップ

1. IssueやPRのコメント欄に画像をドラッグ＆ドロップ
2. 自動的にGitHubのCDNにアップロードされる
3. URLが生成される：`https://github.com/user-attachments/assets/...`

```markdown
<!-- 生成されたURLを他の場所でも使える -->
![screenshot](https://github.com/user-attachments/assets/xxxxx)
```

> この方法はリポジトリのサイズを増やさずに画像をホストできる。

### 方法3: GitHub Wiki に保存

WikiページにアップロードしてURLを取得。

### 画像のサイズ指定

```markdown
<!-- HTMLタグでサイズ指定 -->
<img src="docs/images/screenshot.png" width="500">

<!-- 幅と高さ -->
<img src="docs/images/screenshot.png" width="400" height="300">
```

## Git LFS (Large File Storage)

大きなファイル（画像、動画、データセット、バイナリ）をGitで効率的に管理する仕組み。

通常のGitは全履歴を保持するため、大きなファイルがあるとリポジトリが肥大化する。LFSはファイルのポインタだけをGitに保存し、実体は別サーバーに保管する。

### セットアップ

```bash
# LFSのインストール
brew install git-lfs    # macOS
apt install git-lfs      # Ubuntu

# LFSの初期化（一度だけ）
git lfs install

# 追跡するファイルパターンを指定
git lfs track "*.psd"
git lfs track "*.zip"
git lfs track "data/*.csv"

# .gitattributes が自動生成される
cat .gitattributes
# *.psd filter=lfs diff=lfs merge=lfs -text
# *.zip filter=lfs diff=lfs merge=lfs -text

# .gitattributes もコミット対象
git add .gitattributes
git commit -m "Configure Git LFS"
```

### 使い方

LFS設定後は通常通り `git add`, `git commit`, `git push` するだけ。

```bash
git add large-file.zip
git commit -m "Add large dataset"
git push
```

### 容量制限

| プラン | ストレージ | 帯域 |
|--------|----------|------|
| Free | 1 GB | 1 GB/月 |
| Pro | 1 GB | 1 GB/月 |
| 追加パック | $5/月で50GBストレージ + 50GB帯域 |

## サブモジュール (Submodule)

リポジトリの中に**別のリポジトリ**を含める仕組み。

```
my-project/
├── src/
├── lib/
│   └── shared-utils/    ← 別リポジトリ（サブモジュール）
└── .gitmodules
```

### サブモジュールの追加

```bash
# サブモジュールを追加
git submodule add git@github.com:owner/shared-utils.git lib/shared-utils

# .gitmodules が作成される
cat .gitmodules
# [submodule "lib/shared-utils"]
#     path = lib/shared-utils
#     url = git@github.com:owner/shared-utils.git

git commit -m "Add shared-utils submodule"
```

### サブモジュール付きリポジトリのクローン

```bash
# クローンと同時にサブモジュールを取得
git clone --recursive git@github.com:owner/my-project.git

# または後から
git clone git@github.com:owner/my-project.git
cd my-project
git submodule init
git submodule update
```

### サブモジュールの更新

```bash
# サブモジュールを最新に更新
git submodule update --remote

# 全サブモジュールを更新
git submodule update --remote --merge
```

## GitHub上でのファイル操作

### ファイルの作成・編集

1. リポジトリページでフォルダを開く
2. 「**Add file**」→「**Create new file**」
3. ファイル名と内容を入力
4. 「**Commit changes**」をクリック

パスに `/` を含めると自動でフォルダが作成される:
```
docs/guide/getting-started.md
```

<!-- screenshot: GitHub上でのファイル作成 -->

### ファイルの検索

- **`t`キー**: ファイル名でファジー検索
- **`/`キー** または **`s`キー**: リポジトリ内検索

## 次のステップ

→ [20. READMEとドキュメント](20-readme-docs.md) でドキュメント作成を学ぼう
