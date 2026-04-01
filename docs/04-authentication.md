# 第4章　認証と接続 — パソコンとGitHubを安全につなぐ

## 4.1　この章で学ぶこと

本章では、自分のパソコンとGitHubの間に「安全な通信路」を確立する方法を学びます。前章まででGitのインストールとGitHubアカウントの作成が完了しましたが、それだけではパソコンからGitHubにコードを送ったり、GitHubからコードを取得したりすることはできません。「このパソコンからの操作は、確かにこのGitHubアカウントの持ち主によるものである」という証明、つまり**認証**が必要です。

具体的には、以下の内容を学びます。

- そもそも**なぜ認証が必要なのか**というセキュリティの基本的な考え方
- **SSH**、**HTTPS + Personal Access Token**、**GitHub CLI** という3つの接続方式の比較
- 最も広く推奨されている**SSH鍵による接続**の設定方法（公開鍵暗号の仕組みも含めて）
- HTTPS接続で使う**Personal Access Token（PAT）**の作成と管理
- コマンド一つで認証を完了できる**GitHub CLI**の活用
- コミットが本当に自分のものであることを証明する**GPG署名**
- 仕事用と個人用など、**複数アカウントの使い分け**方

認証の設定は、一度行えば日常的にやり直す必要はありません。しかし、仕組みを理解しておくことで、トラブルが起きたときに自分で対処できるようになります。少し難しく感じるかもしれませんが、一つずつ丁寧に進めていきましょう。

---

## 4.2　なぜ認証が必要なのか

GitHubにコードをアップロード（プッシュ）したり、プライベートリポジトリのコードをダウンロード（クローン）したりする操作を考えてみましょう。もし認証の仕組みがなかったらどうなるでしょうか。

誰でも他人のリポジトリにコードを書き込めてしまいます。悪意のある人がプロジェクトのコードを改ざんしたり、プライベートなコードを盗み見たりすることが可能になります。これは、鍵のかかっていない家に等しい状態です。

認証とは、「あなたが本当にあなたであること」を確認するプロセスです。GitHubにパソコンからアクセスする際、「このアクセスは、GitHubアカウント `tsubasa` の持ち主からのものです」ということを、何らかの方法で証明する必要があります。

以前は、ユーザー名とパスワードを入力するだけで認証できましたが、GitHubは2021年にパスワード認証を廃止しました。パスワードは盗まれやすく、使い回しのリスクもあるためです。現在は、より安全な認証方式のみが利用可能になっています。

---

## 4.3　接続方式の比較

GitHubとの接続方法は、大きく分けて3つあります。それぞれに特徴があり、状況に応じて使い分けることができます。

| 方式 | セキュリティ | 手軽さ | 推奨度 | 特徴 |
|------|------------|--------|--------|------|
| **SSH鍵** | 非常に高い | 初回設定にやや手間がかかる | 最も推奨 | 一度設定すれば認証情報の入力が不要になる |
| **HTTPS + PAT** | 高い | トークンの管理が必要 | 状況に応じて | 企業のファイアウォール内でも通りやすい |
| **GitHub CLI** | 非常に高い | 最も簡単 | 推奨 | コマンド一つで対話的に設定できる |

**初心者の方へのおすすめ**は、GitHub CLI（`gh`）を使う方法です。対話形式で質問に答えていくだけで、裏側でSSH鍵の生成やGitHubへの登録まで自動的に行ってくれます。

一方、**SSH鍵の仕組みを理解しておくこと**は、GitHub CLI を使う場合でも重要です。トラブルシューティングの際や、GitHub以外のGitサービス（GitLab、Bitbucket など）を使う際にも必ず役立ちます。そのため、本章ではSSH鍵の解説を最も詳しく行います。

---

## 4.4　SSH鍵による接続（推奨）

### 公開鍵暗号の仕組み — 南京錠のたとえ

SSH鍵を理解するために、まず「公開鍵暗号」という仕組みを平易に説明します。

公開鍵暗号は、2つの鍵を使う暗号方式です。たとえ話で説明しましょう。

