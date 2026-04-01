# 13. GitHub Pages — 無料でWebサイトを公開

## GitHub Pagesとは

GitHubリポジトリから直接**静的Webサイト**をホスティングできる無料サービス。

- ポートフォリオサイト
- プロジェクトのドキュメント
- ブログ
- 技術メモ

## 公開URL

| タイプ | URL形式 |
|--------|---------|
| ユーザーサイト | `https://username.github.io` |
| プロジェクトサイト | `https://username.github.io/repo-name` |
| カスタムドメイン | `https://your-domain.com` |

## セットアップ方法

### 方法1: リポジトリの設定から

1. リポジトリ → **Settings** → **Pages**
2. **Source**: 「Deploy from a branch」を選択
3. **Branch**: `main`（または `gh-pages`）を選択
4. **Folder**: `/`（ルート）または `/docs` を選択
5. 「**Save**」をクリック

<!-- screenshot: GitHub Pages設定画面 -->

数分後に `https://username.github.io/repo-name` でアクセス可能に。

### 方法2: GitHub Actionsでデプロイ

```yaml
# .github/workflows/deploy-pages.yml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - uses: actions/checkout@v4

      - name: Setup Pages
        uses: actions/configure-pages@v4

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: './public'  # デプロイするフォルダ

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 方法3: ユーザーサイト

1. `username.github.io` という名前のリポジトリを作成
2. `index.html` を配置
3. 自動的に `https://username.github.io` で公開される

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
</head>
<body>
    <h1>Welcome to my site!</h1>
    <p>This is hosted on GitHub Pages.</p>
</body>
</html>
```

## Jekyll（静的サイトジェネレーター）

GitHub PagesはJekyllを標準サポート。Markdownファイルからサイトを自動生成できる。

### テーマの適用

`_config.yml` をリポジトリのルートに作成：

```yaml
title: My Site
description: My personal website
theme: minima  # テーマ名

# リモートテーマも使える
# remote_theme: pages-themes/cayman@v0.2.0
```

### Markdownでページ作成

```markdown
---
layout: default
title: About
---

# About Me

This is my about page written in Markdown.
```

## カスタムドメイン

独自ドメインを使う方法：

1. ドメインレジストラ（お名前.com等）でDNS設定：
   - `CNAME` レコード: `username.github.io`
   - または `A` レコード:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```

2. リポジトリ → Settings → Pages → **Custom domain** にドメインを入力
3. 「Enforce HTTPS」にチェック

リポジトリのルートに `CNAME` ファイルが自動作成される：
```
your-domain.com
```

## 次のステップ

→ [14. Releases & Tags](14-releases.md) でリリース管理を学ぼう
