#!/usr/bin/env python3
"""
Generate statistics and analytics for textbook chapters.

Provides insights into chapter quality, consistency, and readability metrics.

Usage:
    python chapter_stats.py <chapter.md>
    python chapter_stats.py <chapter.md> --detailed
    python chapter_stats.py <directory> --compare

Author: compose-textbook-for-k12 skill
Version: 1.0
"""

import sys
import re
from pathlib import Path
from collections import Counter


def analyze_chapter(file_path):
    """
    Analyze a chapter and generate comprehensive statistics.
    
    Args:
        file_path: Path to the markdown chapter file
        
    Returns:
        dict: Chapter statistics and metrics
    """
    if not Path(file_path).exists():
        return {"error": f"File not found: {file_path}"}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    stats = {
        "file": file_path,
        "basic": analyze_basic_stats(content),
        "structure": analyze_structure(content),
        "pedagogy": analyze_pedagogy(content),
        "language": analyze_language(content),
        "readability": estimate_readability(content)
    }
    
    return stats


def analyze_basic_stats(content):
    """Analyze basic content statistics."""
    # Remove code blocks
    content_no_code = re.sub(r'```[\s\S]*?```', '', content)
    
    # Count words
    words = content_no_code.split()
    word_count = len(words)
    
    # Count characters (excluding spaces)
    char_count = len(content_no_code.replace(' ', '').replace('\n', ''))
    
    # Count sentences (simplified)
    sentences = re.split(r'[.!?]+', content_no_code)
    sentence_count = len([s for s in sentences if s.strip()])
    
    # Count paragraphs
    paragraphs = content.split('\n\n')
    paragraph_count = len([p for p in paragraphs if p.strip() and not p.strip().startswith('#')])
    
    # Estimate pages (500 words per page)
    estimated_pages = word_count / 500
    
    # Estimate reading time (200 words per minute)
    reading_time_minutes = word_count / 200
    
    return {
        "word_count": word_count,
        "character_count": char_count,
        "sentence_count": sentence_count,
        "paragraph_count": paragraph_count,
        "estimated_pages": round(estimated_pages, 1),
        "reading_time_minutes": round(reading_time_minutes, 1),
        "avg_words_per_sentence": round(word_count / sentence_count, 1) if sentence_count > 0 else 0,
        "avg_words_per_paragraph": round(word_count / paragraph_count, 1) if paragraph_count > 0 else 0
    }


def analyze_structure(content):
    """Analyze chapter structure."""
    # Count headings by level
    h1_count = len(re.findall(r'^# ', content, re.MULTILINE))
    h2_count = len(re.findall(r'^## ', content, re.MULTILINE))
    h3_count = len(re.findall(r'^### ', content, re.MULTILINE))
    h4_count = len(re.findall(r'^#### ', content, re.MULTILINE))
    
    # Count structural elements
    insight_boxes = len(re.findall(r'(💡|Insight)', content, re.IGNORECASE))
    mistake_boxes = len(re.findall(r'(⚠️|Common Mistake)', content, re.IGNORECASE))
    think_boxes = len(re.findall(r'(🤔|Think Deeper)', content, re.IGNORECASE))
    
    # Count lists
    bullet_lists = len(re.findall(r'^\s*[-*+] ', content, re.MULTILINE))
    numbered_lists = len(re.findall(r'^\s*\d+\. ', content, re.MULTILINE))
    
    # Count tables
    tables = len(re.findall(r'\|.*\|', content))
    
    # Count code blocks
    code_blocks = len(re.findall(r'```', content)) // 2
    
    return {
        "headings": {
            "h1": h1_count,
            "h2": h2_count,
            "h3": h3_count,
            "h4": h4_count,
            "total": h1_count + h2_count + h3_count + h4_count
        },
        "boxes": {
            "insight": insight_boxes,
            "mistakes": mistake_boxes,
            "think_deeper": think_boxes,
            "total": insight_boxes + mistake_boxes + think_boxes
        },
        "lists": {
            "bullet": bullet_lists,
            "numbered": numbered_lists,
            "total": bullet_lists + numbered_lists
        },
        "tables": tables,
        "code_blocks": code_blocks
    }