あなたが誰かに秘密のメッセージを送りたいとします。従来の方法（共通鍵暗号）では、一つの鍵で箱を施錠し、同じ鍵で開錠します。しかし、その鍵をどうやって相手に安全に渡すかという問題があります。鍵を配送中に盗まれたら、メッセージも読まれてしまいます。

公開鍵暗号は、この問題を巧妙に解決します。仕組みはこうです。

1. あなたは「**南京錠**」（公開鍵）と「**南京錠を開ける鍵**」（秘密鍵）のペアを作ります
2. 南京錠（公開鍵）は世界中にばらまいても構いません。誰でも持って行ってOKです
3. メッセージを送りたい人は、あなたの南京錠で箱を施錠して送ります
4. その箱を開けられるのは、南京錠を開ける鍵（秘密鍵）を持っているあなただけです

SSH鍵もこれと同じ原理です。

- **公開鍵**（`id_ed25519.pub`）：GitHubに登録します。「南京錠」に相当します
- **秘密鍵**（`id_ed25519`）：自分のパソコンに保管します。「南京錠を開ける鍵」に相当します。**絶対に他人に渡してはいけません**

```
あなたのPC                          GitHub
┌────────────────┐                ┌────────────────┐
│ 秘密鍵 🔑      │ ←── 認証 ──→  │ 公開鍵 🔓      │
│ (~/.ssh/       │                │ (Settings →    │
│  id_ed25519)   │                │  SSH keys)     │
└────────────────┘                └────────────────┘
```

GitHubにアクセスするとき、GitHubは「この公開鍵に対応する秘密鍵を持っていますか？」と確認します。あなたのパソコンが秘密鍵を使って正しく応答できれば、「本人である」と認められます。秘密鍵そのものがネットワーク上を流れることはないため、非常に安全です。

### SSH鍵の生成

それでは、実際にSSH鍵を生成しましょう。ターミナルを開いて次のコマンドを実行します。

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

各オプションの意味を説明します。

- `-t ed25519`：鍵の種類（アルゴリズム）を指定しています。Ed25519 は現在最も推奨されているアルゴリズムで、RSAよりも短い鍵長で同等以上のセキュリティを提供します。古い環境で Ed25519 がサポートされていない場合は、`-t rsa -b 4096` を使ってください。
- `-C "your-email@example.com"`：コメントを付加します。このコメントは鍵の識別に使われるもので、認証には影響しません。GitHubに登録したメールアドレスを入れておくのが慣例です。

コマンドを実行すると、いくつかの質問が表示されます。

```
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/you/.ssh/id_ed25519):
```

鍵の保存場所を聞かれています。特に理由がなければ、そのまま Enter キーを押してデフォルトの場所に保存してください。

```
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```

次に**パスフレーズ**の設定を求められます。パスフレーズは、秘密鍵に追加のパスワードをかけるものです。パスフレーズを設定しておくと、万が一パソコンが盗まれたり、秘密鍵ファイルが流出したりしても、パスフレーズを知らなければ鍵を使うことができません。

セキュリティの観点から、パスフレーズの設定を強くおすすめします。後述するSSHエージェントを使えば、パスフレーズを毎回手入力する手間も省けます。

鍵の生成が完了すると、`~/.ssh/` ディレクトリに以下の2つのファイルが作成されます。

- `id_ed25519`：秘密鍵。このファイルは絶対に他人と共有しないでください。
- `id_ed25519.pub`：公開鍵。このファイルの内容をGitHubに登録します。

### SSHエージェントに鍵を登録する

SSHエージェントは、秘密鍵をメモリ上に保持してくれるプログラムです。エージェントに鍵を登録しておくと、SSH接続のたびにパスフレーズを入力する必要がなくなります。自動車でいえば、エンジンをかけるたびにキーを回す代わりに、スマートキーで自動的にエンジンがかかるようなイメージです。

まず、SSHエージェントをバックグラウンドで起動します。

```bash
eval "$(ssh-agent -s)"
```

`Agent pid 12345` のような出力が表示されれば、エージェントが起動しています。

**macOSの場合**は、SSH設定ファイルを作成（または編集）して、Keychainとの連携を設定します。

