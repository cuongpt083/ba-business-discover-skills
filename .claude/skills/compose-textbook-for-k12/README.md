# compose-textbook-for-k12

Comprehensive textbook chapter authoring system for K12 education with pedagogical depth, Vietnam retail context, and Business Analyst thinking framework.

## Overview

This skill enables AI agents to author **full-length, pedagogically-sound textbook chapters** specifically designed for K12 students (high school level) in the context of **Vietnam grocery retail** and **Business Analyst training**.

## Features

- ✅ **Textbook-quality writing** (not slides, articles, or blog posts)
- ✅ **6 mandatory depth layers** for each core concept
- ✅ **10-20 page equivalent** content length
- ✅ **Self-review and revision** process before final output
- ✅ **K12 comprehension target**: Students must understand ≥70% without teacher assistance

## Quick Start

### 1. Extract Variables

Use the interactive script to collect all required variables:

```bash
python scripts/extract_variables.py
```

### 2. Review References

- **Master Prompt**: `references/master-prompt.md`
- **Chapter Template**: `references/chapter-template.md`
- **Gold Standard Example**: `references/gold-standard-example.md`
- **Pedagogy Guidelines**: `references/pedagogy-guidelines.md`

### 3. Generate Chapter

Load the master prompt and substitute all variables, then generate the chapter using your AI assistant.

### 4. Validate Output

```bash
# Validate chapter quality
python scripts/validate_chapter.py output/chapter-2.md

# Check page count
python scripts/count_pages.py output/chapter-2.md
```

## Directory Structure

```
compose-textbook-for-k12/
├── SKILL.md                          # Main skill documentation
├── README.md                         # This file
├── references/                       # Reference materials
│   ├── master-prompt.md             # Core instruction template
│   ├── chapter-template.md          # Vietnamese chapter structure
│   ├── gold-standard-example.md     # Example of ideal quality
│   └── pedagogy-guidelines.md       # K12 pedagogical principles
├── scripts/                          # Automation scripts
│   ├── validate_chapter.py          # Quality validation
│   ├── count_pages.py               # Page count estimation
│   └── extract_variables.py         # Variable collection helper
└── assets/                           # (Optional) Templates and examples
```

## Required Variables

| Variable | Description |
|----------|-------------|
| `COURSE_NAME` | Full course title |
| `TARGET_LEARNER` | Specific learner profile |
| `INDUSTRY_CONTEXT` | Business domain |
| `CHAPTER_NUMBER` | Chapter sequence number |
| `CHAPTER_TITLE` | Descriptive chapter title |
| `CORE_CONCEPT_1`, `CORE_CONCEPT_2`, `CORE_CONCEPT_3` | Main concepts to teach |
| `OPENING_STORY_CONTEXT` | Scenario to hook students |
| `MAIN_CASE` | Extended business scenario |
| `ROLE_OR_SKILL` | BA role/skill being emphasized |
| `THINKING_FRAMEWORK` | Framework being taught |
| `NEXT_CHAPTER_TOPIC` | Preview of next chapter |

## The 6 Mandatory Depth Layers

Each core concept MUST include:

1. **Intuitive Explanation**: Build initial mental model using familiar concepts
2. **Common Misunderstanding**: Address misconceptions proactively
3. **Small Concrete Vietnam Example**: Ground the concept in local context
4. **Extended Mini-Case**: Demonstrate concept application in realistic scenario
5. **Decision-Making Relevance**: Connect to BA role and real decisions
6. **Reflective Question**: Prompt metacognition and deeper thinking

## Scripts

### validate_chapter.py

Validates a generated chapter against quality criteria:
- Presence of all 6 depth layers
- Structural elements (Insight Box, Common Mistakes, Think Deeper)
- Page count (10-20 pages)
- Vietnamese language consistency

**Usage**:
```bash
python scripts/validate_chapter.py <path-to-chapter.md>
```

### count_pages.py

Estimates page count from markdown content (assuming ~500 words per page).

**Usage**:
```bash
python scripts/count_pages.py <path-to-chapter.md>
```

### extract_variables.py

Interactive helper to collect all required variables and generate a filled template.

**Usage**:
```bash
python scripts/extract_variables.py
```

### generate_outline.py ⭐ NEW

Generates a structured chapter outline with all 6 depth layers, checklists, and planning sections.

**Usage**:
```bash
python scripts/generate_outline.py chapter_variables.md
```

**Features**:
- Detailed outline with all required sections
- [Draft] placeholders for each depth layer
- Pre-generation checklist
- Section length estimates

### batch_generate.py ⭐ NEW

Batch processes multiple chapters from a YAML course configuration file.

**Usage**:
```bash
# Process all chapters
python scripts/batch_generate.py course-config.yaml

# Process specific chapters
python scripts/batch_generate.py course-config.yaml --chapters 1,2,3
```

**Features**:
- Reads course configuration from YAML
- Generates variables files for all chapters
- Automatically creates outlines
- Produces batch processing report

See `examples/course-config.yaml` for configuration format.

### chapter_stats.py ⭐ NEW

Comprehensive analytics tool for chapter quality assessment.

**Usage**:
```bash
# Basic statistics
python scripts/chapter_stats.py chapter.md

# Detailed analysis
python scripts/chapter_stats.py chapter.md --detailed
```

**Metrics**:
- Basic: Word count, page estimate, reading time
- Structure: Headings, boxes, lists, tables
- Pedagogy: Depth layers, questions, examples
- Language: Vietnamese/English ratio, sentence length
- Readability: Flesch Reading Ease, K12 suitability

**Quality Assessment**:
- Identifies issues (missing layers, wrong length)
- Provides warnings (long sentences, few examples)
- Validates K12 standards

## Examples

### Creating Chapter 2 on Data Analysis

```bash
# Step 1: Extract variables
python scripts/extract_variables.py

# Step 2: Generate outline
python scripts/generate_outline.py chapter_variables.md

# Step 3: Review references
cat references/master-prompt.md
cat references/gold-standard-example.md

# Step 4: Generate chapter (using AI assistant with master prompt)

# Step 5: Validate
python scripts/validate_chapter.py output/chapter-2.md
python scripts/chapter_stats.py output/chapter-2.md
```

### Example 2: Batch Processing Multiple Chapters ⭐ NEW

```bash
# Step 1: Create course configuration
# Edit examples/course-config.yaml with your course details

# Step 2: Generate all outlines
python scripts/batch_generate.py examples/course-config.yaml

# Step 3: Review generated files in batch_output/
# - chapter_1_variables.md
# - chapter_1_outline.md
# - chapter_2_variables.md
# - chapter_2_outline.md
# - ... etc

# Step 4: Generate chapters using AI assistant

# Step 5: Validate all chapters
for file in batch_output/chapter_*.md; do
    python scripts/validate_chapter.py "$file"
    python scripts/chapter_stats.py "$file"
done
```

## Best Practices

1. **Always start with variables** - Don't skip variable collection
2. **Reference the gold standard** - Review example before generating
3. **Enforce self-review** - The master prompt includes mandatory self-review
4. **Validate output** - Use scripts to catch missing elements
5. **Iterate based on feedback** - Gather feedback from students and teachers

## License

This skill is part of the ba-business-discover-skills project.

## Version

**v1.1** (2026-01-23): Phase 3 Automation & Enhancement
- Added `generate_outline.py` for structured chapter planning
- Added `batch_generate.py` for multi-chapter processing
- Added `chapter_stats.py` for comprehensive analytics
- Added example course configuration YAML
- Enhanced documentation with batch processing workflows

**v1.0** (2026-01-22): Initial skill creation

## Author

Created using the `skill-creator` skill framework.