def analyze_pedagogy(content):
    """Analyze pedagogical elements."""
    # Check for depth layer indicators
    depth_layers = {
        "intuitive_explanation": bool(re.search(r'(tưởng tượng|hãy nghĩ|bạn thấy)', content, re.IGNORECASE)),
        "common_misunderstanding": bool(re.search(r'(sai lầm|common mistake|misunderstanding)', content, re.IGNORECASE)),
        "vietnam_example": bool(re.search(r'(quận|district|TP\.HCM|Hà Nội|Vinmart|Co\.op|Bách Hóa)', content, re.IGNORECASE)),
        "mini_case": bool(re.search(r'(mini.?case|tình huống|câu chuyện)', content, re.IGNORECASE)),
        "decision_relevance": bool(re.search(r'(quyết định|decision|tại sao.*quan trọng)', content, re.IGNORECASE)),
        "reflective_question": bool(re.search(r'(câu hỏi suy ngẫm|think deeper|reflective)', content, re.IGNORECASE))
    }
    
    # Count questions
    questions = len(re.findall(r'\?', content))
    
    # Count examples (heuristic: look for "ví dụ", "example", specific names)
    examples = len(re.findall(r'(ví dụ|example|Cô Lan|Anh Minh|Chị Hương)', content, re.IGNORECASE))
    
    # Count exercises/practice
    exercises = len(re.findall(r'(bài tập|exercise|practice|thực hành)', content, re.IGNORECASE))
    
    return {
        "depth_layers_present": sum(depth_layers.values()),
        "depth_layers_detail": depth_layers,
        "question_count": questions,
        "example_count": examples,
        "exercise_count": exercises
    }


