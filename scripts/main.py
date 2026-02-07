#!/usr/bin/env python3
"""
PDF Interactive Skill - Main Entry Point
Orchestrates PDF parsing, AI summarization, and HTML generation
"""

import argparse
import os
import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from pdf_parser import parse_pdf
from ai_summarizer import summarize_pdf_content
from html_generator import generate_html


def main():
    """Main entry point for the PDF Interactive skill"""

    parser = argparse.ArgumentParser(
        description='Convert PDF to interactive HTML with AI summarization',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s document.pdf
  %(prog)s report.pdf --output summary.html --summary-level detailed
  %(prog)s paper.pdf --skip-summary --dark-mode
        """
    )

    parser.add_argument('pdf_file', help='Path to PDF file')
    parser.add_argument('--output', '-o', help='Output HTML file (default: same as PDF name)')
    parser.add_argument('--summary-level', choices=['brief', 'balanced', 'detailed'],
                        default='balanced', help='Level of AI summarization (default: balanced)')
    parser.add_argument('--skip-summary', action='store_true',
                        help='Skip AI summarization (faster)')
    parser.add_argument('--dark-mode', action='store_true',
                        help='Default to dark mode in output')
    parser.add_argument('--no-search', action='store_true',
                        help='Disable search functionality')
    parser.add_argument('--title', help='Custom page title (default: PDF filename)')

    args = parser.parse_args()

    # Validate PDF file exists
    pdf_path = Path(args.pdf_file)
    if not pdf_path.exists():
        print(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = pdf_path.with_suffix('.html')

    # Determine title
    title = args.title or pdf_path.stem

    print(f"📄 Processing: {pdf_path.name}")
    print(f"🎯 Output: {output_path}")
    print()

    try:
        # Step 1: Parse PDF
        print("📖 Step 1/3: Parsing PDF...")
        pdf_data = parse_pdf(str(pdf_path))
        print(f"   ✓ Found {len(pdf_data['sections'])} sections across {pdf_data['metadata']['pages']} pages")

        # Step 2: AI Processing (optional)
        if args.skip_summary:
            print("⚡ Step 2/3: Skipping AI summarization (--skip-summary)")
            processed_sections = pdf_data['sections']
            # Still clean the content for HTML
            for section in processed_sections:
                # Basic HTML formatting
                paragraphs = section['content'].split('\n\n')
                section['content'] = '\n'.join([f"<p>{p.strip()}</p>" for p in paragraphs if p.strip()])
        else:
            print(f"🤖 Step 2/3: AI summarization ({args.summary_level} mode)...")
            if not os.getenv('ANTHROPIC_API_KEY'):
                print("\n⚠️  Warning: ANTHROPIC_API_KEY not set!")
                print("   Set it with: export ANTHROPIC_API_KEY=your-api-key")
                print("   Or use --skip-summary to skip AI processing")
                sys.exit(1)

            result = summarize_pdf_content(
                pdf_data['sections'],
                summary_level=args.summary_level,
                skip_summary=False
            )
            processed_sections = result['sections']
            print(f"   ✓ Summarized {len(processed_sections)} sections")

        # Step 3: Generate HTML
        print("🎨 Step 3/3: Generating interactive HTML...")
        output_file = generate_html(
            sections=processed_sections,
            title=title,
            output_path=str(output_path),
            metadata={
                'pages': pdf_data['metadata']['pages'],
                'source': pdf_path.name
            },
            dark_mode=args.dark_mode,
            no_search=args.no_search
        )

        print(f"   ✓ Generated: {output_file}")
        print()
        print("✨ Done! Open the HTML file in your browser:")
        print(f"   {output_file}")

    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        if '--debug' in sys.argv:
            raise
        sys.exit(1)


if __name__ == '__main__':
    main()
