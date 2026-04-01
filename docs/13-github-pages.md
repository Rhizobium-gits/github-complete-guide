# 第13章　GitHub Pages — Webサイトを無料で公開する

## 13.1 この章で学ぶこと

この章では、GitHubリポジトリから直接Webサイトを公開できる**GitHub Pages**について学びます。具体的には、以下の内容を扱います。

- 静的サイトホスティングとは何か、GitHub Pagesはどのような仕組みで動いているのか
- ユーザーサイト、プロジェクトサイト、カスタムドメインの3種類の公開URLの違い
- ブランチベース、GitHub Actionsベース、ユーザーサイトの3つのセットアップ方法
- Jekyllテーマを使ったサイトの見た目のカスタマイズ
- 独自ドメイン（カスタムドメイン）の設定方法とHTTPS対応

ポートフォリオサイト、プロジェクトのドキュメント、ブログ、技術メモなど、GitHub Pagesは「ちょっとしたWebサイトを手軽に公開したい」という場面で非常に便利なサービスです。サーバーの契約や管理が不要で、GitHubにコードをプッシュするだけでサイトが公開されます。

---

## 13.2 GitHub Pagesとは

### 静的サイトホスティングの概念

Webサイトには大きく分けて**動的サイト**と**静的サイト**があります。動的サイトとは、ユーザーのリクエストに応じてサーバー側でHTMLを生成するサイトです。ECサイトの商品検索結果ページやSNSのタイムラインなどが典型例です。動的サイトにはサーバーサイドのプログラム（PHP、Python、Node.jsなど）とデータベースが必要です。

一方、**静的サイト**は、あらかじめ用意されたHTML、CSS、JavaScriptファイルをそのままブラウザに配信するサイトです。内容が「静的」つまり固定であるため、サーバー側での処理が最小限で済みます。個人のポートフォリオ、プロジェクトのドキュメント、ブログなどは静的サイトとして十分に実現できます。

GitHub Pagesは、この**静的サイトのホスティング（公開）サービス**です。リポジトリに置いたHTML/CSS/JSファイルを、GitHubのサーバーが自動的にWebサイトとして配信してくれます。レンタルサーバーを契約する必要も、AWSやGCPのようなクラウドサービスの設定を行う必要もありません。

GitHub Pagesの特徴をまとめると、以下のとおりです。

- **完全無料** — パブリックリポジトリであれば無料で利用できる（プライベートリポジトリでも有料プランで利用可能）
- **HTTPS対応** — SSL証明書が自動的に発行され、セキュアな通信が標準で有効
- **Gitベースの更新** — コードをプッシュするだけでサイトが自動更新される
- **Jekyll統合** — Markdownファイルから自動的にHTMLサイトを生成できる
- **カスタムドメイン対応** — 独自のドメイン名でサイトを公開できる

ただし、静的サイトのホスティングに限定されるため、データベースを使った動的な処理やサーバーサイドのスクリプト実行はできません。また、サイトのサイズには制限があり（推奨1GB以下）、帯域幅にも月間100GBのソフトリミットが設けられています。

---

## 13.3 公開URLの形式

GitHub Pagesで公開されるWebサイトのURLは、サイトの種類によって3つの形式があります。それぞれの特徴と使い分けを理解しておきましょう。

### ユーザーサイト（User Site）

GitHubアカウントごとに1つだけ作成できる特別なサイトです。`username.github.io` というリポジトリ名でリポジトリを作成すると、自動的にそのリポジトリの内容が `https://username.github.io` というURLで公開されます。

ユーザーサイトは、自分自身の紹介ページやポートフォリオとして使われることが多いです。ルートURL（`/` で始まる）でアクセスできるため、最も短くて覚えやすいURLになります。

### プロジェクトサイト（Project Site）

個々のリポジトリごとに作成できるサイトです。リポジトリの Settings → Pages から有効化すると、`https://username.github.io/repository-name` というURLで公開されます。

たとえば、`my-library` というリポジトリでGitHub Pagesを有効化すると、`https://username.github.io/my-library` でアクセスできます。ライブラリやツールのドキュメントサイトとして広く使われています。プロジェクトサイトは数の制限がなく、リポジトリごとに1つずつ作成できます。

### カスタムドメイン

`https://username.github.io` の代わりに、自分で取得した独自ドメイン（例: `https://example.com`）でサイトを公開することもできます。ドメインレジストラ（お名前.com、Google Domains、Cloudflareなど）でドメインを取得し、DNSレコードを設定する必要があります。設定方法は後述の13.6節で詳しく解説します。

| サイトの種類 | URL形式 | リポジトリ名の条件 |
|-------------|---------|------------------|
| ユーザーサイト | `https://username.github.io` | `username.github.io`（固定） |
| プロジェクトサイト | `https://username.github.io/repo-name` | 任意 |
| カスタムドメイン | `https://your-domain.com` | 任意 |

---

## 13.4 セットアップ方法

