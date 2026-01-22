#!/usr/bin/env python3
"""
Interactive helper to extract input variables from user conversation.

Prompts user for each required variable and generates a filled template.

Usage:
    python extract_variables.py

Author: compose-textbook-for-k12 skill
Version: 1.0
"""

import sys
from pathlib import Path


REQUIRED_VARIABLES = [
    ("COURSE_NAME", "Full course title", "Business Analysis for Smart Retail"),
    ("TARGET_LEARNER", "Specific learner profile", "Grade 10-12 students, Vietnam"),
    ("INDUSTRY_CONTEXT", "Business domain", "Vietnam Grocery Retail"),
    ("CHAPTER_NUMBER", "Chapter sequence number", "2"),
    ("CHAPTER_TITLE", "Descriptive chapter title", "Phân tích dữ liệu khách hàng"),
    ("CORE_CONCEPT_1", "First main concept", "Customer Segmentation"),
    ("CORE_CONCEPT_2", "Second main concept", "Purchase Pattern Analysis"),
    ("CORE_CONCEPT_3", "Third main concept (optional)", "RFM Analysis"),
    ("OPENING_STORY_CONTEXT", "Scenario to hook students", "Cô Lan's store struggling with inventory"),
    ("MAIN_CASE", "Extended business scenario", "Cô Lan's grocery store in District 10, HCMC"),
    ("ROLE_OR_SKILL", "BA role/skill being emphasized", "Data-driven decision making"),
    ("THINKING_FRAMEWORK", "Framework being taught", "Observe → Segment → Decide"),
    ("NEXT_CHAPTER_TOPIC", "Preview of next chapter", "Inventory optimization techniques"),
]


def extract_variables():
    """
    Interactively collect all required variables from user.
    
    Returns:
        dict: Variable name -> value mapping
    """
    print("\n" + "="*60)
    print("TEXTBOOK CHAPTER VARIABLE EXTRACTION")
    print("="*60)
    print("\nThis tool will help you collect all required variables")
    print("for generating a textbook chapter.\n")
    print("Press Enter to use the default value shown in [brackets].\n")
    
    variables = {}
    
    for var_name, description, default in REQUIRED_VARIABLES:
        prompt = f"{var_name}\n  {description}\n  [{default}]: "
        value = input(prompt).strip()
        
        if not value:
            value = default
        
        variables[var_name] = value
        print()
    
    return variables


def generate_template(variables):
    """
    Generate a filled template with the collected variables.
    
    Args:
        variables: dict of variable name -> value
        
    Returns:
        str: Filled template content
    """
    template = f"""# Chapter Generation Variables

## Course Information
- **Course Name**: {variables['COURSE_NAME']}
- **Target Learner**: {variables['TARGET_LEARNER']}
- **Industry Context**: {variables['INDUSTRY_CONTEXT']}

## Chapter Details
- **Chapter Number**: {variables['CHAPTER_NUMBER']}
- **Chapter Title**: {variables['CHAPTER_TITLE']}

## Core Concepts
1. {variables['CORE_CONCEPT_1']}
2. {variables['CORE_CONCEPT_2']}
3. {variables['CORE_CONCEPT_3']}

## Narrative Elements
- **Opening Story Context**: {variables['OPENING_STORY_CONTEXT']}
- **Main Case**: {variables['MAIN_CASE']}

## BA Framework
- **Role/Skill Focus**: {variables['ROLE_OR_SKILL']}
- **Thinking Framework**: {variables['THINKING_FRAMEWORK']}

## Course Continuity
- **Next Chapter Topic**: {variables['NEXT_CHAPTER_TOPIC']}

---

## Variable Substitution Format

Use these variables in the master prompt by replacing placeholders:

```
{{{{COURSE_NAME}}}} → {variables['COURSE_NAME']}
{{{{TARGET_LEARNER}}}} → {variables['TARGET_LEARNER']}
{{{{INDUSTRY_CONTEXT}}}} → {variables['INDUSTRY_CONTEXT']}
{{{{CHAPTER_NUMBER}}}} → {variables['CHAPTER_NUMBER']}
{{{{CHAPTER_TITLE}}}} → {variables['CHAPTER_TITLE']}
{{{{CORE_CONCEPT_1}}}} → {variables['CORE_CONCEPT_1']}
{{{{CORE_CONCEPT_2}}}} → {variables['CORE_CONCEPT_2']}
{{{{CORE_CONCEPT_3}}}} → {variables['CORE_CONCEPT_3']}
{{{{OPENING_STORY_CONTEXT}}}} → {variables['OPENING_STORY_CONTEXT']}
{{{{MAIN_CASE}}}} → {variables['MAIN_CASE']}
{{{{ROLE_OR_SKILL}}}} → {variables['ROLE_OR_SKILL']}
{{{{THINKING_FRAMEWORK}}}} → {variables['THINKING_FRAMEWORK']}
{{{{NEXT_CHAPTER_TOPIC}}}} → {variables['NEXT_CHAPTER_TOPIC']}
```

## Next Steps

1. Review the variables above
2. Load the master prompt from `references/master-prompt.md`
3. Substitute all variables in the master prompt
4. Generate the chapter using your AI assistant
5. Validate the output using `scripts/validate_chapter.py`
"""
    
    return template


def save_template(template, output_file="chapter_variables.md"):
    """Save the filled template to a file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"\n✅ Variables saved to: {output_file}")


if __name__ == "__main__":
    print("\n🚀 Starting variable extraction...\n")
    
    variables = extract_variables()
    
    print("\n" + "="*60)
    print("SUMMARY OF COLLECTED VARIABLES")
    print("="*60)
    for var_name, value in variables.items():
        print(f"{var_name}: {value}")
    
    print("\n" + "="*60)
    confirm = input("\nDo you want to save these variables? (y/n): ").strip().lower()
    
    if confirm == 'y':
        template = generate_template(variables)
        save_template(template)
        print("\n✅ Done! You can now use these variables to generate your chapter.")
    else:
        print("\n❌ Variables not saved. Exiting.")
