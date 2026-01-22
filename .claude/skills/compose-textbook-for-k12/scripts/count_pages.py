#!/usr/bin/env python3
"""
Estimates page count from markdown content.

Assumptions:
- ~500 words per page for Vietnamese text
- Excludes code blocks and tables from word count
- Accounts for Vietnamese character density

Usage:
    python count_pages.py <path-to-chapter.md>

Author: compose-textbook-for-k12 skill
Version: 1.0
"""

import sys
import re
from pathlib import Path


def count_pages(file_path):
    """
    Estimates page count from markdown file.
    
    Args:
        file_path: Path to the markdown chapter file
        
    Returns:
        dict: Page count estimate and word count details
    """
    if not Path(file_path).exists():
        return {"error": f"File not found: {file_path}"}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove code blocks
    content = re.sub(r'```[\s\S]*?```', '', content)
    
    # Remove tables (simplified)
    content = re.sub(r'\|.*\|', '', content)
    
    # Remove markdown formatting
    content = re.sub(r'[#*_`\[\]()]', '', content)
    
    # Count words (space-separated tokens)
    words = len(content.split())
    
    # Estimate pages (500 words per page)
    pages = words / 500
    
    return {
        "file": file_path,
        "word_count": words,
        "estimated_pages": round(pages, 1),
        "target_range": "25-35 pages",
        "in_range": 25 <= pages <= 35
    }


def print_results(results):
    """Print page count results in a readable format."""
    print("\n" + "="*60)
    print(f"PAGE COUNT ESTIMATE: {results['file']}")
    print("="*60)
    print(f"\nWord Count: {results['word_count']:,}")
    print(f"Estimated Pages: {results['estimated_pages']}")
    print(f"Target Range: {results['target_range']}")
    
    if results['in_range']:
        print("\n✅ Page count is within target range")
    else:
        print("\n⚠️  Page count is outside target range")
        if results['estimated_pages'] < 25:
            print(f"   Need approximately {int((25 - results['estimated_pages']) * 500)} more words")
        else:
            print(f"   Need to reduce by approximately {int((results['estimated_pages'] - 35) * 500)} words")
    
    print("="*60 + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_pages.py <path-to-chapter.md>")
        sys.exit(1)
    
    chapter_file = sys.argv[1]
    results = count_pages(chapter_file)
    
    if "error" in results:
        print(f"Error: {results['error']}")
        sys.exit(1)
    
    print_results(results)
