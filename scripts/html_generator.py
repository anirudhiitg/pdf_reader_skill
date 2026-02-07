#!/usr/bin/env python3
"""
HTML Generator
Generates interactive HTML from processed PDF content
"""

import os
from datetime import datetime
from typing import Dict, List, Optional
from jinja2 import Environment, FileSystemLoader
from pathlib import Path


class HTMLGenerator:
    """Generate interactive HTML pages from PDF content"""

    def __init__(self, template_dir: Optional[str] = None):
        """
        Initialize the HTML generator

        Args:
            template_dir: Path to directory containing templates
        """
        if template_dir is None:
            # Default to templates directory in the skill
            script_dir = Path(__file__).parent
            template_dir = script_dir.parent / 'templates'

        self.template_dir = str(template_dir)
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def generate(self,
                 sections: List[Dict],
                 title: str,
                 output_path: str,
                 metadata: Optional[Dict] = None,
                 dark_mode: bool = False,
                 no_search: bool = False) -> str:
        """
        Generate HTML from processed sections

        Args:
            sections: List of processed section dictionaries
            title: Page title
            output_path: Where to save the HTML file
            metadata: Optional metadata to include
            dark_mode: Default to dark mode
            no_search: Disable search functionality

        Returns:
            Path to generated HTML file
        """
        # Load template
        template = self.env.get_template('interactive.html')

        # Prepare metadata
        if metadata is None:
            metadata = {}

        metadata['generated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Render template
        html = template.render(
            title=title,
            sections=sections,
            metadata=metadata,
            dark_mode=dark_mode,
            no_search=no_search
        )

        # Write to file
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        return str(output_path)


def generate_html(sections: List[Dict],
                  title: str,
                  output_path: str,
                  metadata: Optional[Dict] = None,
                  dark_mode: bool = False,
                  no_search: bool = False) -> str:
    """
    Main function to generate HTML from processed PDF content

    Args:
        sections: List of section dictionaries
        title: Page title
        output_path: Output HTML file path
        metadata: Optional metadata dictionary
        dark_mode: Default to dark mode
        no_search: Disable search functionality

    Returns:
        Path to generated HTML file
    """
    generator = HTMLGenerator()
    return generator.generate(
        sections=sections,
        title=title,
        output_path=output_path,
        metadata=metadata,
        dark_mode=dark_mode,
        no_search=no_search
    )


if __name__ == '__main__':
    import sys
    import json

    if len(sys.argv) < 3:
        print("Usage: python html_generator.py <sections_json> <output_html> [title]")
        sys.exit(1)

    # Load sections
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        data = json.load(f)

    output_file = sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else "Document"

    result = generate_html(
        sections=data['sections'],
        title=title,
        output_path=output_file,
        metadata=data.get('metadata')
    )

    print(f"Generated HTML: {result}")
