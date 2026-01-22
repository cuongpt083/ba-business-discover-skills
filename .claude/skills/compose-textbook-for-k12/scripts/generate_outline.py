#!/usr/bin/env python3
"""
Generate a chapter outline from input variables.

This script creates a structured outline that can be used as a starting point
for chapter generation, helping authors visualize the chapter structure before
full content creation.

Usage:
    python generate_outline.py <variables-file.md>
    python generate_outline.py --interactive

Author: compose-textbook-for-k12 skill
Version: 1.0
"""

import sys
import re
from pathlib import Path


def parse_variables_file(file_path):
    """
    Parse a variables file (created by extract_variables.py) and extract variables.
    
    Args:
        file_path: Path to the variables markdown file
        
    Returns:
        dict: Variable name -> value mapping
    """
    if not Path(file_path).exists():
        return {"error": f"File not found: {file_path}"}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    variables = {}
    
    # Extract variables from markdown format
    patterns = {
        'COURSE_NAME': r'\*\*Course Name\*\*:\s*(.+)',
        'TARGET_LEARNER': r'\*\*Target Learner\*\*:\s*(.+)',
        'INDUSTRY_CONTEXT': r'\*\*Industry Context\*\*:\s*(.+)',
        'CHAPTER_NUMBER': r'\*\*Chapter Number\*\*:\s*(.+)',
        'CHAPTER_TITLE': r'\*\*Chapter Title\*\*:\s*(.+)',
        'CORE_CONCEPT_1': r'1\.\s*(.+)',
        'CORE_CONCEPT_2': r'2\.\s*(.+)',
        'CORE_CONCEPT_3': r'3\.\s*(.+)',
        'OPENING_STORY_CONTEXT': r'\*\*Opening Story Context\*\*:\s*(.+)',
        'MAIN_CASE': r'\*\*Main Case\*\*:\s*(.+)',
        'ROLE_OR_SKILL': r'\*\*Role/Skill Focus\*\*:\s*(.+)',
        'THINKING_FRAMEWORK': r'\*\*Thinking Framework\*\*:\s*(.+)',
        'NEXT_CHAPTER_TOPIC': r'\*\*Next Chapter Topic\*\*:\s*(.+)',
    }
    
    for var_name, pattern in patterns.items():
        match = re.search(pattern, content)
        if match:
            variables[var_name] = match.group(1).strip()
    
    return variables


