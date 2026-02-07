#!/usr/bin/env python3
"""
AI Summarizer
Uses Claude API to summarize and clean PDF content
"""

import os
from typing import List, Dict, Optional
from anthropic import Anthropic


class AISummarizer:
    """Summarize and clean content using Claude AI"""

    def __init__(self, api_key: Optional[str] = None, summary_level: str = 'balanced'):
        """
        Initialize the summarizer

        Args:
            api_key: Anthropic API key (defaults to ANTHROPIC_API_KEY env var)
            summary_level: 'brief', 'balanced', or 'detailed'
        """
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")

        self.client = Anthropic(api_key=self.api_key)
        self.summary_level = summary_level
        self.model = "claude-sonnet-4-5-20250929"

    def get_summary_prompt(self, level: str) -> str:
        """Get the appropriate prompt based on summary level"""
        prompts = {
            'brief': """Provide a very brief summary (2-3 sentences) of the key points.
                       Focus only on the most important information.""",

            'balanced': """Summarize the main points in a clear, concise way (4-6 sentences).
                          Include key details while remaining accessible.""",

            'detailed': """Provide a comprehensive summary that covers all major points and
                          important details. Aim for thoroughness while maintaining clarity."""
        }
        return prompts.get(level, prompts['balanced'])

    def summarize_section(self, title: str, content: str) -> str:
        """
        Summarize a single section of content

        Args:
            title: Section title
            content: Section content

        Returns:
            Summarized text
        """
        if len(content) < 100:
            # Too short to summarize
            return content

        prompt = f"""You are helping to summarize a section from a PDF document.

Section Title: {title}

Section Content:
{content}

Task: {self.get_summary_prompt(self.summary_level)}

Important:
- Be accurate and preserve key information
- Use clear, simple language
- Remove redundancy and filler
- Maintain the original meaning
- Format with proper paragraphs

Provide only the summary, no preamble or meta-commentary."""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text.strip()
        except Exception as e:
            print(f"Warning: Failed to summarize section '{title}': {e}")
            return content  # Return original on error

    def clean_content(self, content: str) -> str:
        """
        Clean and format content for better readability

        Args:
            content: Raw content text

        Returns:
            Cleaned and formatted HTML content
        """
        if len(content) < 50:
            return f"<p>{content}</p>"

        prompt = f"""Clean and format this text for display in an HTML document.

Content:
{content}

Task:
- Fix any OCR errors or formatting issues
- Break into proper paragraphs
- Format lists as HTML lists (<ul> or <ol>)
- Identify and format code blocks with <pre><code>
- Highlight important points with <strong>
- Add <blockquote> for quotes
- Use <p> tags for paragraphs
- Keep tables as clean HTML tables

Return only the formatted HTML, no preamble or explanation."""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=2048,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text.strip()
        except Exception as e:
            print(f"Warning: Failed to clean content: {e}")
            # Basic fallback formatting
            paragraphs = content.split('\n\n')
            return '\n'.join([f"<p>{p.strip()}</p>" for p in paragraphs if p.strip()])

    def process_sections(self, sections: List[Dict], skip_summary: bool = False) -> List[Dict]:
        """
        Process all sections with summarization and cleaning

        Args:
            sections: List of section dictionaries
            skip_summary: If True, only clean content without summarizing

        Returns:
            Processed sections with summaries and cleaned HTML content
        """
        processed = []
        total = len(sections)

        for i, section in enumerate(sections, 1):
            print(f"Processing section {i}/{total}: {section['title']}")

            processed_section = {
                'title': section['title'],
                'level': section['level'],
                'content': self.clean_content(section['content'])
            }

            if not skip_summary:
                summary = self.summarize_section(section['title'], section['content'])
                processed_section['summary'] = summary

            processed.append(processed_section)

        return processed

    def generate_document_summary(self, sections: List[Dict]) -> str:
        """
        Generate an overall document summary

        Args:
            sections: List of section dictionaries

        Returns:
            Overall document summary
        """
        # Combine all section titles and beginnings
        overview = "\n\n".join([
            f"{s['title']}: {s['content'][:200]}..."
            for s in sections[:10]  # First 10 sections
        ])

        prompt = f"""Provide a brief executive summary of this document based on its sections:

{overview}

Task: Write a 2-3 paragraph overview that captures:
- What this document is about
- Main topics covered
- Key takeaways

Be concise and informative."""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=512,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text.strip()
        except Exception as e:
            print(f"Warning: Failed to generate document summary: {e}")
            return "Summary generation failed."


def summarize_pdf_content(sections: List[Dict], summary_level: str = 'balanced',
                          skip_summary: bool = False) -> Dict:
    """
    Main function to summarize PDF content

    Args:
        sections: List of section dictionaries from PDF parser
        summary_level: 'brief', 'balanced', or 'detailed'
        skip_summary: If True, skip AI summarization

    Returns:
        Dictionary with processed sections and document summary
    """
    summarizer = AISummarizer(summary_level=summary_level)

    # Process sections
    processed_sections = summarizer.process_sections(sections, skip_summary)

    # Generate document summary
    doc_summary = None
    if not skip_summary:
        doc_summary = summarizer.generate_document_summary(sections)

    return {
        'sections': processed_sections,
        'document_summary': doc_summary
    }


if __name__ == '__main__':
    import sys
    import json

    if len(sys.argv) < 2:
        print("Usage: python ai_summarizer.py <sections_json_file>")
        sys.exit(1)

    # Load sections from JSON file
    with open(sys.argv[1], 'r') as f:
        data = json.load(f)

    result = summarize_pdf_content(data['sections'])

    print("\n=== Document Summary ===")
    print(result['document_summary'])
    print(f"\n=== Processed {len(result['sections'])} sections ===")
