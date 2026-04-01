# 14. Releases & Tags

## タグ (Tag) とは

特定のコミットに**名前を付ける**機能。主にバージョン番号を付けるのに使う。

```
A → B → C → D → E → F (HEAD)
         ↑       ↑
       v1.0     v2.0   ← タグ
```

### タグの種類

| 種類 | 説明 | 用途 |
|------|------|------|
| **軽量タグ** (lightweight) | コミットへのポインタだけ | 一時的なマーク |
| **注釈付きタグ** (annotated) | メッセージ・署名付き | リリースバージョン（推奨） |

### タグの操作

```bash
# 注釈付きタグを作成（推奨）
git tag -a v1.0.0 -m "Version 1.0.0 - Initial release"

# 軽量タグを作成
git tag v1.0.0

# 過去のコミットにタグを付ける
git tag -a v0.9.0 -m "Beta release" abc1234

# タグ一覧
git tag
git tag -l "v1.*"  # パターン指定

# タグの詳細
git show v1.0.0

# タグをリモートにプッシュ
git push origin v1.0.0

# 全タグをプッシュ
git push origin --tags

# タグを削除
git tag -d v1.0.0              # ローカル
git push origin --delete v1.0.0  # リモート
```

## セマンティックバージョニング (SemVer)

バージョン番号の付け方の標準規約。

```
v MAJOR . MINOR . PATCH
  ↓       ↓       ↓
  破壊的   新機能   バグ修正
  変更     追加     のみ
```

| バージョン変更 | いつ上げる | 例 |
|-------------|---------|-----|
| MAJOR (1.x.x → 2.0.0) | 互換性を壊す変更 | APIの仕様変更 |
| MINOR (1.1.x → 1.2.0) | 後方互換な新機能 | 新しいエンドポイント追加 |
| PATCH (1.1.1 → 1.1.2) | バグ修正 | typo修正、バグフィックス |

プレリリース版:
- `v1.0.0-alpha` — 初期テスト版
- `v1.0.0-beta` — ベータ版
- `v1.0.0-rc.1` — リリース候補

## リリース (Release)

GitHubのリリースはタグに加えて以下を含む：
- リリースノート（変更履歴）
- バイナリファイルなどのアセット

### リリースの作成

#### Web UIから

1. リポジトリ → **Releases** → 「**Create a new release**」
2. タグを選択または新規作成
3. リリースタイトルを入力
4. リリースノートを記入（「Generate release notes」ボタンで自動生成可）
5. 必要ならバイナリファイルをドラッグ＆ドロップ
6. 「**Publish release**」をクリック

<!-- screenshot: リリース作成画面 -->

#### CLIから

```bash
# リリース作成
gh release create v1.0.0 --title "v1.0.0" --notes "Initial release"

# リリースノートを自動生成
gh release create v1.0.0 --generate-notes

# ドラフトリリース
gh release create v1.0.0 --draft --generate-notes

# プレリリース
gh release create v1.0.0-beta --prerelease --generate-notes

# ファイルを添付
gh release create v1.0.0 ./dist/app-linux ./dist/app-mac ./dist/app-win.exe

# リリース一覧
gh release list

# リリースの詳細
gh release view v1.0.0

# アセットのダウンロード
gh release download v1.0.0
```

### 自動リリースノート

`.github/release.yml` で自動生成のカテゴリ分けをカスタマイズ：

```yaml
changelog:
  categories:
    - title: "🚀 New Features"
      labels:
        - "enhancement"
    - title: "🐛 Bug Fixes"
      labels:
        - "bug"
    - title: "📝 Documentation"
      labels:
        - "documentation"
    - title: "🔧 Maintenance"
      labels:
        - "chore"
        - "dependencies"
```

## 次のステップ

→ [15. Fork & コントリビューション](15-fork-contribution.md) でOSSに貢献する方法を学ぼう