```bash
cat >> ~/.ssh/config << 'EOF'
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
EOF
```

この設定の意味を解説します。

- `Host github.com`：以下の設定が `github.com` への接続時に適用されることを示します
- `AddKeysToAgent yes`：鍵を使用する際に自動的にSSHエージェントに追加します
- `UseKeychain yes`：macOSのKeychain（パスワード管理機能）にパスフレーズを保存します。これにより、パソコンを再起動してもパスフレーズの再入力が不要になります
- `IdentityFile ~/.ssh/id_ed25519`：使用する秘密鍵のファイルパスを指定します

次に、鍵をエージェントに追加します。

```bash
# macOSの場合
ssh-add --apple-use-keychain ~/.ssh/id_ed25519

# Linuxの場合
ssh-add ~/.ssh/id_ed25519
```

パスフレーズを設定している場合、ここで入力を求められます。一度入力すれば、以降はエージェントが自動的に処理してくれます。

### 公開鍵をGitHubに登録する

生成した公開鍵をGitHubに登録します。まず、公開鍵の内容をクリップボードにコピーします。

```bash
# macOSの場合
pbcopy < ~/.ssh/id_ed25519.pub

# Linuxの場合（xclipがインストールされている場合）
xclip -selection clipboard < ~/.ssh/id_ed25519.pub

# または、内容を表示して手動でコピー
cat ~/.ssh/id_ed25519.pub
```

公開鍵は `ssh-ed25519 AAAA...` で始まる1行のテキストです。

次に、GitHubのWebサイトで以下の操作を行います。

1. GitHubにログインし、右上のアイコンから **Settings** を開きます
2. 左側のメニューから **SSH and GPG keys** を選択します
3. 「**New SSH key**」ボタンをクリックします
4. **Title**：この鍵を識別するための名前を入力します。「MacBook Pro 2024」や「自宅デスクトップ」など、どのパソコンの鍵かがわかる名前にしましょう
5. **Key type**：「Authentication Key」を選択します
6. **Key**：コピーした公開鍵を貼り付けます
7. 「**Add SSH key**」をクリックします

<!-- screenshot: SSH鍵の追加画面 -->

GitHubのパスワード入力を求められることがありますが、これはセキュリティ上の確認です。

### 接続テスト

設定が正しくできたかどうかを確認しましょう。

```bash
ssh -T git@github.com
```

初めて接続する場合、以下のようなメッセージが表示されることがあります。

```
The authenticity of host 'github.com (20.27.177.113)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvSqA3npr5lFzhzg6hcJkiGk....
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

これは「このサーバーに初めて接続しますが、本当に接続しますか？」という確認です。`yes` と入力してください。GitHubのフィンガープリント（サーバーの指紋）は、GitHubの公式ドキュメントで公開されていますので、心配な場合は照合することもできます。

接続に成功すると、以下のメッセージが表示されます。

```
Hi username! You've been successfully authenticated, but GitHub does not provide shell access.
```

「shell access」（シェルへのアクセス）は提供されないと書かれていますが、これは正常です。GitHubはGitリポジトリのホスティングサービスであり、サーバーにログインして操作するサービスではないためです。認証自体は成功しています。

### SSH接続でリポジトリを操作する

SSH接続が確立できたら、以降はSSH形式のURLを使ってリポジトリを操作します。

```bash
# SSHのURLでリポジトリをクローン
git clone git@github.com:username/repo.git

# 既存リポジトリのリモートURLをSSHに変更する場合
git remote set-url origin git@github.com:username/repo.git
```

SSH形式のURLは `git@github.com:ユーザー名/リポジトリ名.git` という形式です。HTTPS形式の `https://github.com/...` とは異なることに注意してください。GitHubのリポジトリページで「Code」ボタンをクリックすると、「SSH」タブでこのURLを確認できます。

---

## 4.5　HTTPS + Personal Access Token

SSH鍵の代わりに、HTTPS接続と Personal Access Token（PAT）を使う方法もあります。企業のネットワーク環境ではSSHポート（22番）がファイアウォールでブロックされていることがあり、その場合はHTTPS（443番ポート）を使うこの方式が有効です。

