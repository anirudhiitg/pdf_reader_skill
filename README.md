# PDF Interactive Skill for Claude Code

Transform PDF documents into beautiful, interactive HTML pages with AI-powered summarization and content cleaning.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

- **PDF Parsing**: Extracts text and structure from PDF documents
- **AI Summarization**: Uses Claude to intelligently summarize and clean content
- **Interactive HTML**: Generates responsive, searchable web pages with:
  - 📑 Automatic table of contents
  - 🔍 Real-time search functionality
  - 🌓 Dark/light mode toggle
  - 📱 Mobile-responsive design
  - 🖨️ Print-friendly formatting
  - 📋 Copy-to-clipboard for code blocks
  - ⚡ Fast navigation with smooth scrolling

## Demo

<details>
<summary>See example output (click to expand)</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Research Paper - AI Summarized</title>
    <!-- Beautiful, modern styling -->
</head>
<body>
    <!-- Sidebar navigation -->
    <!-- Searchable content -->
    <!-- Interactive features -->
</body>
</html>
```

</details>

## Installation

### Prerequisites

- [Claude Code CLI](https://www.anthropic.com/claude/code) installed
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Python Dependencies

```bash
pip install pdfplumber anthropic jinja2
```

Or using the provided requirements file:

```bash
pip install -r requirements.txt
```

### Step 2: Install the Skill

Clone or download this repository:

```bash
# Clone the repository
git clone https://github.com/yourusername/pdf-interactive-skill.git

# Navigate to the skill directory
cd pdf-interactive-skill
```

### Step 3: Link to Claude Code

Create a symlink in your Claude skills directory:

**On macOS/Linux:**
```bash
ln -s "$(pwd)" ~/.claude/skills/pdf-interactive
```

**On Windows (PowerShell as Administrator):**
```powershell
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\pdf-interactive" -Target (Get-Location)
```

**Or copy the skill manually:**
```bash
# macOS/Linux
cp -r . ~/.claude/skills/pdf-interactive

# Windows
xcopy /E /I . %USERPROFILE%\.claude\skills\pdf-interactive
```

### Step 4: Verify Installation

Restart Claude Code or run:

```bash
claude --reload-skills
```

Test the skill:

```bash
claude
# Then in the Claude session:
/pdf-interactive --help
```

## Quick Start

### Basic Usage

```bash
# Start Claude Code
claude

# Use the skill with a PDF
/pdf-interactive document.pdf
```

This will create `document.html` in the same directory with AI-summarized content.

### With Options

```bash
# Detailed summarization
/pdf-interactive report.pdf --summary-level detailed

# Custom output name
/pdf-interactive paper.pdf --output research-summary.html

# Skip AI processing (faster)
/pdf-interactive doc.pdf --skip-summary

# Custom title
/pdf-interactive contract.pdf --title "Legal Review 2026"
```

## Usage Examples

### Example 1: Research Paper

```bash
/pdf-interactive machine-learning-paper.pdf --summary-level detailed
```

**Result**: An HTML page with:
- Executive summary at the top
- Section-by-section summaries
- Full table of contents
- Search to find specific topics
- Dark mode for reading

### Example 2: Technical Documentation

```bash
/pdf-interactive api-documentation.pdf --output api-guide.html
```

**Result**: Interactive documentation with:
- Navigable sections
- Code blocks with copy buttons
- Searchable content
- Mobile-friendly layout

### Example 3: Legal Document

```bash
/pdf-interactive contract.pdf --summary-level brief --title "Contract Summary"
```

**Result**: Summarized contract with:
- Key points highlighted
- Section navigation
- Clean, professional formatting

### Example 4: Batch Processing

```bash
# Process multiple PDFs
for pdf in *.pdf; do
    /pdf-interactive "$pdf" --summary-level balanced
done
```

## Command Options

| Option | Description | Default |
|--------|-------------|---------|
| `--output <file>` | Output HTML filename | Same as PDF name |
| `--summary-level <level>` | Summarization depth: `brief`, `balanced`, `detailed` | `balanced` |
| `--skip-summary` | Skip AI summarization (faster conversion) | False |
| `--dark-mode` | Default to dark mode | False (light mode) |
| `--no-search` | Disable search functionality | False (search enabled) |
| `--title <title>` | Custom page title | PDF filename |
| `--help` | Show help message | - |

## Output Features

### Generated HTML Includes

1. **Navigation Sidebar**
   - Hierarchical table of contents
   - Clickable section links
   - Current section highlighting
   - Sticky positioning

2. **Content Area**
   - Clean typography
   - Proper heading hierarchy
   - Formatted lists and tables
   - Code blocks with syntax highlighting
   - Blockquotes for emphasis

3. **Interactive Features**
   - Search box with live filtering
   - Dark/light mode toggle
   - Copy buttons for code
   - Smooth scrolling
   - Mobile hamburger menu

4. **Styling**
   - Responsive design (desktop/tablet/mobile)
   - Print-friendly CSS
   - Modern, clean aesthetic
   - Accessible colors and fonts

## How It Works

```mermaid
graph LR
    A[PDF File] --> B[Extract Text]
    B --> C[Parse Structure]
    C --> D[AI Analysis]
    D --> E[Summarize Sections]
    E --> F[Generate HTML]
    F --> G[Interactive Page]
