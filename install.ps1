# Installation script for PDF Interactive Skill (Windows PowerShell)

Write-Host "📦 Installing PDF Interactive Skill for Claude Code" -ForegroundColor Cyan
Write-Host ""

# Check if Claude Code is installed
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
    Write-Host "⚠️  Claude Code CLI not found. Please install it first:" -ForegroundColor Yellow
    Write-Host "   Visit: https://www.anthropic.com/claude/code"
    exit 1
}

# Check Python version
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Python not found. Please install Python 3.8 or higher." -ForegroundColor Red
    exit 1
}

$pythonVersion = python --version
Write-Host "✓ Found $pythonVersion" -ForegroundColor Green

# Install Python dependencies
Write-Host ""
Write-Host "📥 Installing Python dependencies..." -ForegroundColor Cyan
pip install -r requirements.txt

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to install dependencies" -ForegroundColor Red
    exit 1
}

Write-Host "✓ Dependencies installed" -ForegroundColor Green

# Create skills directory if it doesn't exist
$skillsDir = "$env:USERPROFILE\.claude\skills"
if (-not (Test-Path $skillsDir)) {
    New-Item -ItemType Directory -Path $skillsDir -Force | Out-Null
}

# Get the current directory
$currentDir = $PSScriptRoot

# Create symlink or copy
$skillLink = "$skillsDir\pdf-interactive"

if (Test-Path $skillLink) {
    Write-Host ""
    Write-Host "⚠️  Skill already exists at: $skillLink" -ForegroundColor Yellow
    $response = Read-Host "   Replace it? (y/n)"
    if ($response -ne "y") {
        Write-Host "Installation cancelled."
        exit 0
    }
    Remove-Item -Path $skillLink -Recurse -Force
}

Write-Host ""
Write-Host "🔗 Creating link..." -ForegroundColor Cyan

# Try to create symlink (requires admin privileges)
try {
    New-Item -ItemType SymbolicLink -Path $skillLink -Target $currentDir -ErrorAction Stop | Out-Null
    Write-Host "✓ Skill installed as symlink at: $skillLink" -ForegroundColor Green
}
catch {
    Write-Host "⚠️  Could not create symlink (requires admin). Copying files instead..." -ForegroundColor Yellow
    Copy-Item -Path $currentDir -Destination $skillLink -Recurse -Force
    if ($LASTEXITCODE -eq 0 -or $?) {
        Write-Host "✓ Skill installed (copied) at: $skillLink" -ForegroundColor Green
    }
    else {
        Write-Host "❌ Installation failed" -ForegroundColor Red
        exit 1
    }
}

# Check for ANTHROPIC_API_KEY
Write-Host ""
if (-not $env:ANTHROPIC_API_KEY) {
    Write-Host "⚠️  ANTHROPIC_API_KEY environment variable not set" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "   To use AI summarization features, set your API key:" -ForegroundColor White
    Write-Host "   `$env:ANTHROPIC_API_KEY = 'your-api-key'" -ForegroundColor Gray
    Write-Host ""
    Write-Host "   Or set it permanently (run PowerShell as Administrator):" -ForegroundColor White
    Write-Host "   [System.Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY', 'your-api-key', 'User')" -ForegroundColor Gray
    Write-Host ""
    Write-Host "   You can still use the skill with --skip-summary flag" -ForegroundColor White
}
else {
    Write-Host "✓ ANTHROPIC_API_KEY is set" -ForegroundColor Green
}

Write-Host ""
Write-Host "✨ Installation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Usage:" -ForegroundColor Cyan
Write-Host "  claude"
Write-Host "  /pdf-interactive document.pdf"
Write-Host ""
Write-Host "Or run directly:" -ForegroundColor Cyan
Write-Host "  python $currentDir\scripts\main.py document.pdf"
Write-Host ""
Write-Host "For help:" -ForegroundColor Cyan
Write-Host "  /pdf-interactive --help"
Write-Host ""
