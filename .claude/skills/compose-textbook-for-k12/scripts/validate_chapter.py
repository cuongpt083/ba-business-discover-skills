#!/usr/bin/env python3
"""
Validates a generated textbook chapter against quality criteria.

Usage:
    python validate_chapter.py <path-to-chapter.md>

Checks:
- Presence of all 6 mandatory depth layers for each core concept
- Structural elements (Insight Box, Common Mistakes, Think Deeper)
- Estimated page count (10-20 pages)
- Vietnamese language consistency

Author: compose-textbook-for-k12 skill
Version: 1.0
"""

import sys
import re
from pathlib import Path


def validate_chapter(file_path):
    """
    Validates a textbook chapter against quality criteria.
    
    Args:
        file_path: Path to the markdown chapter file
        
    Returns:
        dict: Validation results with pass/fail status and details
    """
    if not Path(file_path).exists():
        return {"error": f"File not found: {file_path}"}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    results = {
        "file": file_path,
        "passed": True,
        "checks": []
    }
    
    # Check 1: Depth layers presence
    depth_layers = check_depth_layers(content)
    results["checks"].append(depth_layers)
    if not depth_layers["passed"]:
        results["passed"] = False
    
    # Check 2: Structural elements
    structural = check_structural_elements(content)
    results["checks"].append(structural)
    if not structural["passed"]:
        results["passed"] = False
    
    # Check 3: Page count estimate
    page_count = estimate_page_count(content)
    results["checks"].append(page_count)
    if not page_count["passed"]:
        results["passed"] = False
    
    # Check 4: Vietnamese language consistency
    language = check_language_consistency(content)
    results["checks"].append(language)
    if not language["passed"]:
        results["passed"] = False
    
    return results


def check_depth_layers(content):
    """Check if all 6 mandatory depth layers are present."""
    # This is a simplified check - in production, you'd use more sophisticated NLP
    layers = {
        "intuitive_explanation": False,
        "common_misunderstanding": False,
        "vietnam_example": False,
        "extended_case": False,
        "decision_relevance": False,
        "reflective_question": False
    }
    
    # Look for indicators of each layer
    if re.search(r'(tưởng tượng|hãy nghĩ|bạn thấy)', content, re.IGNORECASE):
        layers["intuitive_explanation"] = True
    
    if re.search(r'(sai lầm|common mistake|misunderstanding)', content, re.IGNORECASE):
        layers["common_misunderstanding"] = True
    
    if re.search(r'(quận|district|TP\.HCM|Hà Nội|Vinmart|Co\.op)', content, re.IGNORECASE):
        layers["vietnam_example"] = True
    
    if re.search(r'(mini.?case|tình huống|câu chuyện)', content, re.IGNORECASE):
        layers["extended_case"] = True
    
    if re.search(r'(quyết định|decision|tại sao.*quan trọng)', content, re.IGNORECASE):
        layers["decision_relevance"] = True
    
    if re.search(r'(câu hỏi suy ngẫm|think deeper|reflective)', content, re.IGNORECASE):
        layers["reflective_question"] = True
    
    missing = [k for k, v in layers.items() if not v]
    
    return {
        "name": "Depth Layers Check",
        "passed": len(missing) == 0,
        "details": f"Found {6 - len(missing)}/6 layers. Missing: {', '.join(missing) if missing else 'None'}"
    }


def check_structural_elements(content):
    """Check for required structural elements."""
    elements = {
        "insight_box": bool(re.search(r'(💡|Insight)', content, re.IGNORECASE)),
        "common_mistakes": bool(re.search(r'(⚠️|Common Mistake)', content, re.IGNORECASE)),
        "think_deeper": bool(re.search(r'(🤔|Think Deeper)', content, re.IGNORECASE))
    }
    
    missing = [k for k, v in elements.items() if not v]
    
    return {
        "name": "Structural Elements Check",
        "passed": len(missing) == 0,
        "details": f"Found {3 - len(missing)}/3 elements. Missing: {', '.join(missing) if missing else 'None'}"
    }


def estimate_page_count(content):
    """Estimate page count (assuming ~500 words per page for Vietnamese text)."""
    # Count words (simplified for Vietnamese - counts space-separated tokens)
    words = len(content.split())
    estimated_pages = words / 500
    
    in_range = 10 <= estimated_pages <= 20
    
    return {
        "name": "Page Count Estimate",
        "passed": in_range,
        "details": f"Estimated {estimated_pages:.1f} pages (target: 10-20). Word count: {words}"
    }


def check_language_consistency(content):
    """Check for Vietnamese language consistency."""
    # Simple check: ensure Vietnamese characters are present
    vietnamese_chars = bool(re.search(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]', content))
    
    return {
        "name": "Vietnamese Language Check",
        "passed": vietnamese_chars,
        "details": "Vietnamese characters detected" if vietnamese_chars else "No Vietnamese characters found"
    }


def print_results(results):
    """Print validation results in a readable format."""
    print("\n" + "="*60)
    print(f"VALIDATION REPORT: {results['file']}")
    print("="*60)
    
    for check in results["checks"]:
        status = "✅ PASS" if check["passed"] else "❌ FAIL"
        print(f"\n{status} - {check['name']}")
        print(f"  {check['details']}")
    
    print("\n" + "="*60)
    if results["passed"]:
        print("✅ OVERALL: PASSED - Chapter meets quality criteria")
    else:
        print("❌ OVERALL: FAILED - Chapter needs revision")
    print("="*60 + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_chapter.py <path-to-chapter.md>")
        sys.exit(1)
    
    chapter_file = sys.argv[1]
    results = validate_chapter(chapter_file)
    
    if "error" in results:
        print(f"Error: {results['error']}")
        sys.exit(1)
    
    print_results(results)
    sys.exit(0 if results["passed"] else 1)