def analyze_language(content):
    """Analyze language characteristics."""
    # Vietnamese character detection
    vietnamese_chars = len(re.findall(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]', content))
    
    # English words (heuristic: words with only ASCII letters)
    english_words = len(re.findall(r'\b[A-Za-z]+\b', content))
    
    # Technical terms (words in backticks or parentheses)
    technical_terms = len(re.findall(r'`[^`]+`|\([A-Za-z\s]+\)', content))
    
    # Sentence length analysis
    sentences = re.split(r'[.!?]+', content)
    sentence_lengths = [len(s.split()) for s in sentences if s.strip()]
    
    avg_sentence_length = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    max_sentence_length = max(sentence_lengths) if sentence_lengths else 0
    
    # Long sentences (> 25 words - potential readability issue)
    long_sentences = len([l for l in sentence_lengths if l > 25])
    
    return {
        "vietnamese_chars": vietnamese_chars,
        "english_words": english_words,
        "technical_terms": technical_terms,
        "avg_sentence_length": round(avg_sentence_length, 1),
        "max_sentence_length": max_sentence_length,
        "long_sentences_count": long_sentences,
        "long_sentences_percent": round(long_sentences / len(sentence_lengths) * 100, 1) if sentence_lengths else 0
    }


def estimate_readability(content):
    """Estimate readability metrics."""
    # Remove code blocks and special characters
    clean_content = re.sub(r'```[\s\S]*?```', '', content)
    clean_content = re.sub(r'[#*_`\[\]()]', '', clean_content)
    
    words = clean_content.split()
    word_count = len(words)
    
    sentences = re.split(r'[.!?]+', clean_content)
    sentence_count = len([s for s in sentences if s.strip()])
    
    # Syllable count (simplified for Vietnamese - count vowel groups)
    syllables = len(re.findall(r'[aeiouàáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹ]+', clean_content.lower()))
    
    # Flesch Reading Ease (adapted for Vietnamese)
    # Formula: 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)
    if sentence_count > 0 and word_count > 0:
        flesch_score = 206.835 - 1.015 * (word_count / sentence_count) - 84.6 * (syllables / word_count)
        flesch_score = max(0, min(100, flesch_score))  # Clamp to 0-100
    else:
        flesch_score = 0
    
    # Interpret Flesch score
    if flesch_score >= 80:
        difficulty = "Very Easy (Grade 5)"
    elif flesch_score >= 70:
        difficulty = "Easy (Grade 6-7)"
    elif flesch_score >= 60:
        difficulty = "Fairly Easy (Grade 8-9)"
    elif flesch_score >= 50:
        difficulty = "Standard (Grade 10-12)"
    elif flesch_score >= 30:
        difficulty = "Fairly Difficult (College)"
    else:
        difficulty = "Difficult (University+)"
    
    return {
        "flesch_reading_ease": round(flesch_score, 1),
        "difficulty_level": difficulty,
        "suitable_for_k12": flesch_score >= 50
    }


def print_stats(stats, detailed=False):
    """Print statistics in a readable format."""
    print("\n" + "="*60)
    print(f"CHAPTER STATISTICS: {Path(stats['file']).name}")
    print("="*60)
    
    # Basic Stats
    basic = stats['basic']
    print("\n📊 BASIC STATISTICS")
    print(f"  Word Count: {basic['word_count']:,}")
    print(f"  Estimated Pages: {basic['estimated_pages']}")
    print(f"  Reading Time: {basic['reading_time_minutes']} minutes")
    print(f"  Sentences: {basic['sentence_count']}")
    print(f"  Paragraphs: {basic['paragraph_count']}")
    print(f"  Avg Words/Sentence: {basic['avg_words_per_sentence']}")
    print(f"  Avg Words/Paragraph: {basic['avg_words_per_paragraph']}")
    
    # Structure
    structure = stats['structure']
    print("\n🏗️  STRUCTURE")
    print(f"  Headings: {structure['headings']['total']} (H1:{structure['headings']['h1']}, H2:{structure['headings']['h2']}, H3:{structure['headings']['h3']})")
    print(f"  Boxes: {structure['boxes']['total']} (Insight:{structure['boxes']['insight']}, Mistakes:{structure['boxes']['mistakes']}, Think:{structure['boxes']['think_deeper']})")
    print(f"  Lists: {structure['lists']['total']} (Bullet:{structure['lists']['bullet']}, Numbered:{structure['lists']['numbered']})")
    print(f"  Tables: {structure['tables']}")
    print(f"  Code Blocks: {structure['code_blocks']}")
    
    # Pedagogy
    pedagogy = stats['pedagogy']
    print("\n📚 PEDAGOGICAL ELEMENTS")
    print(f"  Depth Layers Present: {pedagogy['depth_layers_present']}/6")
    if detailed:
        for layer, present in pedagogy['depth_layers_detail'].items():
            status = "✅" if present else "❌"
            print(f"    {status} {layer}")
    print(f"  Questions: {pedagogy['question_count']}")
    print(f"  Examples: {pedagogy['example_count']}")
    print(f"  Exercises: {pedagogy['exercise_count']}")
    
    # Language
    language = stats['language']
    print("\n🌐 LANGUAGE ANALYSIS")
    print(f"  Vietnamese Characters: {language['vietnamese_chars']:,}")
    print(f"  English Words: {language['english_words']:,}")
    print(f"  Technical Terms: {language['technical_terms']}")
    print(f"  Avg Sentence Length: {language['avg_sentence_length']} words")
    print(f"  Max Sentence Length: {language['max_sentence_length']} words")
    print(f"  Long Sentences (>25 words): {language['long_sentences_count']} ({language['long_sentences_percent']}%)")
    
    # Readability
    readability = stats['readability']
    print("\n📖 READABILITY")
    print(f"  Flesch Reading Ease: {readability['flesch_reading_ease']}")
    print(f"  Difficulty Level: {readability['difficulty_level']}")
    suitable = "✅ Yes" if readability['suitable_for_k12'] else "❌ No"
    print(f"  Suitable for K12: {suitable}")
    
    # Quality Assessment
    print("\n✅ QUALITY ASSESSMENT")
    
    issues = []
    warnings = []
    
    # Check page count
    if basic['estimated_pages'] < 10:
        issues.append(f"Chapter too short ({basic['estimated_pages']} pages, target: 10-20)")
    elif basic['estimated_pages'] > 20:
        warnings.append(f"Chapter too long ({basic['estimated_pages']} pages, target: 10-20)")
    
    # Check depth layers
    if pedagogy['depth_layers_present'] < 6:
        issues.append(f"Missing depth layers ({pedagogy['depth_layers_present']}/6)")
    
    # Check structural elements
    if structure['boxes']['total'] < 3:
        warnings.append(f"Few structural boxes ({structure['boxes']['total']}, recommend: 3+)")
    
    # Check sentence length
    if language['long_sentences_percent'] > 20:
        warnings.append(f"Many long sentences ({language['long_sentences_percent']}%, may be hard for K12)")
    
    # Check readability
    if not readability['suitable_for_k12']:
        issues.append(f"Readability too difficult for K12 (Flesch: {readability['flesch_reading_ease']})")
    
    if not issues and not warnings:
        print("  ✅ No issues found - Chapter meets quality standards")
    else:
        if issues:
            print("  ❌ ISSUES:")
            for issue in issues:
                print(f"     - {issue}")
        if warnings:
            print("  ⚠️  WARNINGS:")
            for warning in warnings:
                print(f"     - {warning}")
    
    print("="*60 + "\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python chapter_stats.py <chapter.md>")
        print("   or: python chapter_stats.py <chapter.md> --detailed")
        sys.exit(1)
    
    chapter_file = sys.argv[1]
    detailed = "--detailed" in sys.argv
    
    print(f"\n📊 Analyzing chapter: {chapter_file}")
    
    stats = analyze_chapter(chapter_file)
    
    if "error" in stats:
        print(f"❌ Error: {stats['error']}")
        sys.exit(1)
    
    print_stats(stats, detailed=detailed)