### Personal Access Token（PAT）とは

PATは、パスワードの代わりに使用する「トークン（文字列）」です。GitHubのパスワードとは別に生成され、有効期限や権限の範囲を細かく設定できます。パスワードがアカウント全体の「万能鍵」だとすれば、PATは「特定の部屋だけ開けられる鍵」のようなものです。

### PATの作成手順

1. GitHubにログインし、右上のアイコンから **Settings** を開きます
2. 左側メニューの一番下にある **Developer settings** をクリックします
3. **Personal access tokens** → **Tokens (classic)** を選択します
4. 「**Generate new token (classic)**」をクリックします

<!-- screenshot: PAT作成画面 -->

以下の項目を設定します。

**Note（メモ）**：このトークンの用途を書きます。「MacBook 開発用」「CI/CD パイプライン用」など、後から見て何のために作ったトークンかがわかる名前にしてください。

**Expiration（有効期限）**：トークンの有効期間を設定します。90日程度が推奨されます。有効期限を設定しないこともできますが、セキュリティの観点からおすすめしません。期限が切れたら、新しいトークンを生成して差し替えます。

**Scopes（スコープ = 権限範囲）**：このトークンにどの操作を許可するかを選択します。

### スコープの選び方

| スコープ | 用途 | 必要な場面 |
|---------|------|-----------|
| `repo` | リポジトリの読み書き | ほぼ必須。プライベートリポジトリへのアクセスに必要です |
| `workflow` | GitHub Actionsワークフローの管理 | CI/CD（自動テスト・デプロイ）を使う場合に必要です |
| `admin:org` | Organization（組織）の管理 | 組織のメンバー管理などを行う場合に必要です |
| `gist` | Gist（コード断片の共有）の作成・編集 | Gistを使う場合のみ |
| `delete_repo` | リポジトリの削除 | 通常は不要です。誤操作防止のため、付与しないことを推奨します |

**最小権限の原則**に従い、必要最低限のスコープだけを選択してください。日常的な開発作業であれば、`repo` と `workflow` の2つで十分です。

「**Generate token**」をクリックすると、トークンが表示されます。**このトークンは一度しか表示されません**。画面を閉じるとニ度と確認できなくなるため、必ずコピーしてパスワードマネージャーなどの安全な場所に保存してください。

### PATを使ったリポジトリ操作

```bash
# HTTPS URLでクローン
git clone https://github.com/username/repo.git
```

ユーザー名とパスワードを聞かれたら、パスワードの代わりにPATを入力します。

### 認証情報の保存（毎回入力しなくて済むように）

HTTPS接続では、操作のたびにユーザー名とトークンの入力を求められることがあります。これを省略するために、OSの認証情報管理機能を活用しましょう。

```bash
# macOSの場合：Keychainに保存
git config --global credential.helper osxkeychain

# Windowsの場合：Windows Credential Managerに保存
git config --global credential.helper wincred

# Linuxの場合：一定時間メモリに保存（秒数で指定、以下は1時間）
git config --global credential.helper 'cache --timeout=3600'
```

macOSの `osxkeychain` と Windowsの `wincred` は、OS内蔵のパスワード管理機能に認証情報を安全に保存します。一度入力すれば、以降は自動的に認証が行われます。

Linuxの `cache` は、メモリ上に一時的に保存する方式で、指定した秒数が経過すると認証情報は消えます。永続的に保存したい場合は `store` ヘルパーもありますが、トークンが平文（暗号化なし）でファイルに保存されるため、セキュリティ上のリスクがあります。可能であれば、`libsecret` や `pass` などの暗号化された認証情報ストアの利用を検討してください。

### Fine-grained PAT（きめ細かいPAT）

GitHubは、従来のPAT（Classic）に加えて、**Fine-grained PAT**（きめ細かいPAT）という新しい方式も提供しています。

Fine-grained PATでは、以下のようなより詳細な権限制御が可能です。

- **リポジトリ単位**で権限を設定できる（特定のリポジトリだけにアクセスを限定）
- **読み取りのみ**・**読み書き**などの粒度で権限を設定できる
- 組織のセキュリティポリシーに準拠したトークンを作成できる

