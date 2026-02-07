# Contributing to PDF Interactive Skill

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/yourusername/pdf-interactive-skill/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - PDF characteristics (if relevant)
   - Your environment (OS, Python version, etc.)

### Suggesting Enhancements

1. Check [existing issues](https://github.com/yourusername/pdf-interactive-skill/issues) for similar suggestions
2. Create a new issue with:
   - Clear description of the enhancement
   - Use cases and benefits
   - Possible implementation approach

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/yourusername/pdf-interactive-skill.git
   cd pdf-interactive-skill
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the code style (see below)
   - Add tests if applicable
   - Update documentation

4. **Test your changes**
   ```bash
   python scripts/main.py examples/sample.pdf
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: brief description of changes"
   ```

6. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a Pull Request on GitHub

## Code Style

### Python

- Follow [PEP 8](https://pep8.org/)
- Use type hints where possible
- Add docstrings to functions and classes
- Keep functions focused and small

Example:
```python
def parse_section(content: str, level: int) -> Dict[str, Any]:
    """
    Parse a section of content

    Args:
        content: Raw section text
        level: Heading level (1-3)

    Returns:
        Dictionary with parsed section data
    """
    # Implementation
    pass
```

### HTML/CSS/JavaScript

- Use semantic HTML5
- Follow modern CSS practices (CSS Grid, Flexbox)
- Vanilla JavaScript (no jQuery)
- Mobile-first responsive design

### Commit Messages

Use conventional commits:
- `Add:` - New feature
- `Fix:` - Bug fix
- `Update:` - Update existing feature
- `Docs:` - Documentation changes
- `Refactor:` - Code refactoring
- `Test:` - Adding tests

Examples:
```
Add: image extraction feature
Fix: heading detection for numbered lists
Update: improve search performance
Docs: add installation instructions
```

## Development Setup

1. **Clone and setup**
   ```bash
   git clone https://github.com/yourusername/pdf-interactive-skill.git
   cd pdf-interactive-skill
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install pytest black flake8  # Development tools
   ```

4. **Set environment variables**
   ```bash
   export ANTHROPIC_API_KEY=your-api-key
   ```

5. **Run tests**
   ```bash
   pytest tests/
   ```

## Project Structure

```
pdf-interactive-skill/
├── scripts/              # Main Python scripts
│   ├── pdf_parser.py    # PDF extraction
│   ├── ai_summarizer.py # AI summarization
│   ├── html_generator.py# HTML generation
│   └── main.py          # Entry point
├── templates/           # HTML templates
│   └── interactive.html # Main template
├── examples/            # Example files
├── tests/               # Test files (to be added)
├── SKILL.md            # Skill definition
├── README.md           # Main documentation
└── requirements.txt    # Python dependencies
```

## Areas for Contribution

### High Priority

- [ ] Image extraction from PDFs
- [ ] Math formula rendering (LaTeX)
- [ ] Better table formatting
- [ ] Batch processing multiple PDFs
- [ ] Unit tests

### Medium Priority

- [ ] Custom CSS themes
- [ ] Export to other formats (Markdown, DOCX)
- [ ] OCR integration for scanned PDFs
- [ ] Progress indicators for long documents
- [ ] Caching for faster re-processing

### Nice to Have

- [ ] Web UI for easier use
- [ ] Cloud storage integration
- [ ] Annotation support
- [ ] Version comparison
- [ ] Collaborative features

## Testing

### Manual Testing

1. Test with various PDF types:
   - Research papers
   - Technical documentation
   - Legal documents
   - Presentations
   - Books

2. Test edge cases:
   - Very large PDFs (500+ pages)
   - PDFs with complex layouts
   - PDFs with images and tables
   - Scanned PDFs

3. Test on different platforms:
   - Windows, macOS, Linux
   - Different browsers
   - Mobile devices

### Automated Testing (Future)

We're working on adding:
- Unit tests for each module
- Integration tests
- End-to-end tests
- Performance benchmarks

## Documentation

When adding features, please update:
- README.md - User-facing documentation
- SKILL.md - Skill definition and usage
- Code comments and docstrings
- This CONTRIBUTING.md if relevant

## Questions?

- Open an issue for questions
- Check existing documentation
- Review closed issues for similar questions

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow

Thank you for contributing! 🎉