```

1. **PDF Extraction**: Uses `pdfplumber` to extract text while preserving structure
2. **Structure Analysis**: Identifies headings, sections, and content hierarchy
3. **AI Processing**: Claude analyzes and summarizes each section
4. **Template Rendering**: Jinja2 generates HTML from a customizable template
5. **Enhancement**: Adds JavaScript for search, navigation, and interactivity

## Project Structure

```
pdf-interactive-skill/
├── SKILL.md                 # Skill definition for Claude Code
├── README.md                # This file
├── requirements.txt         # Python dependencies
├── LICENSE                  # MIT License
├── templates/
│   └── interactive.html     # HTML template (Jinja2)
├── examples/
│   ├── sample.pdf          # Example PDF
│   └── sample-output.html  # Example output
├── scripts/
│   ├── pdf_parser.py       # PDF extraction logic
│   ├── ai_summarizer.py    # AI summarization
│   └── html_generator.py   # HTML generation
└── .gitignore              # Git ignore file
```

## Customization

### Custom HTML Template

Edit `templates/interactive.html` to customize:
- Colors and fonts
- Layout and spacing
- Additional features
- Branding

### Custom Summarization

Modify `scripts/ai_summarizer.py` to adjust:
- Summary length
- Focus areas
- Tone and style
- Language

### Custom Styling

Add your own CSS in the template:

```html
<style>
    :root {
        --primary-color: #your-color;
        --font-family: 'Your-Font', sans-serif;
    }
</style>
```

## Troubleshooting

### Issue: "Module not found" error

**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: PDF won't parse

**Solution**:
- Ensure it's a text-based PDF (not scanned image)
- Try opening in a PDF reader to verify text is selectable
- Check if PDF has security restrictions

### Issue: Slow processing

**Solution**:
- Use `--summary-level brief` for faster processing
- Use `--skip-summary` to skip AI processing
- Process smaller sections at a time

### Issue: Poor HTML formatting

**Solution**:
- PDFs with complex layouts may not convert perfectly
- Edit the output HTML manually if needed
- Adjust the template for better formatting

### Issue: Missing content

**Solution**:
- Check PDF for copy protection
- Verify PDF is not corrupted
- Try a different PDF library (pypdf2 vs pdfplumber)

## Requirements

### Python Packages

```txt
pdfplumber>=0.10.0
anthropic>=0.18.0
jinja2>=3.1.0
```

### System Requirements

- Python 3.8+
- 512MB RAM minimum
- Internet connection (for AI features)

## Performance

| PDF Size | Pages | Processing Time (with AI) | Processing Time (no AI) |
|----------|-------|---------------------------|------------------------|
| Small    | 1-10  | 30-60 seconds            | 5-10 seconds          |
| Medium   | 11-50 | 2-5 minutes              | 15-30 seconds         |
| Large    | 51-200| 5-15 minutes             | 30-60 seconds         |
| Very Large| 200+ | 15+ minutes              | 1-2 minutes           |

*Times vary based on content complexity and summary level*

## Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/pdf-interactive-skill.git

# Install in development mode
cd pdf-interactive-skill
pip install -e .

# Run tests
python -m pytest tests/
```

## Roadmap

- [ ] Image extraction and embedding
- [ ] Math formula rendering (LaTeX)
- [ ] Export to Markdown/DOCX
- [ ] Batch processing UI
- [ ] Custom theme builder
- [ ] Annotation support
- [ ] Cloud storage integration
- [ ] Real-time collaboration
- [ ] Version comparison

## FAQ

**Q: Can this handle scanned PDFs?**
A: No, this requires text-based PDFs. For scanned documents, use OCR software first (like Adobe Acrobat or Tesseract).

**Q: Does it extract images?**
A: Currently text-only. Image extraction is planned for a future release.

**Q: Can I use this without AI summarization?**
A: Yes! Use the `--skip-summary` flag for direct PDF-to-HTML conversion.

**Q: Is my data sent to the cloud?**
A: Only if using AI summarization (via Anthropic API). Use `--skip-summary` for fully local processing.

**Q: Can I customize the HTML output?**
A: Yes! Edit the template file or add your own CSS/JS.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built for [Claude Code](https://www.anthropic.com/claude/code)
- Powered by [Anthropic's Claude API](https://www.anthropic.com/)
- PDF parsing by [pdfplumber](https://github.com/jsvine/pdfplumber)
- Templating by [Jinja2](https://jinja.palletsprojects.com/)

## Support

- 🐛 [Report a bug](https://github.com/yourusername/pdf-interactive-skill/issues)
- 💡 [Request a feature](https://github.com/yourusername/pdf-interactive-skill/issues)
- 📖 [Read the docs](https://github.com/yourusername/pdf-interactive-skill/wiki)
- 💬 [Join discussions](https://github.com/yourusername/pdf-interactive-skill/discussions)

## Author

Created by [Your Name](https://github.com/yourusername)

---

**Star this repo if you find it useful!** ⭐
