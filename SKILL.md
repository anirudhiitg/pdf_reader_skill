---
name: pdf-interactive
description: Parse PDF documents, summarize and clean content using AI, and generate interactive HTML for easy consumption. Supports automatic content extraction, intelligent summarization, table of contents generation, search functionality, and responsive design. Perfect for transforming dense PDFs into readable, navigable web pages.
---

# PDF Interactive Skill

Transform PDF documents into beautiful, interactive HTML pages with AI-powered summarization and content cleaning.

## What This Skill Does

1. **Extracts PDF Content** - Reads and parses PDF files, preserving structure and formatting
2. **AI Summarization** - Uses Claude to summarize sections, clean up text, and extract key insights
3. **Interactive HTML Generation** - Creates a responsive, searchable HTML page with:
   - Automatic table of contents
   - Collapsible sections
   - Search functionality
   - Dark/light mode toggle
   - Copy-to-clipboard for code blocks
   - Smooth navigation
   - Mobile-responsive design

## When to Use This Skill

Use `/pdf-interactive` when you need to:
- Convert research papers into readable web pages
- Make technical documentation more accessible
- Create summaries of long PDF reports
- Extract and organize information from contracts or legal documents
- Transform educational materials into interactive study guides
- Share PDF content in a more user-friendly format

## How It Works

The skill follows this workflow:

1. **PDF Extraction**: Reads the PDF file and extracts text, preserving headings and structure
2. **Content Analysis**: AI analyzes the content to identify sections, key points, and structure
3. **Summarization**: Each section is summarized and cleaned up for clarity
4. **HTML Generation**: Creates an interactive HTML page with:
   - Navigation sidebar with table of contents
   - Formatted content with proper headings
   - Search box to find content quickly
   - Dark mode support
   - Print-friendly styling

## Usage

Simply provide a PDF file path:

```
/pdf-interactive path/to/document.pdf
```

Or with options:

```
/pdf-interactive path/to/document.pdf --output custom-name.html --summary-level detailed
```

### Options

- `--output <filename>` - Specify output HTML filename (default: same as PDF name)
- `--summary-level <brief|balanced|detailed>` - Control summarization depth (default: balanced)
- `--skip-summary` - Skip AI summarization, just convert PDF to HTML
- `--dark-mode` - Default to dark mode in the output
- `--no-search` - Disable search functionality
- `--title <title>` - Custom title for the HTML page

## Examples

### Basic Usage

```
/pdf-interactive research-paper.pdf
```

Creates `research-paper.html` with balanced summarization.

### Detailed Summary

```
/pdf-interactive report.pdf --summary-level detailed
```

Creates detailed summaries of each section.

### Quick Conversion

```
/pdf-interactive document.pdf --skip-summary
```

Converts to HTML without AI processing (faster).

### Custom Output

```
/pdf-interactive contract.pdf --output legal-review.html --title "Contract Review 2026"
```

Creates custom-named output with custom title.

## Output Features

The generated HTML includes:

### Navigation
- Sticky sidebar with hierarchical table of contents
- Click to jump to any section
- Auto-highlighting of current section

### Content Features
- Clean, readable typography
- Proper heading hierarchy
- Formatted lists and tables
- Code blocks with syntax highlighting
- Blockquotes for important callouts

### Interactive Elements
- **Search**: Real-time search across all content
- **Dark Mode**: Toggle between light and dark themes
- **Copy Buttons**: Easy copying of code snippets
- **Expand/Collapse**: Collapsible sections for long documents
- **Print Support**: Clean printing without navigation elements

### Responsive Design
- Mobile-friendly layout
- Adjusts to any screen size
- Touch-friendly navigation on tablets

## Technical Implementation

The skill uses:
- **PDF Parsing**: Python's `PyPDF2` or `pdfplumber` for text extraction
- **AI Processing**: Claude API for summarization and content analysis
- **HTML/CSS/JS**: Modern web technologies for interactivity
- **Template Engine**: Jinja2 for flexible HTML generation

## Installation

See the main [README.md](README.md) for installation instructions.

## Tips for Best Results

1. **Choose the right summary level**:
   - `brief` - Quick overview, key points only (fastest)
   - `balanced` - Good detail while staying concise (recommended)
   - `detailed` - Comprehensive summaries (slowest, most thorough)

2. **For large PDFs**: Consider using `--skip-summary` first to preview the structure, then run with summarization if needed

3. **For technical docs**: The skill automatically detects and preserves code blocks, formulas, and technical notation

4. **For presentations**: PDFs from slides work well; each slide becomes a section

5. **For scanned PDFs**: This skill requires text-based PDFs. For scanned documents, use OCR preprocessing first.

## Limitations

- Requires text-based PDFs (not scanned images without OCR)
- Complex layouts may need manual adjustment
- Very large PDFs (>500 pages) may take several minutes to process
- Tables are converted to HTML tables but complex formatting may be simplified
- Images are not currently extracted (text only)

## Future Enhancements

Planned features:
- Image extraction and embedding
- Math formula rendering (LaTeX support)
- Export to other formats (Markdown, DOCX)
- Batch processing multiple PDFs
- Custom CSS themes
- Annotation support

## Troubleshooting

**PDF won't parse**: Ensure it's a text-based PDF. Try opening in a PDF reader to verify text is selectable.

**Slow processing**: Large PDFs take time. Use `--skip-summary` for faster conversion, or use `--summary-level brief`.

**Poor formatting**: Some PDF layouts are complex. The output is best-effort; you may need to manually adjust the HTML.

**Missing content**: Check if the PDF has security restrictions. Some PDFs prevent text extraction.

## Contributing

This is an open-source skill! Contributions welcome. See the repository for guidelines.

## License

MIT License - see LICENSE file for details.
