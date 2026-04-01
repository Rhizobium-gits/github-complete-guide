# 25. ファイルの拡張子とプログラミング言語

## 拡張子とは

ファイル名の末尾に付く `.xxx` の部分。ファイルの種類（どの言語で書かれているか、何のデータか）を示す。

```
main.py       ← .py = Pythonファイル
index.html    ← .html = HTMLファイル
style.css     ← .css = CSSファイル
README.md     ← .md = Markdownファイル
```

GitHubはファイルの拡張子を見て、**シンタックスハイライト**（色分け表示）を自動適用する。

## プログラミング言語と拡張子の一覧

### Web開発

| 拡張子 | 言語/形式 | 用途 | 例 |
|--------|----------|------|-----|
| `.html` | HTML | Webページの構造 | `index.html` |
| `.css` | CSS | Webページのスタイル | `style.css` |
| `.js` | JavaScript | Webの動的処理 | `app.js` |
| `.ts` | TypeScript | 型付きJavaScript | `app.ts` |
| `.jsx` | JSX | React用JavaScript | `App.jsx` |
| `.tsx` | TSX | React用TypeScript | `App.tsx` |
| `.vue` | Vue.js | Vueコンポーネント | `Header.vue` |
| `.svelte` | Svelte | Svelteコンポーネント | `App.svelte` |
| `.php` | PHP | サーバーサイドWeb | `index.php` |
| `.scss` / `.sass` | Sass | CSS拡張言語 | `main.scss` |
| `.less` | Less | CSS拡張言語 | `theme.less` |

### 汎用プログラミング言語

| 拡張子 | 言語 | 特徴 | 主な用途 |
|--------|------|------|---------|
| `.py` | Python | 読みやすい、汎用的 | AI/ML、データ分析、Web、自動化 |
| `.js` | JavaScript | ブラウザ＆サーバー | Web開発（フロント＆バック） |
| `.ts` | TypeScript | JSに型を追加 | 大規模Web開発 |
| `.java` | Java | エンタープライズ向け | 業務システム、Android |
| `.kt` | Kotlin | モダンなJava代替 | Android、サーバー |
| `.c` | C言語 | 低レベル、高速 | OS、組み込み、ドライバ |
| `.cpp` / `.cc` | C++ | Cの拡張 | ゲーム、システム開発 |
| `.h` | C/C++ヘッダー | 宣言ファイル | ライブラリのインタフェース |
| `.cs` | C# | Microsoft製 | ゲーム(Unity)、Windows |
| `.go` | Go | Google製、高速 | サーバー、CLI、インフラ |
| `.rs` | Rust | 安全＆高速 | システム開発、WebAssembly |
| `.rb` | Ruby | 書きやすい | Web（Ruby on Rails） |
| `.swift` | Swift | Apple製 | iOS/macOS アプリ |
| `.m` | Objective-C | Apple旧世代 | iOS/macOS レガシー |
| `.dart` | Dart | Google製 | Flutter（モバイルアプリ） |
| `.scala` | Scala | JVM上の関数型 | ビッグデータ(Spark) |
| `.ex` / `.exs` | Elixir | 並行処理に強い | Webサーバー |
| `.lua` | Lua | 軽量スクリプト | ゲーム組み込み |
| `.pl` / `.pm` | Perl | テキスト処理 | レガシーシステム |
| `.zig` | Zig | モダンなC代替 | システム開発 |

### データサイエンス・科学計算

| 拡張子 | 言語/形式 | 用途 |
|--------|----------|------|
| `.py` | Python | データ分析、機械学習 |
| `.R` / `.r` | R言語 | 統計分析、可視化 |
| `.Rmd` | R Markdown | R + レポート |
| `.ipynb` | Jupyter Notebook | 対話型データ分析（Python/R） |
| `.jl` | Julia | 高速な科学計算 |
| `.m` | MATLAB | 数値計算（大学でよく使用） |
| `.nf` | Nextflow | バイオインフォパイプライン |
| `.wdl` | WDL | ワークフロー記述 |
| `.qza` / `.qzv` | QIIME 2 | メタゲノム解析のアーティファクト |

### シェル・スクリプト

| 拡張子 | 言語 | 用途 |
|--------|------|------|
| `.sh` | Bash/Shell | Linux/macOSの自動化 |
| `.bash` | Bash | Bash専用スクリプト |
| `.zsh` | Zsh | Zsh専用スクリプト |
| `.fish` | Fish | Fishシェル |
| `.ps1` | PowerShell | Windows自動化 |
| `.bat` / `.cmd` | バッチ | Windowsコマンド |

### データ・設定ファイル

| 拡張子 | 形式 | 用途 | 特徴 |
|--------|------|------|------|
| `.json` | JSON | データ交換、設定 | 構造化データ、APIの標準 |
| `.yaml` / `.yml` | YAML | 設定ファイル | 読みやすい、GitHub Actionsで使用 |
| `.toml` | TOML | 設定ファイル | Rust/Pythonプロジェクトで人気 |
| `.xml` | XML | データ、設定 | 構造化データ（やや冗長） |
| `.csv` | CSV | 表データ | カンマ区切り |
| `.tsv` | TSV | 表データ | タブ区切り |
| `.ini` / `.cfg` | INI | 設定ファイル | シンプルな設定 |
| `.env` | 環境変数 | 秘密情報 | **⚠️ .gitignoreに入れる** |
| `.properties` | Properties | Java設定 | キー=値 形式 |

