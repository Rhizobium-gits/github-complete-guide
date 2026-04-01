# GitHub 完全ガイド - これを読めば全て分かる

> GitHubの全操作・全機能を日本語で網羅した完全リファレンスガイド

## このガイドについて

GitHubを初めて使う人から、チーム開発で活用したい人まで、**これ1つ読めばGitHubの全てが分かる**ことを目指したガイドです。

- 用語の意味から丁寧に解説
- 実際のコマンド例を全て記載
- スクリーンショット付きで視覚的に理解できる（`<!-- screenshot -->` 箇所に後から画像を追加）
- コピペで使えるコマンド集

## 目次

### 第1部: 基礎知識
| # | トピック | 内容 |
|---|---------|------|
| 01 | [Gitとは何か](docs/01-what-is-git.md) | Git/GitHubの違い、バージョン管理の概念、用語集 |
| 02 | [環境構築](docs/02-setup.md) | Gitのインストール、初期設定、エディタ連携 |
| 03 | [GitHubアカウント作成](docs/03-account.md) | アカウント登録、2FA設定、プロフィール設定 |
| 04 | [認証と接続](docs/04-authentication.md) | SSH鍵、HTTPS、Personal Access Token、GPG署名 |

### 第2部: Git基本操作
| # | トピック | 内容 |
|---|---------|------|
| 05 | [リポジトリの作成と管理](docs/05-repository.md) | init, clone, リモート設定、.gitignore |
| 06 | [基本ワークフロー](docs/06-basic-workflow.md) | add, commit, push, pull, status, log, diff |
| 07 | [ブランチ操作](docs/07-branches.md) | branch, checkout, switch, merge, rebase, 戦略 |
| 08 | [コンフリクト解決](docs/08-conflicts.md) | マージコンフリクトの仕組みと解決方法 |
| 09 | [履歴の操作](docs/09-history.md) | reset, revert, stash, cherry-pick, reflog |

### 第3部: GitHub機能
| # | トピック | 内容 |
|---|---------|------|
| 10 | [プルリクエスト](docs/10-pull-requests.md) | PR作成、レビュー、マージ、テンプレート |
| 11 | [Issue管理](docs/11-issues.md) | Issue作成、ラベル、マイルストーン、テンプレート |
| 12 | [GitHub Actions (CI/CD)](docs/12-github-actions.md) | ワークフロー、自動テスト、自動デプロイ |
| 13 | [GitHub Pages](docs/13-github-pages.md) | 静的サイト公開、Jekyll、カスタムドメイン |
| 14 | [Releases & Tags](docs/14-releases.md) | タグ作成、リリース管理、バイナリ配布 |

### 第4部: コラボレーション
| # | トピック | 内容 |
|---|---------|------|
| 15 | [Fork & コントリビューション](docs/15-fork-contribution.md) | Fork、upstream、OSSへの貢献方法 |
| 16 | [Organization & Teams](docs/16-organizations.md) | 組織管理、チーム権限、Enterprise |
| 17 | [コードレビュー](docs/17-code-review.md) | レビューの仕方、CODEOWNERS、保護ブランチ |
| 18 | [Projects (プロジェクト管理)](docs/18-projects.md) | Projects v2、ボード、ロードマップ |

### 第5部: 応用・カスタマイズ
| # | トピック | 内容 |
|---|---------|------|
| 19 | [ファイルの扱い方](docs/19-files.md) | Raw URL、画像保存、LFS、バイナリ、サブモジュール |
| 20 | [READMEとドキュメント](docs/20-readme-docs.md) | Markdown記法、バッジ、Wiki、プロフィールREADME |
| 21 | [GitHubのカスタマイズ](docs/21-customization.md) | テーマ、通知設定、ショートカット、GitHub CLI |
| 22 | [セキュリティ](docs/22-security.md) | Dependabot、Secret Scanning、セキュリティポリシー |
| 23 | [外部連携](docs/23-integrations.md) | Claude Code、VS Code、Slack、CI/CDツール連携 |
| 24 | [トラブルシューティング](docs/24-troubleshooting.md) | よくあるエラーと解決法、FAQ |

### 付録
| # | トピック | 内容 |
|---|---------|------|
| A | [Gitコマンド早見表](docs/appendix-a-cheatsheet.md) | 全コマンド一覧・逆引き |
| B | [用語集](docs/appendix-b-glossary.md) | GitHub関連用語の完全辞書 |

---

## スクリーンショットの追加方法

このガイド内の `<!-- screenshot: 説明 -->` 部分にスクリーンショットを追加できます。

1. スクリーンショットを撮影
2. `docs/images/` フォルダに保存（例: `docs/images/github-signup.png`）
3. `<!-- screenshot: 説明 -->` を `![説明](images/ファイル名.png)` に置き換え

## ライセンス

MIT License - 自由に使ってください。

## 貢献

誤りの修正やコンテンツの追加はPRやIssueで歓迎します。
