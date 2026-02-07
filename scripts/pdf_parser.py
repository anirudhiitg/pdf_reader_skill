#!/usr/bin/env python3
"""
PDF Parser
Extracts text and structure from PDF documents
"""

import pdfplumber
import re
from typing import List, Dict, Optional


class PDFParser:
    """Extract text and structure from PDF files"""

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.pages = []
        self.sections = []

    def extract_text(self) -> List[Dict]:
        """Extract text from all pages"""
        with pdfplumber.open(self.pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    self.pages.append({
                        'page_number': i + 1,
                        'text': text,
                        'width': page.width,
                        'height': page.height
                    })
        return self.pages

    def detect_headings(self, text: str) -> List[Dict]:
        """
        Detect headings in text based on common patterns:
        - ALL CAPS lines
        - Lines ending with newline but not period
        - Short lines (< 100 chars)
        - Lines with numbering (1. 2. etc.)
        """
        lines = text.split('\n')
        headings = []

        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue

            # Patterns that suggest a heading
            is_all_caps = line.isupper() and len(line.split()) > 1
            is_numbered = re.match(r'^(\d+\.|\d+\)|\w\.|[IVX]+\.)', line)
            is_short = len(line) < 100
            is_title_case = line.istitle()

            # Calculate heading level
            level = 1
            if is_numbered:
                # Count the depth of numbering (1.1.1 = level 3)
                level = line.split()[0].count('.') + 1
            elif is_all_caps:
                level = 1
            elif is_title_case and is_short:
                level = 2
            else:
                continue

            headings.append({
                'line_number': i,
                'text': line,
                'level': min(level, 3)  # Max level 3
            })

        return headings

    def parse_structure(self) -> List[Dict]:
        """
        Parse the PDF into structured sections based on headings
        """
        if not self.pages:
            self.extract_text()

        # Combine all page text
        full_text = '\n'.join([page['text'] for page in self.pages])

        # Detect headings
        headings = self.detect_headings(full_text)

        if not headings:
            # No headings found, treat entire document as one section
            return [{
                'title': 'Document Content',
                'level': 1,
                'content': full_text
            }]

        # Split text into sections based on headings
        lines = full_text.split('\n')
        sections = []

        for i, heading in enumerate(headings):
            start_line = heading['line_number']
            end_line = headings[i + 1]['line_number'] if i + 1 < len(headings) else len(lines)

            # Extract content between headings
            content_lines = lines[start_line + 1:end_line]
            content = '\n'.join(content_lines).strip()

            sections.append({
                'title': heading['text'],
                'level': heading['level'],
                'content': content
            })

        self.sections = sections
        return sections

    def get_metadata(self) -> Dict:
        """Extract PDF metadata"""
        with pdfplumber.open(self.pdf_path) as pdf:
            return {
                'pages': len(pdf.pages),
                'metadata': pdf.metadata
            }

    def extract_tables(self, page_number: int) -> List:
        """Extract tables from a specific page"""
        with pdfplumber.open(self.pdf_path) as pdf:
            if 0 <= page_number < len(pdf.pages):
                page = pdf.pages[page_number]
                return page.extract_tables()
        return []


def parse_pdf(pdf_path: str) -> Dict:
    """
    Main function to parse a PDF and return structured data

    Args:
        pdf_path: Path to the PDF file

    Returns:
        Dictionary with sections, metadata, and raw text
    """
    parser = PDFParser(pdf_path)

    # Extract and parse
    parser.extract_text()
    sections = parser.parse_structure()
    metadata = parser.get_metadata()

    return {
        'sections': sections,
        'metadata': metadata,
        'pages': parser.pages
    }


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Usage: python pdf_parser.py <pdf_file>")
        sys.exit(1)

    pdf_file = sys.argv[1]
    result = parse_pdf(pdf_file)

    print(f"\n=== PDF Analysis ===")
    print(f"Pages: {result['metadata']['pages']}")
    print(f"Sections: {len(result['sections'])}")
    print(f"\n=== Sections ===")

    for i, section in enumerate(result['sections'], 1):
        print(f"\n{i}. {section['title']} (Level {section['level']})")
        print(f"   Content length: {len(section['content'])} characters")