### ドキュメント・テキスト

| 拡張子 | 形式 | 用途 |
|--------|------|------|
| `.md` | Markdown | READMEやドキュメント（GitHub標準） |
| `.rst` | reStructuredText | Pythonドキュメント（Sphinx） |
| `.txt` | テキスト | プレーンテキスト |
| `.adoc` | AsciiDoc | 高機能なドキュメント |
| `.tex` | LaTeX | 学術論文 |
| `.org` | Org Mode | Emacs用ドキュメント |

### Web・API定義

| 拡張子 | 形式 | 用途 |
|--------|------|------|
| `.graphql` / `.gql` | GraphQL | APIスキーマ定義 |
| `.proto` | Protocol Buffers | gRPC API定義 |
| `.swagger` | Swagger/OpenAPI | REST API定義 |

### ビルド・パッケージ管理

| ファイル名 | 言語/ツール | 用途 |
|-----------|-----------|------|
| `Makefile` | Make | ビルド定義（C/C++等） |
| `CMakeLists.txt` | CMake | クロスプラットフォームビルド |
| `Dockerfile` | Docker | コンテナイメージ定義 |
| `docker-compose.yml` | Docker Compose | 複数コンテナ管理 |
| `package.json` | npm | Node.js依存関係管理 |
| `requirements.txt` | pip | Python依存関係管理 |
| `pyproject.toml` | Python | 現代的なPython設定 |
| `Cargo.toml` | Cargo | Rust依存関係管理 |
| `go.mod` | Go Modules | Go依存関係管理 |
| `Gemfile` | Bundler | Ruby依存関係管理 |
| `build.gradle` | Gradle | Java/Kotlinビルド |
| `pom.xml` | Maven | Javaビルド |

### GitHub特有のファイル

| ファイル/フォルダ | 用途 |
|-----------------|------|
| `README.md` | プロジェクト説明（自動表示される） |
| `LICENSE` | ライセンスファイル |
| `.gitignore` | Git追跡除外設定 |
| `.gitattributes` | ファイル属性設定（LFS等） |
| `.github/` | GitHub固有の設定フォルダ |
| `.github/workflows/` | GitHub Actionsのワークフロー |
| `.github/ISSUE_TEMPLATE/` | Issueテンプレート |
| `.github/pull_request_template.md` | PRテンプレート |
| `.github/CODEOWNERS` | コードオーナー定義 |
| `.github/dependabot.yml` | Dependabot設定 |
| `.github/FUNDING.yml` | スポンサーボタン設定 |
| `CLAUDE.md` | Claude Codeへの指示ファイル |

## GitHubの言語判定

GitHubはリポジトリ内のファイルを自動解析して、使用言語の割合をカラーバーで表示する。

<!-- screenshot: GitHubの言語バー -->

この判定は [github-linguist](https://github.com/github-linguist/linguist) というツールで行われている。

### 言語判定のカスタマイズ

`.gitattributes` でファイルの言語を上書きできる：

```gitattributes
# vendorディレクトリを統計から除外
vendor/* linguist-vendored

# ドキュメントとして扱う
docs/* linguist-documentation

# 特定のファイルを別言語として認識させる
*.jsx linguist-language=JavaScript

# 生成コードとして除外
generated/* linguist-generated
```

## 拡張子が無いファイル

Gitでは拡張子が無いファイルもよく使われる：

| ファイル名 | 用途 |
|-----------|------|
| `Makefile` | ビルド定義 |
| `Dockerfile` | Dockerイメージ定義 |
| `Procfile` | Herokuプロセス定義 |
| `Vagrantfile` | Vagrant VM定義 |
| `Brewfile` | Homebrew依存定義 |
| `Rakefile` | Rubyタスク定義 |
| `.editorconfig` | エディタ設定の統一 |
| `.prettierrc` | Prettierフォーマッター設定 |
| `.eslintrc` | ESLintリンター設定 |

## ファイルの文字コード

```
UTF-8 ← 現在の標準。日本語も問題なし。GitHubもこれを前提。
Shift_JIS / EUC-JP ← レガシー。GitHubで文字化けの原因になる。
```

プロジェクト内で文字コードを統一するには `.editorconfig` を配置：

```ini
# .editorconfig
root = true

[*]
charset = utf-8
end_of_line = lf
indent_style = space
indent_size = 4
insert_final_newline = true
trim_trailing_whitespace = true

[*.md]
trim_trailing_whitespace = false

[Makefile]
indent_style = tab
```

## 次のステップ

→ [26. GitHubアプリの比較](26-github-apps.md) でデスクトップ・CLI・Web・モバイルを使い分けよう
