# 12. GitHub Actions (CI/CD)

## GitHub Actionsとは

GitHubに組み込まれた**自動化ツール**。コードのpushやPR作成をトリガーに、テスト・ビルド・デプロイを自動実行できる。

```
開発者がpush → GitHub Actionsが起動 → テスト実行 → 結果をPRに表示
                                      ↓
                                 ビルド・デプロイ
```

## 基本概念

| 用語 | 説明 |
|------|------|
| **Workflow** | 自動化の定義ファイル（`.github/workflows/` に配置） |
| **Event** | ワークフローを起動するトリガー（push, PRなど） |
| **Job** | ワークフロー内のタスクグループ |
| **Step** | Job内の個々の処理 |
| **Action** | 再利用可能な処理の単位 |
| **Runner** | ワークフローを実行するサーバー |

```
Workflow (YAMLファイル)
├── Event (トリガー: push, pull_request, schedule...)
├── Job 1 (例: テスト)
│   ├── Step 1: コードをチェックアウト
│   ├── Step 2: 依存関係をインストール
│   └── Step 3: テストを実行
└── Job 2 (例: デプロイ)
    ├── Step 1: ビルド
    └── Step 2: デプロイ
```

## 最初のワークフロー

`.github/workflows/ci.yml` を作成：

```yaml
name: CI  # ワークフロー名

on:  # トリガー
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:  # ジョブ定義
  test:  # ジョブ名
    runs-on: ubuntu-latest  # 実行環境

    steps:  # 処理ステップ
      - name: Checkout code
        uses: actions/checkout@v4  # 公式アクション

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest
```

## トリガー（Event）の種類

### よく使うトリガー

```yaml
on:
  # プッシュ時
  push:
    branches: [main, develop]
    paths: ['src/**']  # 特定パスの変更時のみ

  # PR時
  pull_request:
    branches: [main]
    types: [opened, synchronize, reopened]

  # スケジュール（cron形式）
  schedule:
    - cron: '0 0 * * *'  # 毎日0時（UTC）

  # 手動実行
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deploy target'
        required: true
        default: 'staging'
        type: choice
        options:
          - staging
          - production

  # リリース公開時
  release:
    types: [published]

  # Issue作成時
  issues:
    types: [opened]
```

## 実用的なワークフロー例

### Python プロジェクト

```yaml
name: Python CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.10', '3.11', '3.12']

    steps:
      - uses: actions/checkout@v4

      - name: Setup Python ${{ matrix.python-version }}
        uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}

      - name: Cache pip
        uses: actions/cache@v4
        with:
          path: ~/.cache/pip
          key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Lint with ruff
        run: ruff check .

      - name: Test with pytest
        run: pytest --cov=src --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v4
```

### Node.js プロジェクト

```yaml
name: Node.js CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Lint
        run: npm run lint

      - name: Test
        run: npm test

      - name: Build
        run: npm run build
```

### 自動リリース

```yaml
name: Release

on:
  push:
    tags: ['v*']

jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - uses: actions/checkout@v4

      - name: Create Release
        uses: softprops/action-gh-release@v2
        with:
          generate_release_notes: true
```

## Secrets（シークレット）

APIキーやパスワードなど秘密情報をワークフローで使う方法。

### 設定方法

1. リポジトリ → Settings → Secrets and variables → Actions
2. 「New repository secret」をクリック
3. 名前と値を入力

<!-- screenshot: Secrets設定画面 -->

```bash
# CLIで設定
gh secret set API_KEY
# → 値を入力するプロンプトが表示される
```

### 使い方

```yaml
steps:
  - name: Deploy
    env:
      API_KEY: ${{ secrets.API_KEY }}
    run: ./deploy.sh
```

## 料金

| プラン | Linux | macOS | Windows |
|--------|-------|-------|---------|
| Free | 2,000分/月 | 200分/月 | 500分/月 |
| Pro | 3,000分/月 | 300分/月 | 750分/月 |

パブリックリポジトリは**無料・無制限**。

## ワークフローの確認

```bash
# 実行一覧
gh run list

# 特定の実行の詳細
gh run view 1234567890

# ログを表示
gh run view 1234567890 --log

# 失敗したワークフローを再実行
gh run rerun 1234567890
```

<!-- screenshot: Actions実行結果画面 -->

## 次のステップ

→ [13. GitHub Pages](13-github-pages.md) でWebサイトを公開しよう