GitHub Pagesのセットアップには3つの方法があります。プロジェクトの規模や要件に応じて使い分けましょう。

### 方法1: ブランチから公開（最もシンプル）

リポジトリの特定のブランチ・ディレクトリをそのままWebサイトとして公開する方法です。最も手軽で、設定ファイルをほとんど書く必要がありません。

1. リポジトリの「**Settings**」タブを開く
2. 左サイドバーの「**Pages**」をクリック
3. 「Build and deployment」セクションで、Sourceを「**Deploy from a branch**」に設定
4. **Branch** でブランチを選択（通常は `main`）。公開するフォルダは `/`（ルート）または `/docs` を選択
5. 「**Save**」をクリック

<!-- screenshot: GitHub Pages設定画面。SourceドロップダウンでDeploy from a branchが選択されている状態 -->

数分後には、`https://username.github.io/repo-name` でサイトにアクセスできるようになります。リポジトリのルートに `index.html` が存在すれば、それがトップページとして表示されます。`/docs` フォルダを選択した場合は、`docs/index.html` がトップページになります。

`/docs` フォルダの指定は、ソースコードとドキュメントを同じリポジトリで管理したい場合に便利です。ソースコードはリポジトリのルートに、ドキュメント（Webサイト）は `/docs` ディレクトリに置くことで、両者を明確に分離できます。

### 方法2: GitHub Actionsから公開（柔軟な方法）

静的サイトジェネレーター（Hugo、Astro、Next.jsなど）を使ってビルドしたサイトを公開する場合や、デプロイ前に何らかの処理を行いたい場合は、GitHub Actionsを使ったデプロイが適しています。

まず、Settings → Pages で Source を「**GitHub Actions**」に変更します。次に、以下のようなワークフローファイルを作成します。

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

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Pages
        uses: actions/configure-pages@v4

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: './public'    # デプロイしたいフォルダを指定

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

このワークフローのポイントをいくつか補足します。

**`permissions`** — GitHub Pagesへのデプロイには、`pages: write` と `id-token: write` の権限が必要です。これを明示的に記述しないと、デプロイステップで権限エラーが発生します。

**`concurrency`** — 複数のデプロイが同時に走ることを防ぐ設定です。`cancel-in-progress: false` にすると、先に走っているデプロイが完了するまで次のデプロイは待機します。

**`path: './public'`** — デプロイするフォルダを指定します。静的サイトジェネレーターの出力ディレクトリに合わせて変更してください（Hugo なら `./public`、Next.js の Static Export なら `./out` など）。

### 方法3: ユーザーサイトの作成

自分のGitHubアカウントのポートフォリオサイトを作成する場合は、以下の手順が最も簡単です。

1. `username.github.io` という名前のリポジトリを新規作成します（`username` は自分のGitHub ユーザー名に置き換えてください）
2. リポジトリに `index.html` を配置します
3. mainブランチにプッシュすると、自動的に `https://username.github.io` で公開されます