def generate_outline(variables):
    """
    Generate a structured chapter outline from variables.
    
    Args:
        variables: dict of variable name -> value
        
    Returns:
        str: Formatted chapter outline
    """
    outline = f"""# Chapter {variables.get('CHAPTER_NUMBER', 'X')} Outline: {variables.get('CHAPTER_TITLE', 'Title')}

> **Course**: {variables.get('COURSE_NAME', 'Course Name')}  
> **Target**: {variables.get('TARGET_LEARNER', 'Target Learner')}  
> **Context**: {variables.get('INDUSTRY_CONTEXT', 'Industry Context')}

---

## 📋 Chapter Structure Overview

### Estimated Length
- **Target**: 10-20 pages
- **Word Count**: 5,000-10,000 words
- **Reading Time**: 40-80 minutes

### Core Components
1. Opening Story
2. Core Concept 1: {variables.get('CORE_CONCEPT_1', 'Concept 1')}
3. Core Concept 2: {variables.get('CORE_CONCEPT_2', 'Concept 2')}
4. Core Concept 3: {variables.get('CORE_CONCEPT_3', 'Concept 3')} (if applicable)
5. Tools/Methods
6. BA Thinking Framework
7. Guided Practice
8. Pre-class Assignment

---

## 1. Opening Story (2-3 pages)

### Story Context
{variables.get('OPENING_STORY_CONTEXT', 'Story context here')}

### Main Case
{variables.get('MAIN_CASE', 'Main business scenario here')}

### Hook Questions
- What problem does the protagonist face?
- Why is this problem important?
- What would you do in their situation?

### Learning Connection
- How does this story relate to {variables.get('CORE_CONCEPT_1', 'the first concept')}?
- What questions should a BA ask in this situation?

---

## 2. Core Concept 1: {variables.get('CORE_CONCEPT_1', 'Concept 1')} (3-4 pages)

### 6 Mandatory Depth Layers

#### Layer 1: Intuitive Explanation
- [ ] Start with familiar analogy or daily life example
- [ ] Build initial mental model
- [ ] Avoid technical jargon

**Draft**: [Write intuitive explanation here]

#### Layer 2: Common Misunderstanding
- [ ] Identify typical misconception
- [ ] Explain why it's tempting to think this way
- [ ] Clarify correct understanding

**Draft**: [Write common misunderstanding here]

#### Layer 3: Small Concrete Vietnam Example
- [ ] Use specific location (District, city)
- [ ] Include local brands or cultural context
- [ ] Keep it 2-3 sentences

**Draft**: [Write Vietnam example here]

#### Layer 4: Extended Mini-Case
- [ ] Develop 1-2 paragraph story
- [ ] Include problem, analysis, outcome
- [ ] Show concept in action

**Draft**: [Write mini-case here]

#### Layer 5: Decision-Making Relevance
- [ ] Connect to BA role
- [ ] Explain "So what? Why does this matter?"
- [ ] Link to {variables.get('THINKING_FRAMEWORK', 'thinking framework')}

**Draft**: [Write decision-making relevance here]

#### Layer 6: Reflective Question
- [ ] Ask open-ended question
- [ ] Encourage personal connection
- [ ] No single "right" answer

**Draft**: [Write reflective question here]

### Structural Elements
- [ ] Insight Box (💡)
- [ ] Common Mistakes Box (⚠️)
- [ ] Think Deeper Box (🤔)

---

## 3. Core Concept 2: {variables.get('CORE_CONCEPT_2', 'Concept 2')} (3-4 pages)

### 6 Mandatory Depth Layers

#### Layer 1: Intuitive Explanation
**Draft**: [Write intuitive explanation here]

#### Layer 2: Common Misunderstanding
**Draft**: [Write common misunderstanding here]

#### Layer 3: Small Concrete Vietnam Example
**Draft**: [Write Vietnam example here]

#### Layer 4: Extended Mini-Case
**Draft**: [Write mini-case here]

#### Layer 5: Decision-Making Relevance
**Draft**: [Write decision-making relevance here]

#### Layer 6: Reflective Question
**Draft**: [Write reflective question here]

### Structural Elements
- [ ] Insight Box (💡)
- [ ] Common Mistakes Box (⚠️)
- [ ] Think Deeper Box (🤔)

---

## 4. Core Concept 3: {variables.get('CORE_CONCEPT_3', 'Concept 3')} (2-3 pages, if applicable)

### 6 Mandatory Depth Layers

#### Layer 1: Intuitive Explanation
**Draft**: [Write intuitive explanation here]

#### Layer 2: Common Misunderstanding
**Draft**: [Write common misunderstanding here]

#### Layer 3: Small Concrete Vietnam Example
**Draft**: [Write Vietnam example here]

#### Layer 4: Extended Mini-Case
**Draft**: [Write mini-case here]

#### Layer 5: Decision-Making Relevance
**Draft**: [Write decision-making relevance here]

#### Layer 6: Reflective Question
**Draft**: [Write reflective question here]

### Structural Elements
- [ ] Insight Box (💡)
- [ ] Common Mistakes Box (⚠️)
- [ ] Think Deeper Box (🤔)

---

## 5. Tools/Methods: {variables.get('THINKING_FRAMEWORK', 'Framework')} (2-3 pages)

### Description
- [ ] Explain the tool/method in simple terms
- [ ] When to use it
- [ ] When NOT to use it

### Application in {variables.get('INDUSTRY_CONTEXT', 'context')}
- [ ] Concrete example from Vietnam grocery retail
- [ ] Step-by-step demonstration
- [ ] Common pitfalls

---

## 6. BA Thinking: {variables.get('ROLE_OR_SKILL', 'Role/Skill')} (1-2 pages)

### What Makes a Good BA?
- [ ] Key mindsets and behaviors
- [ ] Connection to {variables.get('THINKING_FRAMEWORK', 'framework')}
- [ ] Real-world application

### Reflective Questions
- [ ] Which skill do you need to develop?
- [ ] What question from this chapter made you think most?

---

## 7. Guided Practice (2-3 pages)

### Objective
- [ ] Apply {variables.get('CORE_CONCEPT_1', 'concept 1')} to a new scenario
- [ ] Practice {variables.get('THINKING_FRAMEWORK', 'framework')}

### Scenario
**Draft**: [Write practice scenario here - should be similar to main case but different enough to require thinking]

### Steps
1. [ ] [Step 1]
2. [ ] [Step 2]
3. [ ] [Step 3]

### Self-Assessment Checklist
- [ ] I understand the objective
- [ ] I tried adjusting my approach
- [ ] I can explain the result in my own words

---

## 8. Pre-class Assignment (1-2 pages)

### Task
**Draft**: [Write assignment description - should connect to next chapter: {variables.get('NEXT_CHAPTER_TOPIC', 'next topic')}]

### Deliverables
- [ ] [Deliverable 1]
- [ ] [Deliverable 2]

### Guidance
- [ ] Suggest using AI as assistant
- [ ] Emphasize understanding "why", not just "what"

---

## 9. Vocabulary Box (1 page)

### Key Terms
- [ ] {variables.get('CORE_CONCEPT_1', 'Concept 1')} (Vietnamese + English)
- [ ] {variables.get('CORE_CONCEPT_2', 'Concept 2')} (Vietnamese + English)
- [ ] {variables.get('CORE_CONCEPT_3', 'Concept 3')} (Vietnamese + English)
- [ ] {variables.get('THINKING_FRAMEWORK', 'Framework')} (Vietnamese + English)
- [ ] Other domain-specific terms

---

## 10. Chapter Summary & Transition (1 page)

### Key Takeaways
- [ ] Main learning from {variables.get('CORE_CONCEPT_1', 'concept 1')}
- [ ] Main learning from {variables.get('CORE_CONCEPT_2', 'concept 2')}
- [ ] Foundation for next chapter

### Teaser for Next Chapter
**Draft**: "In the next chapter, we'll explore {variables.get('NEXT_CHAPTER_TOPIC', 'next topic')} and how it helps [future value]."

---

## ✅ Pre-Generation Checklist

Before generating the full chapter, ensure:

### Content Planning
- [ ] All 6 depth layers planned for each core concept
- [ ] Vietnam-specific examples identified
- [ ] Mini-cases drafted
- [ ] Structural elements (boxes) planned

### Pedagogical Quality
- [ ] Language appropriate for K12 (simple, clear)
- [ ] Scaffolding from concrete to abstract
- [ ] Cognitive load managed (one concept at a time)
- [ ] 70% comprehension target achievable

### Consistency
- [ ] Tone matches gold standard
- [ ] {variables.get('INDUSTRY_CONTEXT', 'Industry context')} used throughout
- [ ] {variables.get('THINKING_FRAMEWORK', 'Framework')} integrated
- [ ] Connects to previous and next chapters

### Length
- [ ] Estimated 10-20 pages (5,000-10,000 words)
- [ ] Balanced distribution across sections
- [ ] Not too rushed, not too slow

---

## 📝 Notes for Author

### Strengths to Leverage
- Vietnam grocery retail context is rich with examples
- {variables.get('ROLE_OR_SKILL', 'BA role')} is practical and relatable
- {variables.get('THINKING_FRAMEWORK', 'Framework')} provides clear structure

### Potential Challenges
- Keeping language simple for K12
- Balancing depth with accessibility
- Finding enough Vietnam-specific examples

### Tips
- Use real store names (Vinmart, Co.opmart, Bách Hóa Xanh)
- Use common Vietnamese names (Cô Lan, Anh Minh, Chị Hương)
- Include cultural context (Tết, wet markets, family businesses)
- Test explanations with "explain to younger sibling" approach

---

## Next Steps

1. **Review this outline** - Make sure all sections make sense
2. **Fill in drafts** - Add content to [Draft] placeholders
3. **Load master prompt** - Use references/master-prompt.md
4. **Generate chapter** - Use AI assistant with filled outline
5. **Validate** - Run scripts/validate_chapter.py
6. **Iterate** - Revise based on validation feedback

---

*Generated by generate_outline.py - compose-textbook-for-k12 skill*
"""
    
    return outline


def save_outline(outline, output_file="chapter_outline.md"):
    """Save the outline to a file."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(outline)
    
    print(f"\n✅ Outline saved to: {output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_outline.py <variables-file.md>")
        print("   or: python generate_outline.py --interactive")
        sys.exit(1)
    
    if sys.argv[1] == "--interactive":
        print("\n🚀 Interactive mode not yet implemented.")
        print("Please use extract_variables.py first, then pass the generated file to this script.")
        sys.exit(1)
    
    variables_file = sys.argv[1]
    
    print(f"\n📖 Generating outline from: {variables_file}")
    
    variables = parse_variables_file(variables_file)
    
    if "error" in variables:
        print(f"❌ Error: {variables['error']}")
        sys.exit(1)
    
    print(f"\n✅ Parsed {len(variables)} variables")
    
    outline = generate_outline(variables)
    
    output_file = f"chapter_{variables.get('CHAPTER_NUMBER', 'X')}_outline.md"
    save_outline(outline, output_file)
    
    print(f"\n✅ Done! Review the outline and fill in the [Draft] placeholders before generating the full chapter.")
