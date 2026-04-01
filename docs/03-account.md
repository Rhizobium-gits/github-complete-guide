# 03. GitHubアカウント作成とプロフィール設定

## アカウント作成

1. https://github.com にアクセス
2. 「Sign up」をクリック
3. 以下を入力：
   - **Email**: メールアドレス
   - **Password**: パスワード（15文字以上、または8文字以上で数字と小文字を含む）
   - **Username**: ユーザー名（これがURLの一部になる: `github.com/あなたのユーザー名`）
4. メール認証を完了

<!-- screenshot: GitHubサインアップ画面 -->

### ユーザー名の選び方

- URLになるので短くて覚えやすいものがよい
- 本名、ハンドルネーム、どちらでもOK
- 後から変更可能（ただしURLが変わるので注意）
- 企業やOSSでの活動を考えるなら、プロフェッショナルな名前を推奨

## 二段階認証 (2FA) の設定

GitHubでは2FAが**必須**になっている。

### 設定手順

1. GitHub → 右上のアイコン → **Settings**
2. 左メニュー → **Password and authentication**
3. 「Two-factor authentication」→ **Enable**
4. 認証アプリを選択（推奨）

<!-- screenshot: 2FA設定画面 -->

### 推奨認証アプリ

| アプリ | 対応OS | 特徴 |
|--------|--------|------|
| **1Password** | 全OS | パスワード管理と統合 |
| **Authy** | 全OS | マルチデバイス対応 |
| **Google Authenticator** | iOS/Android | シンプル |
| **Microsoft Authenticator** | iOS/Android | MS製品と統合 |

### リカバリーコードの保管

2FA設定時に**リカバリーコード**が表示される。これは**必ず安全な場所に保管**すること。

```
スマホを紛失した場合、リカバリーコードがないとアカウントにアクセスできなくなる！
```

保管場所の例：
- パスワードマネージャー
- 印刷して金庫に保管
- 暗号化されたファイル

## プロフィール設定

### 基本プロフィール

Settings → **Public profile** で設定：

| 項目 | 説明 | 例 |
|------|------|-----|
| **Name** | 表示名 | Tsubasa Tomini |
| **Bio** | 自己紹介（160文字以内） | Bioinformatics researcher / Python & R |
| **URL** | Webサイト | https://example.com |
| **Twitter username** | Xアカウント | @youraccount |
| **Company** | 所属 | @your-org |
| **Location** | 所在地 | Tokyo, Japan |
| **Pronouns** | 代名詞 | he/him, she/her, they/them |

<!-- screenshot: プロフィール設定画面 -->

### プロフィール写真

- **Settings → Public profile → Profile picture** からアップロード
- 推奨: 正方形、最低 200x200 ピクセル
- GitHub上のあらゆる場所で表示されるアイコンになる

### プロフィールREADME（自分のページをカスタマイズ）

`github.com/あなたのユーザー名` にアクセスした時に表示される自己紹介ページを作れる。

**作り方:**

1. **自分のユーザー名と同じ名前のリポジトリ**を作成（例: `Rhizobium-gits/Rhizobium-gits`）
2. 「Add a README file」にチェック
3. その `README.md` を編集

```markdown
# Hi there 👋

## About Me
- 🔬 Bioinformatics researcher
- 🌱 Currently learning metagenomics
- 💻 Python, R, Shell scripting

## GitHub Stats
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=YOUR_USERNAME&show_icons=true&theme=dark)

## Languages
![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=YOUR_USERNAME&layout=compact&theme=dark)
```

<!-- screenshot: プロフィールREADMEの表示例 -->

**よく使われるバッジ・ウィジェット:**

```markdown
<!-- GitHub Streak -->
![GitHub Streak](https://streak-stats.demolab.com/?user=YOUR_USERNAME&theme=dark)

<!-- 訪問者カウンター -->
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=YOUR_USERNAME)

<!-- スキルバッジ -->
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
```

## GitHubのプラン

| プラン | 料金 | 主な機能 |
|--------|------|---------|
| **Free** | 無料 | 無制限のパブリック/プライベートリポジトリ、GitHub Actions 2,000分/月 |
| **Pro** | $4/月 | 高度な機能、GitHub Pages制限緩和 |
| **Team** | $4/ユーザー/月 | チーム管理機能 |
| **Enterprise** | $21/ユーザー/月 | SAML SSO、監査ログ、高度なセキュリティ |

> 個人利用なら**Free**で十分。学生は**GitHub Education**で Pro 相当が無料。

### GitHub Education（学生向け）

学生証があれば申請可能：
1. https://education.github.com にアクセス
2. 「Get benefits」をクリック
3. 学生証の写真をアップロード
4. 承認されるとGitHub Pro + 各種特典が無料

## 通知設定

Settings → **Notifications** で細かく設定できる：

- **Email notifications**: メールで通知を受け取るか
- **Web notifications**: GitHub上で通知を表示するか
- **Watching**: リポジトリの監視設定
- **Subscriptions**: 購読中のIssue/PRの管理

### おすすめ設定
```
✅ Web notifications — 有効
✅ Email notifications — 重要なもののみ
❌ Automatically watch repositories — 無効にする（ノイズが多くなる）
```

## 次のステップ

→ [04. 認証と接続](04-authentication.md) でPCとGitHubを安全に接続しよう