作成は **Developer settings → Personal access tokens → Fine-grained tokens** から行います。より安全なトークン管理が可能なため、新規にトークンを作成する場合はFine-grained PATの使用を検討してみてください。

---

## 4.6　GitHub CLI

GitHub CLI（コマンド名：`gh`）は、GitHubが公式に提供するコマンドラインツールです。認証の設定をはじめ、リポジトリの作成、プルリクエストの操作、Issueの管理など、GitHub上のほぼすべての操作をターミナルから行えます。

認証に関して言えば、GitHub CLI は最も簡単な方法です。対話形式で質問に答えていくだけで、SSH鍵の生成からGitHubへの登録までを自動的に行ってくれます。

### インストール

```bash
# macOS（Homebrew）
brew install gh

# Windows（winget）
winget install --id GitHub.cli

# Linux（Debian/Ubuntu）
sudo apt install gh

# Linux（Fedora）
sudo dnf install gh
```

### 認証の設定

インストールが完了したら、次のコマンドで認証を開始します。

```bash
gh auth login
```

対話形式でいくつかの質問が表示されます。

```
? What account do you want to log into?  GitHub.com
? What is your preferred protocol for Git operations?  SSH
? Generate a new SSH key to add to your GitHub account?  Yes
? Title for your SSH key:  MacBook Pro
? How would you like to authenticate GitHub CLI?  Login with a web browser
```

各質問の意味を解説します。

- **アカウントの種類**：`GitHub.com`（通常のGitHub）か `GitHub Enterprise Server`（企業向け自社ホスト版）かを選びます。ほとんどの場合は `GitHub.com` です。
- **Git操作のプロトコル**：`SSH` を選択することをおすすめします。この選択により、GitHub CLI がSSH鍵の設定も併せて行ってくれます。
- **SSH鍵の生成**：まだSSH鍵を作成していなければ `Yes` を選びます。すでに4.4節の手順で鍵を作成済みの場合は、既存の鍵を使うことも可能です。
- **SSH鍵のタイトル**：GitHubに登録する際の識別名です。どのパソコンの鍵かがわかる名前を付けましょう。
- **認証方法**：`Login with a web browser` を選ぶと、ブラウザが自動的に開き、GitHubのログインページが表示されます。ターミナルに表示されるコードをブラウザに入力して認証を完了してください。

<!-- screenshot: gh auth login の対話画面 -->

ブラウザでの認証が完了すると、ターミナルに認証成功のメッセージが表示されます。これで設定は完了です。

### 認証状態の確認

現在の認証状態を確認するには、次のコマンドを使います。

```bash
gh auth status
```

出力例：

```
github.com
  ✓ Logged in to github.com account username (keyring)
  - Active account: true
  - Git operations protocol: ssh
  - Token: gho_****
  - Token scopes: 'admin:org', 'gist', 'repo', 'workflow'
```

この出力から、ログインしているアカウント、Git操作で使われるプロトコル、トークンのスコープなどを確認できます。もし認証に問題がある場合は、`gh auth login` を再度実行して設定をやり直すことができます。

---

## 4.7　GPG署名 — コミットの本人証明

### なぜ署名が必要なのか

第2章で `user.name` と `user.email` を設定しましたが、実はこの情報は**誰でも自由に設定できます**。極端な話、他人のユーザー名とメールアドレスを設定してコミットすることも技術的には可能です。つまり、コミットの「著者情報」だけでは、そのコミットが本当にその人によるものかどうかを保証できないのです。

GPG署名は、この問題を解決します。GPG（GNU Privacy Guard）という暗号ツールを使ってコミットに電子署名を付与することで、「このコミットは確かに私が作成したものです」という暗号的な証明を提供します。

GPG署名されたコミットは、GitHub上で「**Verified**」（検証済み）という緑色のバッジが表示されます。このバッジがあるコミットは、GitHubに登録されたGPG公開鍵と照合され、本人によるものであることが確認済みです。

<!-- screenshot: Verifiedバッジ付きコミット -->

オープンソースプロジェクトやセキュリティが重視される環境では、GPG署名が求められることがあります。必須ではありませんが、設定しておくとコミットの信頼性が高まります。

