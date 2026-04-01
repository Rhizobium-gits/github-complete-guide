# 22. セキュリティ

## やってはいけないこと

```
⚠️ 絶対にコミットしてはいけないもの：
- パスワード、APIキー、トークン
- .env ファイル
- 秘密鍵 (id_rsa, *.pem)
- データベースの接続情報
- AWS/GCPの認証情報
```

一度でもコミットすると、削除しても履歴に残り、誰でも見れてしまう。

### 万が一コミットしてしまったら

```bash
# 1. まずシークレットを無効化（GitHubやサービス側で）
# 2. 新しいシークレットを発行
# 3. 履歴からファイルを完全削除
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch .env' \
  --prune-empty --tag-name-filter cat -- --all

# または BFG Repo-Cleaner を使う（高速）
bfg --delete-files .env
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

## Dependabot（依存関係の自動更新）

脆弱性のあるライブラリを自動検出・更新PRを作成してくれる。

### 有効化

リポジトリ → Settings → **Code security and analysis**:
- **Dependency graph**: 有効
- **Dependabot alerts**: 有効
- **Dependabot security updates**: 有効

<!-- screenshot: Dependabot設定画面 -->

### 設定ファイル

`.github/dependabot.yml`:
```yaml
version: 2
updates:
  # Python (pip)
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    labels:
      - "dependencies"
    reviewers:
      - "username"

  # npm
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"

  # GitHub Actions
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
```

## Secret Scanning

リポジトリ内にAPIキーやトークンが含まれていないか自動スキャン。

Settings → **Code security and analysis** → **Secret scanning**: 有効

対応するシークレットの種類：
- AWS Access Key
- GitHub Token
- Google API Key
- Slack Token
- npm Token
- その他多数

## セキュリティポリシー

`SECURITY.md` をリポジトリに配置して、脆弱性の報告方法を案内：

```markdown
# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.x     | ✅ サポート中       |
| 1.x     | ❌ サポート終了     |

## Reporting a Vulnerability

脆弱性を発見した場合は、Issueではなく以下にメールで報告してください：

security@example.com

公開前に修正する時間をいただくため、公開的なIssueでの報告はお控えください。
```

## セキュリティのベストプラクティス

1. **2FA必須**: アカウントの二段階認証を有効化
2. **.gitignoreの徹底**: `.env`, 認証情報ファイルを確実に無視
3. **シークレット管理**: GitHub SecretsやVaultを使用
4. **最小権限**: PATの権限は必要最小限に
5. **定期的な更新**: Dependabotのアラートに対応
6. **ブランチ保護**: mainへの直接pushを禁止
7. **監査**: 定期的にアクセス権限を見直す

## 次のステップ

→ [23. 外部連携](23-integrations.md) でツール連携を学ぼう
