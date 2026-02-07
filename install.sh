#!/bin/bash
# Installation script for PDF Interactive Skill

set -e

echo "📦 Installing PDF Interactive Skill for Claude Code"
echo ""

# Check if Claude Code is installed
if ! command -v claude &> /dev/null; then
    echo "⚠️  Claude Code CLI not found. Please install it first:"
    echo "   Visit: https://www.anthropic.com/claude/code"
    exit 1
fi

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1-2)
echo "✓ Found Python $PYTHON_VERSION"

# Install Python dependencies
echo ""
echo "📥 Installing Python dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✓ Dependencies installed"

# Create skills directory if it doesn't exist
SKILLS_DIR="$HOME/.claude/skills"
mkdir -p "$SKILLS_DIR"

# Get the current directory
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Create symlink
SKILL_LINK="$SKILLS_DIR/pdf-interactive"

if [ -e "$SKILL_LINK" ]; then
    echo ""
    echo "⚠️  Skill already exists at: $SKILL_LINK"
    read -p "   Replace it? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf "$SKILL_LINK"
    else
        echo "Installation cancelled."
        exit 0
    fi
fi

echo ""
echo "🔗 Creating symlink..."
ln -s "$CURRENT_DIR" "$SKILL_LINK"

if [ $? -ne 0 ]; then
    echo "❌ Failed to create symlink. Trying copy instead..."
    cp -r "$CURRENT_DIR" "$SKILL_LINK"
    if [ $? -ne 0 ]; then
        echo "❌ Installation failed"
        exit 1
    fi
fi

echo "✓ Skill installed at: $SKILL_LINK"

# Check for ANTHROPIC_API_KEY
echo ""
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  ANTHROPIC_API_KEY environment variable not set"
    echo ""
    echo "   To use AI summarization features, set your API key:"
    echo "   export ANTHROPIC_API_KEY=your-api-key"
    echo ""
    echo "   Or add it to your shell profile (~/.bashrc or ~/.zshrc):"
    echo "   echo 'export ANTHROPIC_API_KEY=your-api-key' >> ~/.bashrc"
    echo ""
    echo "   You can still use the skill with --skip-summary flag"
else
    echo "✓ ANTHROPIC_API_KEY is set"
fi

echo ""
echo "✨ Installation complete!"
echo ""
echo "Usage:"
echo "  claude"
echo "  /pdf-interactive document.pdf"
echo ""
echo "Or run directly:"
echo "  python3 $CURRENT_DIR/scripts/main.py document.pdf"
echo ""
echo "For help:"
echo "  /pdf-interactive --help"
echo ""
