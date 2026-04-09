#!/usr/bin/env python3
"""Replace \screenshot{...} placeholders with \includegraphics in LaTeX files."""

import re
import os
import glob

# Mapping from screenshot description keywords to image filenames
SCREENSHOT_MAP = {
    # Ch02 - Setup
    "xcode-select": "xcode-install",
    "Git for Windows": "git-for-windows",
    "git --version": "git-version",
    "Email設定": "email-settings",
    "noreply": "email-settings",
    "VS Code公式": "vscode-extensions",
    "VS Codeのダウンロード": "vscode-extensions",

    # Ch03 - Account
    "Sign up": "signup",
    "サインアップ": "signup",
    "メール認証": "email-verify",
    "2FA": "2fa-setup",
    "二段階認証": "2fa-setup",
    "プロフィール設定": "profile-settings",
    "プロフィールREADME": "profile-readme",
    "Achievements": "achievements",
    "コントリビューショングラフ": "contribution-graph",
    "通知設定": "notifications-settings",

    # Ch04 - Authentication
    "SSH鍵の追加": "ssh-key-add",
    "PAT作成": "pat-create",
    "gh auth login": "gh-auth-login",
    "Verified": "verified-commit",

    # Ch05 - Repository
    "+ボタン": "repo-create",
    "リポジトリ作成画面": "repo-create",
    "Codeボタン": "clone-url",
    "クローンURL": "clone-url",
    "Settings": "repo-settings",

    # Ch06 - Basic Workflow
    "ソース管理パネルと差分": "vscode-git",

    # Ch07 - Branches
    # (mostly diagrams, no screenshots)

    # Ch08 - Conflicts
    "コンフリクト解決UI": "vscode-conflict",
    "コンフリクトマーカー": "vscode-conflict",

    # Ch09 - History
    # (mostly terminal commands)

    # Ch10 - Pull Requests
    "PR作成画面": "pr-create",
    "Files changed": "pr-files-changed",
    "レビュー送信": "pr-review",
    "Review changes": "pr-review",
    "ドラフトPR": "pr-draft",
    "Draft": "pr-draft",

    # Ch11 - Issues
    "Issue作成画面": "issue-create",
    "ラベル管理": "issue-labels",
    "マイルストーン": "issue-milestone",
    "Issueテンプレート": "issue-template-select",
    "ピン留め": "issue-pinned",
    "good first issue": "good-first-issue",

    # Ch12 - GitHub Actions
    "Actions.*実行結果": "actions-results",
    "Actionsタブ": "actions-results",
    "workflow.*dispatch": "actions-workflow-dispatch",
    "手動実行": "actions-workflow-dispatch",
    "Secrets設定": "secrets-settings",
    "シークレット": "secrets-settings",

    # Ch13 - GitHub Pages
    "Pages設定": "pages-settings",
    "Deploy from": "pages-settings",
    "Jekyll.*テーマ": "jekyll-themes",
    "Custom domain": "pages-custom-domain",
    "カスタムドメイン": "pages-custom-domain",

    # Ch14 - Releases
    "リリース作成": "release-create",

    # Ch15 - Fork
    "Forkボタン": "fork-button",
    "ForkからPR": "fork-pr",
    "Fork.*PR": "fork-pr",

    # Ch16 - Organizations
    "Organization作成": "org-create",
    "チーム作成": "org-team",
    "メンバー招待": "org-members",

    # Ch17 - Code Review
    "ブランチ保護": "branch-protection",
    "suggestion": "code-review-suggestion",

    # Ch18 - Projects
    "Board": "projects-board",
    "カンバン": "projects-board",
    "Table": "projects-table",
    "スプレッドシート": "projects-table",
    "Roadmap": "projects-roadmap",
    "タイムライン": "projects-roadmap",
    "カスタムフィールド": "projects-table",
    "ワークフロー設定": "projects-board",

    # Ch19 - Files
    "blob.*tree": "file-blob",
    "blame": "file-blame",
    "Blame": "file-blame",
    "行番号.*ハイライト": "line-highlight",
    "github.dev": "github-dev",
    "ドラッグ.*ドロップ": "file-create",
    "ファイル作成": "file-create",

    # Ch20 - README
    "READMEが表示": "readme-display",
    "リポジトリトップ": "readme-display",
    "折りたたみ": "collapsible",
    "ライセンス選択": "license-select",
    "Wiki有効化": "wiki-settings",

    # Ch21 - Customization
    "テーマ設定": "theme-settings",
    "Appearance": "theme-settings",
    "ショートカット一覧": "shortcuts",

    # Ch22 - Security
    "Dependabot": "dependabot-settings",
    "Code security": "dependabot-settings",

    # Ch23 - Integrations
    "ソース管理パネル全体": "vscode-git",
    "Claude Code": "vscode-claude",
    "拡張機能": "vscode-extensions",
    "インストール済みアプリ": "marketplace",
    "Marketplace": "marketplace",
    "Webhook": "webhook-settings",

    # Ch24 - Troubleshooting
    # (mostly terminal outputs)

    # Ch25 - File Extensions
    "シンタックスハイライト": "syntax-highlight",
    "Python.*ハイライト": "syntax-highlight",
    "言語バー": "language-bar",
    "ファイルファインダー": "file-finder",

    # Ch26 - GitHub Apps
    "GitHub Desktop.*メイン": "github-desktop",
    "Desktopのメイン": "github-desktop",
    "GitHub Mobile": "github-mobile",
    "VS Code.*ソース管理": "vscode-git",
}

def find_best_image(description, images_dir):
    """Find the best matching image for a screenshot description."""
    description_lower = description.lower()

    for keyword, filename in SCREENSHOT_MAP.items():
        try:
            match = re.search(keyword, description, re.IGNORECASE)
        except re.PatternError:
            match = keyword.lower() in description_lower
        if match:
            img_path = os.path.join(images_dir, f"{filename}.png")
            if os.path.exists(img_path):
                return filename
    return None

def replace_screenshots_in_file(tex_file, images_dir):
    """Replace \screenshot{...} with \includegraphics in a tex file."""
    with open(tex_file, 'r') as f:
        content = f.read()

    def replace_match(match):
        desc = match.group(1)
        img_name = find_best_image(desc, images_dir)
        if img_name:
            return (
                f"\\begin{{figure}}[htbp]\n"
                f"\\centering\n"
                f"\\includegraphics[width=0.95\\textwidth]{{images/{img_name}.png}}\n"
                f"\\caption{{{desc}}}\n"
                f"\\end{{figure}}"
            )
        else:
            # Keep placeholder if no matching image
            return match.group(0)

    new_content = re.sub(r'\\screenshot\{([^}]*)\}', replace_match, content)

    if new_content != content:
        with open(tex_file, 'w') as f:
            f.write(new_content)
        replacements = content.count('\\screenshot{') - new_content.count('\\screenshot{')
        remaining = new_content.count('\\screenshot{')
        print(f"  {os.path.basename(tex_file)}: {replacements} replaced, {remaining} remaining")
        return replacements
    return 0

def main():
    chapters_dir = os.path.join(os.path.dirname(__file__), 'chapters')
    images_dir = os.path.join(os.path.dirname(__file__), 'images')

    total = 0
    for tex_file in sorted(glob.glob(os.path.join(chapters_dir, '*.tex'))):
        count = replace_screenshots_in_file(tex_file, images_dir)
        total += count

    print(f"\nTotal: {total} screenshots replaced")

if __name__ == '__main__':
    main()
