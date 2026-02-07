# Publishing to GitHub

This guide walks you through publishing your PDF Interactive Skill to GitHub.

## Prerequisites

- GitHub account ([sign up here](https://github.com/join))
- Git installed (already done ✓)
- Repository is ready in: `/c/Users/anirudhyadav/pdf_reader_skill`

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and log in
2. Click the "+" icon in the top right, select "New repository"
3. Fill in the details:
   - **Repository name**: `pdf_reader_skill`
   - **Description**: "Convert PDFs to interactive HTML with AI summarization - A Claude Code skill"
   - **Visibility**: Public (recommended for sharing)
   - **Do NOT** initialize with README, .gitignore, or license (we already have these)
4. Click "Create repository"

## Step 2: Push to GitHub

After creating the repository, run these commands:

```bash
cd /c/Users/anirudhyadav/pdf_reader_skill

# Add the remote repository (replace 'anirudhiitg' with your GitHub username)
git remote add origin https://github.com/anirudhiitg/pdf_reader_skill.git

# Verify the remote
git remote -v

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Update README with Your Info

1. Edit `README.md` and replace:
   - `anirudhiitg` with your actual GitHub username (appears in URLs)
   - `[Your Name]` in the Author section

2. Edit `LICENSE` and replace:
   - `[Your Name]` with your actual name

3. Commit and push changes:
   ```bash
   git add README.md LICENSE
   git commit -m "Update: add author information"
   git push
   ```

## Step 4: Add Topics and Description

On your GitHub repository page:

1. Click "About" ⚙️ (gear icon) on the right sidebar
2. Add a short description:
   ```
   Transform PDFs into beautiful, interactive HTML with AI summarization. A skill for Claude Code.
   ```
3. Add topics (tags):
   - `claude-code`
   - `pdf-parser`
   - `ai-summarization`
   - `html-generator`
   - `pdf-to-html`
   - `anthropic`
   - `python`
4. Click "Save changes"

## Step 5: Create a Release (Optional but Recommended)

1. Go to the "Releases" section on the right sidebar
2. Click "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `v1.0.0 - Initial Release`
5. Description:
   ```markdown
   ## 🎉 Initial Release

   ### Features
   - PDF parsing with structure detection
   - AI-powered summarization using Claude
   - Interactive HTML generation
   - Search functionality
   - Dark/light mode toggle
   - Mobile-responsive design
   - Cross-platform support (Windows, macOS, Linux)

   ### Installation
   See [README.md](README.md) for installation instructions.

   ### Requirements
   - Python 3.8+
   - Claude Code CLI
   - Anthropic API key (for AI features)
   ```
6. Click "Publish release"

## Step 6: Enable GitHub Pages (Optional)

To showcase an example output:

1. Create a `docs/` folder with an example HTML:
   ```bash
   mkdir docs
   # Add an example HTML file
   git add docs/
   git commit -m "Add: example documentation"
   git push
   ```

2. Go to Settings → Pages
3. Source: Deploy from a branch
4. Branch: `main`, folder: `/docs`
5. Click "Save"

Your example will be available at: `https://anirudhiitg.github.io/pdf_reader_skill/`

## Step 7: Share Your Skill!

### On GitHub
Your repository is now live at:
```
https://github.com/anirudhiitg/pdf_reader_skill
```

### Share on Social Media
Tweet about it:
```
🎉 Just created a Claude Code skill that transforms PDFs into interactive HTML with AI summarization!

✨ Features:
- Smart PDF parsing
- AI-powered summaries
- Search & dark mode
- Mobile-friendly

Check it out: https://github.com/anirudhiitg/pdf_reader_skill

#ClaudeCode #AI #PDF
```

### Submit to Claude Code Skills Directory (if available)
Check if Anthropic has a skills directory and submit your skill!

## Repository Badges (Optional but Cool)

Add these to the top of your README.md:

```markdown
[![GitHub stars](https://img.shields.io/github/stars/anirudhiitg/pdf_reader_skill?style=social)](https://github.com/anirudhiitg/pdf_reader_skill/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/anirudhiitg/pdf_reader_skill?style=social)](https://github.com/anirudhiitg/pdf_reader_skill/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
```

## Maintaining Your Repository

### Accepting Contributions

1. Review pull requests in the "Pull requests" tab
2. Respond to issues in the "Issues" tab
3. Update the README with new features
4. Create new releases for major updates

### Keeping It Updated

```bash
# Make changes
git add .
git commit -m "Update: description of changes"
git push
```

### Creating New Releases

When you add significant features:

1. Update version number
2. Create a new tag: `git tag v1.1.0`
3. Push tag: `git push --tags`
4. Create release on GitHub with changelog

## Troubleshooting

### Can't push to GitHub
- Check remote: `git remote -v`
- Verify credentials: Make sure you're logged in
- Try HTTPS or SSH depending on your setup

### README not showing properly
- Ensure it's named exactly `README.md`
- Check Markdown syntax
- Preview locally with a Markdown viewer

### Want to update after first push
```bash
# Make your changes
git add .
git commit -m "Update: your message"
git push
```

## Next Steps

1. **Star your own repository** to show it on your profile
2. **Share with the community** on Twitter, Reddit, etc.
3. **Add examples** with real PDF outputs
4. **Write a blog post** about creating the skill
5. **Contribute back** to other Claude Code skills

## Questions?

Open an issue on your repository or reach out to the Claude Code community!

---

**Good luck with your skill! 🚀**