### GPG鍵の生成

まず、GPGをインストールします。

```bash
# macOS（Homebrew）
brew install gnupg

# Linux（Ubuntu/Debian）
sudo apt install gnupg

# Windows：Git for Windows に同梱されている場合があります
```

次に、GPG鍵を生成します。

```bash
gpg --full-generate-key
```

いくつかの質問が表示されます。

- **鍵の種類**：`RSA and RSA`（デフォルト）を選択します
- **鍵のビット数**：`4096` を入力します。2048ビットでも十分ですが、4096ビットにしておくとより長期間安全です
- **有効期限**：`0`（無期限）でも構いませんが、セキュリティを重視するなら1〜2年に設定し、期限が来たら更新することも検討してください
- **名前**：GitHubの表示名と一致させてください
- **メールアドレス**：GitHubに登録したメールアドレス（またはnoreplyアドレス）を入力してください
- **パスフレーズ**：GPG鍵を保護するパスフレーズを設定します

### GitHubにGPG鍵を登録する

まず、生成した鍵のIDを確認します。

```bash
gpg --list-secret-keys --keyid-format=long
```

出力例：

```
/Users/you/.gnupg/pubring.kbx
------------------------------
sec   rsa4096/3AA5C34371567BD2 2024-01-01 [SC]
      A1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q7R8S9T0
uid                 [ultimate] Your Name <your-email@example.com>
ssb   rsa4096/1234567890ABCDEF 2024-01-01 [E]
```

`sec` 行の `rsa4096/` の後に続く `3AA5C34371567BD2` が鍵IDです。

次に、公開鍵をテキスト形式でエクスポートします。

```bash
gpg --armor --export 3AA5C34371567BD2
```

`-----BEGIN PGP PUBLIC KEY BLOCK-----` から `-----END PGP PUBLIC KEY BLOCK-----` までの全文をコピーし、GitHubに登録します。

1. GitHub → Settings → **SSH and GPG keys** を開きます
2. 「**New GPG key**」ボタンをクリックします
3. コピーした公開鍵の全文を貼り付けます
4. 「**Add GPG key**」をクリックします

### Gitで署名を有効化する

最後に、Gitがコミット時に自動的にGPG署名を付与するように設定します。

```bash
# 使用するGPG鍵のIDを指定
git config --global user.signingkey 3AA5C34371567BD2

# すべてのコミットを自動的に署名する
git config --global commit.gpgsign true

# GPGプログラムのパスを指定（macOSで必要な場合）
git config --global gpg.program gpg
```

`commit.gpgsign true` を設定すると、以降のすべてのコミットに自動的にGPG署名が付与されます。手動で署名したい場合は、この設定を省略し、コミット時に `-S` オプションを付けてください（`git commit -S -m "メッセージ"`）。

macOSでGPG署名が動作しない場合は、以下の設定が必要なことがあります。

```bash
echo 'export GPG_TTY=$(tty)' >> ~/.zshrc
source ~/.zshrc
```

これは、GPGがパスフレーズの入力を受け付けるために、現在のターミナルの情報を必要とするためです。

---

## 4.8　複数アカウントの管理

仕事用と個人用など、複数のGitHubアカウントを持っている場合、それぞれのアカウントに対して異なるSSH鍵を使い分ける必要があります。一つのSSH公開鍵を複数のGitHubアカウントに登録することはできないためです。

### SSH configによるアカウントの使い分け

SSH設定ファイル（`~/.ssh/config`）を編集して、接続先ごとに異なる鍵を使うように設定します。

まず、アカウントごとにSSH鍵を生成します。

```bash
# 個人アカウント用の鍵
ssh-keygen -t ed25519 -C "personal@example.com" -f ~/.ssh/id_ed25519_personal

# 仕事アカウント用の鍵
ssh-keygen -t ed25519 -C "work@company.com" -f ~/.ssh/id_ed25519_work
```

`-f` オプションでファイル名を指定することで、デフォルトの `id_ed25519` とは異なる名前で鍵を保存できます。

次に、`~/.ssh/config` ファイルを編集します。