簡単な `index.html` の例を示します。

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            line-height: 1.6;
        }
        h1 { color: #333; }
    </style>
</head>
<body>
    <h1>Welcome!</h1>
    <p>This is my portfolio site, hosted on GitHub Pages.</p>
    <h2>Projects</h2>
    <ul>
        <li><a href="https://github.com/username/project-a">Project A</a></li>
        <li><a href="https://github.com/username/project-b">Project B</a></li>
    </ul>
</body>
</html>
```

ユーザーサイトは特別な設定なしに公開されるため、GitHub Pagesの動作を試す最も手軽な方法でもあります。

---

## 13.5 Jekyllテーマの適用

### Jekyllとは

**Jekyll**は、Ruby製の静的サイトジェネレーターです。Markdownで書いた文章を、テーマに基づいてHTMLサイトに自動変換してくれます。GitHub PagesにはJekyllが組み込まれているため、Rubyを自分のマシンにインストールしなくても、Markdownファイルをプッシュするだけでサイトが生成されます。

HTMLやCSSを一から書かなくても、プロフェッショナルな見た目のサイトが作れるのがJekyllの魅力です。技術ドキュメントやブログに特に適しています。

### テーマの設定

リポジトリのルートに `_config.yml` を作成し、使いたいテーマを指定します。

```yaml
title: My Project Documentation
description: プロジェクトの公式ドキュメント
theme: minima

# リモートテーマ（GitHub Pagesが標準サポートしていないテーマ）を使う場合
# remote_theme: pages-themes/cayman@v0.2.0
```

GitHub Pagesが標準でサポートしているテーマには、`minima`、`architect`、`cayman`、`dinky`、`hacker`、`leap-day`、`merlot`、`midnight`、`minimal`、`modernist`、`slate`、`tactile`、`time-machine` などがあります。

設定画面からテーマを選ぶこともできます。Settings → Pages → 「Theme Chooser」から、プレビューを見ながらテーマを選択できます。

<!-- screenshot: Jekyll テーマ選択画面。複数のテーマのプレビューが表示されている状態 -->

### Markdownでページを作成する

テーマを設定したら、あとはMarkdownファイルを追加するだけです。ファイルの先頭に**Front Matter**（YAML形式のメタデータ）を記述することで、Jekyllがそのファイルをページとして認識します。

```markdown
---
layout: default
title: About
---

# About This Project

This project provides a simple library for data processing.

## Features

- Fast CSV parsing
- Built-in data validation
- Export to multiple formats
```

`layout: default` は、テーマが提供するデフォルトのレイアウト（ヘッダー、フッター、ナビゲーションなどを含むHTMLの枠組み）を使用することを指示しています。`title` はページのタイトルで、ブラウザのタブやナビゲーションに表示されます。

リポジトリのルートに置いた `README.md` も、Jekyllによって自動的にトップページに変換されます。すでに `README.md` があるリポジトリであれば、テーマを設定するだけでそれなりのサイトが出来上がるのです。

---

## 13.6 カスタムドメインの設定

### なぜカスタムドメインを使うのか

`username.github.io` のURLでも十分に機能しますが、プロフェッショナルなプロジェクトや個人ブランディングのためには、独自ドメイン（例: `docs.myproject.com`）を使いたい場面があります。カスタムドメインを設定すると、GitHub Pagesのサイトに自分のドメインでアクセスできるようになります。

### DNSレコードの設定

カスタムドメインを使うには、ドメインのDNSレコードを設定して、そのドメインへのアクセスをGitHub Pagesのサーバーに向ける必要があります。設定方法は、Apex ドメイン（`example.com`）とサブドメイン（`www.example.com` や `docs.example.com`）で異なります。

**サブドメインの場合（推奨）**

ドメインレジストラのDNS設定画面で、`CNAME` レコードを追加します。

| タイプ | ホスト名 | 値 |
|--------|---------|-----|
| CNAME | `www` | `username.github.io` |

たとえば、`www.example.com` を使いたい場合は、ホスト名に `www`、値に `username.github.io` を設定します。

**Apexドメインの場合**

Apexドメイン（`example.com`）を使いたい場合は、`A` レコードでGitHub PagesのIPアドレスを指定します。

| タイプ | ホスト名 | 値 |
|--------|---------|-----|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |

4つのIPアドレスすべてを登録することで、冗長性が確保されます。

### GitHub側の設定

DNSレコードを設定したら、GitHub側でもカスタムドメインを登録します。

1. リポジトリの Settings → Pages を開く
2. 「**Custom domain**」欄にドメイン名を入力する（例: `www.example.com`）
3. 「**Save**」をクリックする
4. GitHubがDNSの設定を確認します。正しく設定されていれば、数分以内にチェックマークが表示されます
5. 「**Enforce HTTPS**」にチェックを入れる

<!-- screenshot: GitHub PagesのCustom domain設定画面。ドメイン名が入力されDNS checkが成功している状態 -->

「Save」をクリックすると、リポジトリのルートに `CNAME` という名前のファイルが自動的に作成されます。このファイルにはドメイン名が1行だけ書かれています。

```
www.example.com
```

このファイルは手動で作成しても構いません。重要なのは、このファイルがリポジトリに存在することです。

### HTTPS対応

GitHub Pagesでは、カスタムドメインに対しても**無料でSSL/TLS証明書が自動発行**されます。「Enforce HTTPS」を有効にすると、HTTPでのアクセスが自動的にHTTPSにリダイレクトされます。

DNSの設定が反映されてから証明書が発行されるまでに、最大24時間かかることがあります。「Enforce HTTPS」のチェックボックスがグレーアウトしている場合は、DNS設定の反映を待っている状態です。しばらく待ってからページを再読み込みしてみてください。

---

## 13.7 まとめ

この章では、GitHub Pagesを使ったWebサイトの公開方法を学びました。

- **GitHub Pages**は、GitHubリポジトリから直接静的Webサイトをホスティングできる無料サービスです
- **ユーザーサイト**（`username.github.io`）は1つだけ、**プロジェクトサイト**（`username.github.io/repo`）はリポジトリごとに作成できます
- セットアップは**ブランチベース**（最も簡単）、**GitHub Actionsベース**（柔軟）、**ユーザーサイト**（特定リポジトリ名）の3つの方法があります
- **Jekyll**テーマを適用すると、Markdownファイルからプロフェッショナルな見た目のサイトが自動生成されます
- **カスタムドメイン**を使う場合は、DNSレコード（CNAMEまたはAレコード）を設定し、GitHub側でドメインを登録します。HTTPSは無料で自動対応されます

GitHub Pagesは、「サーバー管理の知識がなくても、コードをプッシュするだけでWebサイトが公開できる」という手軽さが最大の魅力です。プロジェクトのドキュメント公開から個人のポートフォリオまで、幅広い用途に活用できます。

次の章では、ソフトウェアをユーザーに届ける仕組み――**リリース管理**について学びます。

---

次の章: [第14章　リリース管理 — ソフトウェアを世に届ける](14-releases.md)
