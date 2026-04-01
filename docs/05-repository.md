# 05. リポジトリの作成と管理

## リポジトリとは

リポジトリ（repo）= プロジェクトのファイル群 + 変更履歴を保存する場所。

```
my-project/              ← リポジトリ（= プロジェクトフォルダ）
├── .git/                ← Gitの管理データ（触らない）
├── .gitignore           ← Gitに無視させるファイルの指定
├── README.md            ← プロジェクト説明
├── src/                 ← ソースコード
│   └── main.py
└── tests/               ← テスト
    └── test_main.py
```

## リポジトリの作成方法

### 方法1: GitHubで作成してからクローン（推奨）

**GitHub上での操作:**

1. GitHub右上の「**+**」→「**New repository**」
2. 設定項目：

| 項目 | 説明 |
|------|------|
| **Repository name** | リポジトリ名（URLの一部になる） |
| **Description** | 簡単な説明（任意） |
| **Public / Private** | 公開 / 非公開 |
| **Add a README file** | ✅チェック推奨 |
| **Add .gitignore** | 言語に応じたテンプレを選択 |
| **Choose a license** | ライセンスを選択（OSSの場合） |

<!-- screenshot: リポジトリ作成画面 -->

3. 「**Create repository**」をクリック

**ローカルにクローン:**

```bash
# SSH（推奨）
git clone git@github.com:username/my-project.git

# HTTPS
git clone https://github.com/username/my-project.git

# GitHub CLI
gh repo clone username/my-project

# クローンしたディレクトリに移動
cd my-project
```

### 方法2: ローカルで作成してからGitHubにプッシュ

```bash
# プロジェクトフォルダを作成
mkdir my-project
cd my-project

# Gitリポジトリとして初期化
git init

# READMEを作成
echo "# My Project" > README.md

# 最初のコミット
git add README.md
git commit -m "Initial commit"

# GitHubにリモートリポジトリを作成（GitHub CLI使用）
gh repo create my-project --public --source=. --remote=origin --push
```

**GitHub CLIを使わない場合:**
1. GitHubで空のリポジトリを作成（README等のチェックを外す）
2. ローカルから接続：

```bash
git remote add origin git@github.com:username/my-project.git
git branch -M main
git push -u origin main
```

### 方法3: GitHub CLIで一発作成

```bash
# 対話形式
gh repo create

# ワンライナー
gh repo create my-project --public --clone
cd my-project
```

## クローン (clone) の詳細

`git clone` は「リモートリポジトリの完全なコピーをローカルに作成する」コマンド。

```bash
# 基本
git clone git@github.com:username/repo.git

# 別名のフォルダに保存
git clone git@github.com:username/repo.git my-folder-name

# 特定のブランチだけクローン
git clone -b develop git@github.com:username/repo.git

# 浅いクローン（履歴を最新1件だけ取得 — 高速）
git clone --depth 1 git@github.com:username/repo.git

# サブモジュールも含めてクローン
git clone --recursive git@github.com:username/repo.git
```

## リモート (remote) の管理

リモート = GitHubなど外部のリポジトリへの接続先。

```bash
# リモート一覧を表示
git remote -v
# 出力例:
# origin  git@github.com:username/repo.git (fetch)
# origin  git@github.com:username/repo.git (push)

# リモートを追加
git remote add origin git@github.com:username/repo.git

# リモートのURLを変更
git remote set-url origin git@github.com:username/new-repo.git

# リモートを削除
git remote remove origin

# リモートの詳細情報
git remote show origin
```

### リモート名の慣例

| リモート名 | 用途 |
|-----------|------|
| `origin` | 自分のリポジトリ（デフォルト） |
| `upstream` | Fork元のリポジトリ |

## .gitignore — ファイルの無視設定

Gitで管理したくないファイルを指定する。

### .gitignore の書き方

```gitignore
# コメント（#で始まる行）

# 特定のファイルを無視
secret.txt
.env

# 特定の拡張子を無視
*.log
*.tmp
*.pyc

# 特定のフォルダを無視
node_modules/
__pycache__/
.venv/
dist/
build/

# フォルダ内の特定ファイルだけ無視
docs/*.pdf

# 否定（無視しない）
!important.log

# OSが生成するファイル
.DS_Store          # macOS
Thumbs.db          # Windows
```

### 言語別テンプレート

GitHubが提供するテンプレート: https://github.com/github/gitignore

```bash
# Python用の.gitignoreをダウンロード
curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/main/Python.gitignore
```

主な言語のよく使う設定：

**Python:**
```gitignore
__pycache__/
*.py[cod]
.venv/
*.egg-info/
dist/
.env
```

**Node.js:**
```gitignore
node_modules/
dist/
.env
*.log
```

**R:**
```gitignore
.Rhistory
.RData
.Rproj.user/
```

### 既に追跡されているファイルを無視する

`.gitignore` に追加しても、既にGitで追跡されているファイルは無視されない。

```bash
# 追跡を解除（ファイルは残る）
git rm --cached secret.txt

# フォルダの追跡を解除
git rm -r --cached node_modules/

# コミット
git commit -m "Remove tracked files that should be ignored"
```

## リポジトリの設定

### GitHub上での設定

Settings タブで設定できる主な項目：

| 設定 | 場所 | 説明 |
|------|------|------|
| リポジトリ名変更 | General | リポジトリ名やVisibility変更 |
| ブランチ保護 | Branches | mainへの直接pushを禁止等 |
| Collaborators | Collaborators | 共同作業者の追加 |
| Pages | Pages | GitHub Pages の設定 |
| Secrets | Secrets and variables | CI/CD用のシークレット |
| Webhooks | Webhooks | 外部サービス連携 |

<!-- screenshot: リポジトリSettings画面 -->

### リポジトリの可視性

| 設定 | 説明 |
|------|------|
| **Public** | 誰でも閲覧可能。クローンも自由。 |
| **Private** | 招待された人だけアクセス可能。 |
| **Internal** | Organization内のメンバーのみ（Enterprise向け） |

```bash
# CLIで可視性を変更
gh repo edit --visibility public
gh repo edit --visibility private
```

### リポジトリの削除

```bash
# CLIで削除（確認あり）
gh repo delete username/repo-name --yes
```

または GitHub → Settings → 最下部の「**Delete this repository**」

> ⚠️ 削除は取り消せない。クローンしている人がいればそこにデータは残るが、GitHub上からは完全に消える。

## テンプレートリポジトリ

よく使うプロジェクト構成をテンプレートにできる。

### テンプレートの作成

1. リポジトリの Settings を開く
2. 「**Template repository**」にチェック

### テンプレートから新規作成

1. テンプレートリポジトリのページで「**Use this template**」→「**Create a new repository**」

```bash
# CLIの場合
gh repo create my-new-project --template username/template-repo
```

## 次のステップ

→ [06. 基本ワークフロー](06-basic-workflow.md) でファイルの変更をコミット・プッシュしよう