```
# 個人アカウント
Host github.com-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_personal

# 仕事アカウント
Host github.com-work
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_work
```

ここでのポイントは、`Host` の値です。実際のホスト名は `github.com` ですが、`github.com-personal` や `github.com-work` という**エイリアス（別名）**を設定しています。`HostName github.com` により、どちらのエイリアスでも実際には `github.com` に接続されますが、使用する鍵が異なります。

それぞれの公開鍵を、対応するGitHubアカウントに登録してください。

### 使い方

リポジトリの操作時は、目的のアカウントに対応するエイリアスを使います。

```bash
# 個人アカウントのリポジトリをクローン
git clone git@github.com-personal:personal-user/my-project.git

# 仕事アカウントのリポジトリをクローン
git clone git@github.com-work:work-user/company-project.git
```

URLの `github.com` の部分が、`github.com-personal` や `github.com-work` に置き換わっている点に注目してください。SSHはこのエイリアスを見て、どの鍵を使うかを自動的に判断します。

### リポジトリごとのユーザー情報の切り替え

SSH鍵の使い分けに加えて、コミットに記録されるユーザー名とメールアドレスもアカウントごとに切り替える必要があります。

```bash
# 仕事用のリポジトリに移動
cd /path/to/work/project

# このリポジトリだけで使うユーザー情報を設定（--localがデフォルト）
git config user.name "Tsubasa (Work)"
git config user.email "tsubasa@company.com"
```

第2章で解説した `--global` と `--local` の仕組みがここで活きてきます。`--global` で個人アカウントの情報を設定しておき、仕事用のリポジトリでは `--local` で上書きするという運用が一般的です。

設定を忘れて個人のメールアドレスで仕事のコミットをしてしまうミスを防ぐために、Gitの `includeIf` 機能を使う方法もあります。`~/.gitconfig` に以下のように記述すると、特定のディレクトリ以下のリポジトリに対して自動的に設定を切り替えられます。

```ini
[includeIf "gitdir:~/work/"]
    path = ~/.gitconfig-work
```

`~/.gitconfig-work` ファイルに仕事用の設定を書いておけば、`~/work/` ディレクトリ以下のリポジトリでは自動的にその設定が適用されます。

```ini
# ~/.gitconfig-work の内容
[user]
    name = Tsubasa (Work)
    email = tsubasa@company.com
```

この方法なら、リポジトリごとに毎回設定する手間が省け、設定忘れのリスクも軽減されます。

---

## 4.9　まとめ

本章では、パソコンとGitHubを安全に接続するための認証方法を学びました。振り返ってみましょう。

- **認証の必要性**：パスワード認証は廃止されており、より安全な方法でGitHubに接続する必要があります。
- **3つの接続方式**：SSH鍵、HTTPS + PAT、GitHub CLI の3つの方式があり、それぞれに適した場面があります。
- **SSH鍵**：公開鍵暗号の仕組みを利用した認証方式で、秘密鍵は自分のPCに、公開鍵はGitHubに登録します。一度設定すれば、以降の認証は自動的に行われます。
- **Personal Access Token（PAT）**：HTTPS接続で使用するトークンで、有効期限や権限の範囲を細かく設定できます。Fine-grained PATではリポジトリ単位の権限制御も可能です。
- **GitHub CLI**：`gh auth login` コマンドで対話的に認証を設定できる、最も手軽な方法です。
- **GPG署名**：コミットに電子署名を付与し、本人が作成したものであることを暗号的に証明します。GitHub上で「Verified」バッジとして表示されます。
- **複数アカウントの管理**：SSH configのエイリアス機能と `--local` 設定、`includeIf` を組み合わせることで、複数のGitHubアカウントをスムーズに使い分けられます。

認証の設定は、最初の一回だけ乗り越えれば、あとは快適にGitHubを使い続けることができます。もし途中でエラーが出たり、うまくいかなかったりした場合は、第24章のトラブルシューティングも参照してください。

次の章では、いよいよGitHub上にリポジトリを作成し、コードを管理するための「器」を用意します。

---

→ 次の章：[第5章　リポジトリの作成と管理](05-repository.md)
