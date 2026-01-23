---
name: compose-textbook-for-k12
description: >
  Comprehensive textbook chapter authoring system for K12 education with pedagogical depth,
  Vietnam retail context, and Business Analyst thinking framework. Use when creating full-length
  textbook chapters (10-20 pages) that require structured learning, mandatory depth layers,
  and self-review quality assurance. Ensures consistent pedagogical pacing and K12 comprehension.
---

# Compose Textbook for K12

## Purpose

This skill enables AI agents to author **full-length, pedagogically-sound textbook chapters** specifically designed for K12 students (high school level) in the context of **Vietnam grocery retail** and **Business Analyst training**.

The skill enforces:
- **Textbook-quality writing** (not slides, articles, or blog posts)
- **6 mandatory depth layers** for each core concept
- **10-20 page equivalent** content length
- **Self-review and revision** process before final output
- **K12 comprehension target**: Students must understand ≥70% without teacher assistance

## When to Use This Skill

### ✅ Use this skill when:

- **Creating textbook chapters** for K12 curriculum (not reference materials or quick guides)
- **Target audience is high school students** (grades 10-12) with zero prior knowledge
- **Content requires deep pedagogical pacing** with scaffolded learning
- **Industry context is Vietnam grocery retail** (or similar retail/business domains)
- **Business Analyst thinking framework** is central to the learning objectives
- **Full chapter development** is needed (10-20 pages with examples, cases, and exercises)

### ❌ Do NOT use this skill for:

- Quick reference materials, cheat sheets, or summary documents
- Professional/adult training materials (use different pedagogical approach)
- Non-retail or non-BA contexts without significant adaptation
- Slide decks, presentation materials, or lecture notes
- Short-form content (< 20 pages)
- Content targeting university level or professional audiences

## ⚡ Quick Triggering (Agent Autonomy)

You can trigger this skill using simple natural language prompts. The agent is trained to take initiative and minimize user friction.

### Simple Prompts
- *"Viết Chương 2 về Phân tích dữ liệu khách hàng cho học sinh lớp 11."*
- *"Tạo một chương sách giáo khoa về kỹ năng đặt câu hỏi trong BA retail."*
- *"Write Chapter 5 on Competition Analysis for K12 retail students."*

### Agent Autonomous Workflow
When a simple prompt or source material is detected, the agent MUST:
1. **Context Analysis**: Identify the chapter number, title, and core concepts.
2. **Variable Extraction**: Attempt to extract all variables defined in `references/master-prompt.md`.
3. **Gap Filling (STRICT)**: 
   - Before generating content, the agent MUST list the variables it has found and identify any **missing mandatory fields** (especially `CORE_CONCEPTS`, `MAIN_CASE`, and `THINKING_FRAMEWORK`).
   - If critical information is missing, the agent **MUST NOT** hallucinate or proceed with generic content. Instead, it must present a clean list of missing information and ask the user to provide it.
4. **User Confirmation**: For complex chapters, the agent should present its proposed outline/variables to the user and say: *"I have gathered the following context. Is this correct or should I adjust anything before I write the 10-20 page chapter?"*
5. **Execution**: Only after all gaps are filled and/or the user confirms, automatically load `references/master-prompt.md` and `references/chapter-template.md` to generate the final chapter.

## 📄 Source-Based One-Shot Generation

This skill is designed to transform existing lecture materials (slides, notes, documents) into high-quality textbook chapters with minimal user interaction.

### How it works:
1. **Input**: Provide a file or paste content (e.g., @"Lecture_Notes.docx").
2. **One-Shot Trigger**: *"Dựa trên tài liệu này, hãy viết Chương 3 cho sách giáo khoa K12."*
3. **Agent Action**:
   - The agent reads the source material.
   - It extracts the technical core and existing examples.
   - It automatically maps these to the **6 mandatory depth layers**.
   - It fills all variables in `master-prompt.md` using the source data.
   - It executes the full generation and self-review process in one pass.

### Benefits:
- **Zero Configuration**: No need to manually run variable extraction scripts.
- **Fact Accuracy**: Higher alignment with your specific curriculum.
- **Speed**: Go from raw notes to a 10-page chapter in minutes.

## How to Use This Skill (For Humans & Agents)

> [!NOTE]
> **For AI Agents**: You do NOT need to ask the user to run scripts manually. If you are an agent reading this, follow the **Quick Triggering** workflow described above to gather variables, infer defaults, and execute the generation autonomously.
> 
> **For Humans**: Follow the steps below to prepare your chapter manually using the provided tools.

### Step 1: Gather Input Variables

Before invoking the master prompt, collect all **required variables** from the user or course design:

#### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `COURSE_NAME` | Full course title | "Business Analysis for Smart Retail" |
| `TARGET_LEARNER` | Specific learner profile | "Grade 10-12 students, Vietnam" |
| `INDUSTRY_CONTEXT` | Business domain | "Vietnam Grocery Retail" |
| `CHAPTER_NUMBER` | Chapter sequence number | "2" |
| `CHAPTER_TITLE` | Descriptive chapter title | "Phân tích dữ liệu khách hàng" |
| `CORE_CONCEPT_1` | First main concept | "Customer Segmentation" |
| `CORE_CONCEPT_2` | Second main concept | "Purchase Pattern Analysis" |
| `CORE_CONCEPT_3` | Third main concept (optional) | "RFM Analysis" |
| `OPENING_STORY_CONTEXT` | Scenario to hook students | "A small grocery store owner struggling with inventory" |
| `MAIN_CASE` | Extended business scenario | "Cô Lan's grocery store in District 10, HCMC" |
| `ROLE_OR_SKILL` | BA role/skill being emphasized | "Data-driven decision making" |
| `THINKING_FRAMEWORK` | Framework being taught | "Problem → Insight → Decision" |
| `NEXT_CHAPTER_TOPIC` | Preview of next chapter | "Inventory optimization techniques" |

**Pro tip**: Use `scripts/extract_variables.py` (if available) to interactively collect these variables.

### Step 2: Review the Chapter Template

Before generating content, review the **chapter template** to understand the expected structure:

```bash
# View the Vietnamese chapter template
cat references/chapter-template.md
```

The template includes:
- Learning objectives
- Opening story (hook)
- Core concepts with 6 depth layers each
- Tools/methods section
- BA thinking section
- Guided practice
- Pre-class assignment
- Vocabulary box
- Chapter summary
- Transition to next chapter

### Step 3: Review the Gold Standard Example

Examine a **complete example chapter** to understand quality expectations:

```bash
# View the gold standard chapter
cat references/gold-standard-example.md
```

Pay attention to:
- **Depth of explanation**: How concepts are expanded vertically, not just listed
- **Pedagogical pacing**: Slow, patient introduction of new ideas
- **Vietnam context**: Specific, relatable examples from local grocery retail
- **Language simplicity**: Accessible to K12 students without heavy jargon

### Step 4: Apply the Master Prompt

Load the **master prompt template** and substitute all variables:

```bash
# View the master prompt
cat references/master-prompt.md
```

The master prompt contains:
- **Absolute Rules**: Non-negotiable requirements for textbook quality
- **Mandatory Depth Layers**: 6 layers required for each core concept
  1. Intuitive explanation
  2. Common misunderstanding
  3. Small concrete Vietnam example
  4. Extended mini-case
  5. Decision-making relevance
  6. Reflective question
- **Structural Requirements**: Page count, recurring elements (Insight Box, Common Mistakes, Think Deeper)
- **Voice & Style**: Patient teacher, real BA mentor, not a marketer
- **Self-Review Phase**: Mandatory checklist and revision process

**Critical**: The master prompt includes a **self-review phase** where the AI must:
1. Check all 6 depth layers are present for each concept
2. Identify 2+ sections that are too shallow
3. Identify 1+ section that may be too abstract for K12
4. Revise those sections immediately
5. Output only the final, revised chapter

### Step 5: Generate the Chapter

Execute the prompt with all variables filled. The generation process will:

1. **Draft the full chapter** following the template structure
2. **Self-review** using the mandatory checklist:
   - Depth check (6 layers per concept?)
   - Pedagogy check (K12 comprehensible?)
   - Textbook quality check (feels like real textbook?)
   - Consistency check (matches gold standard tone?)
3. **Identify weak sections** (too shallow or too abstract)
4. **Revise immediately** with more explanation, examples, and simplified language
5. **Output only the final, revised chapter** in valid Markdown

### Step 6: Validate Output (Optional but Recommended)

Use validation scripts to verify quality:

```bash
# Validate the generated chapter
python scripts/validate_chapter.py output/chapter-2.md

# Check page count estimate

Validation checks:
- ✅ All 6 mandatory depth layers present for each core concept
- ✅ Chapter length within 10-20 pages equivalent
- ✅ Required structural elements included (Insight Box, Common Mistakes, Think Deeper)
- ✅ Vietnamese language consistency
- ✅ No heavy math or advanced code

## Bundled Resources

### References

#### `references/master-prompt.md`
The complete master prompt template with all rules, requirements, and self-review instructions. This is the core instruction set for chapter generation.

#### `references/chapter-template.md`
Vietnamese chapter structure template showing the exact format and sections required. Includes placeholders for all variables.

#### `references/gold-standard-example.md`
A complete example chapter demonstrating ideal quality, depth, and pedagogical pacing. Use this as the benchmark for "what good looks like."

#### `references/pedagogy-guidelines.md`
K12 pedagogical principles and best practices, including:
- Bloom's Taxonomy for high school level
- Scaffolding techniques for complex concepts
- Cognitive load management
- Vietnam education context considerations
- Language simplification strategies

### Scripts

#### `scripts/validate_chapter.py`
Automated chapter quality checker that verifies:
- Presence of all 6 depth layers for each core concept
- Structural elements (Insight Box, Common Mistakes, Think Deeper)
- Estimated page count (10-20 pages)
- Vietnamese language consistency

**Usage**:
```bash
python scripts/validate_chapter.py <path-to-chapter.md>
```

#### `scripts/count_pages.py`
Estimates page count from markdown content using Vietnamese text character counting.

**Usage**:
```bash
python scripts/count_pages.py <path-to-chapter.md>
```

#### `scripts/extract_variables.py`
Interactive helper to extract input variables from user conversation and generate a filled template.

**Usage**:
```bash
python scripts/extract_variables.py
```

#### `scripts/generate_outline.py`
Generates a structured chapter outline with all 6 depth layers, checklists, and planning sections from a variables file.

**Usage**:
```bash
python scripts/generate_outline.py chapter_variables.md
```

**Features**:
- Creates detailed outline with all required sections
- Includes [Draft] placeholders for each depth layer
- Provides pre-generation checklist
- Estimates section lengths

#### `scripts/batch_generate.py`
Batch processes multiple chapters from a YAML course configuration file.

**Usage**:
```bash
# Process all chapters
python scripts/batch_generate.py course-config.yaml

# Process specific chapters only
python scripts/batch_generate.py course-config.yaml --chapters 1,2,3
```

**Features**:
- Reads course configuration from YAML
- Generates variables files for all chapters
- Automatically creates outlines
- Produces batch processing report

**Example course-config.yaml**:
```yaml
course:
  name: "Business Analysis for Smart Retail"
  target_learner: "Grade 10-12 students, Vietnam"
  industry_context: "Vietnam Grocery Retail"

chapters:
  - number: 1
    title: "Business Analyst là gì?"
    core_concepts:
      - "What is a Business Analyst"
      - "Why BA matters in retail"
    opening_story: "Cô Lan's inventory problem"
    main_case: "Cô Lan's store in District 10"
    role_skill: "Problem identification"
    framework: "Ask → Analyze → Recommend"
    next_topic: "Understanding Your Customers"
```

#### `scripts/chapter_stats.py`
Comprehensive analytics tool for chapter quality assessment.

**Usage**:
```bash
# Basic statistics
python scripts/chapter_stats.py chapter.md

# Detailed analysis with depth layer breakdown
python scripts/chapter_stats.py chapter.md --detailed
```

**Metrics Provided**:
- **Basic**: Word count, page estimate, reading time, sentences, paragraphs
- **Structure**: Headings, boxes, lists, tables, code blocks
- **Pedagogy**: Depth layers present, questions, examples, exercises
- **Language**: Vietnamese/English ratio, sentence length, technical terms
- **Readability**: Flesch Reading Ease score, difficulty level, K12 suitability

**Quality Assessment**:
- Identifies issues (missing depth layers, wrong page count, poor readability)
- Provides warnings (too many long sentences, few examples)
- Validates against K12 standards

## Examples

### Example 1: Creating Chapter 2 on Data Analysis

**Input Variables**:
```yaml
COURSE_NAME: "Business Analysis for Smart Retail"
TARGET_LEARNER: "Grade 10-12 students, Vietnam"
INDUSTRY_CONTEXT: "Vietnam Grocery Retail"
CHAPTER_NUMBER: "2"
CHAPTER_TITLE: "Phân tích dữ liệu khách hàng"
CORE_CONCEPT_1: "Customer Segmentation"
CORE_CONCEPT_2: "Purchase Pattern Analysis"
CORE_CONCEPT_3: "RFM Analysis"
OPENING_STORY_CONTEXT: "Cô Lan runs a small grocery store in District 10, HCMC. She notices some customers buy daily, others weekly, but doesn't know how to serve each group better."
MAIN_CASE: "Cô Lan's store has 200 regular customers. She wants to understand their buying patterns to optimize inventory and promotions."
ROLE_OR_SKILL: "Data-driven decision making"
THINKING_FRAMEWORK: "Observe → Segment → Decide"
NEXT_CHAPTER_TOPIC: "Inventory optimization using demand forecasting"
```

**Output**: A 30-page textbook chapter with:
- Opening story about Cô Lan's challenge
- 6-layer depth explanation of Customer Segmentation
- 6-layer depth explanation of Purchase Pattern Analysis
- 6-layer depth explanation of RFM Analysis
- Guided practice: Segment Cô Lan's customers
- Pre-class assignment: Analyze a local store's customer data
- Vocabulary box with Vietnamese translations
- Smooth transition to Chapter 3

### Example 2: Adapting for Different Industry Context

If adapting to a **different industry** (e.g., healthcare, education), update:

```yaml
INDUSTRY_CONTEXT: "Vietnam Healthcare Sector"
OPENING_STORY_CONTEXT: "Dr. Minh manages a community clinic in rural Vietnam..."
MAIN_CASE: "Clinic patient flow optimization..."
```

**Important**: Keep the same:
- Pedagogical structure (6 depth layers)
- K12 comprehension target
- Self-review process
- 10-20 page length

### Example 3: Creating Chapter 1 (Foundation Chapter)

For **Chapter 1** (introductory chapter), emphasize:

```yaml
CHAPTER_NUMBER: "1"
CHAPTER_TITLE: "Business Analyst là gì?"
CORE_CONCEPT_1: "What is a Business Analyst"
CORE_CONCEPT_2: "Why BA matters in retail"
CORE_CONCEPT_3: "BA thinking framework introduction"
THINKING_FRAMEWORK: "Ask → Analyze → Recommend"
```

Chapter 1 should:
- Assume **zero prior knowledge**
- Define all basic terms
- Build foundational mental models
- Set expectations for the course

### Example 4: Batch Processing Multiple Chapters

For creating an entire course (5+ chapters), use the batch processing workflow:

**Step 1: Create course configuration**
```yaml
# course-config.yaml
course:
  name: "Business Analysis for Smart Retail"
  target_learner: "Grade 10-12 students, Vietnam"
  industry_context: "Vietnam Grocery Retail"

chapters:
  - number: 1
    title: "Business Analyst là gì?"
    core_concepts: [...]
    # ... other fields
  - number: 2
    title: "Hiểu khách hàng"
    # ... etc
```

**Step 2: Generate all outlines**
```bash
python scripts/batch_generate.py course-config.yaml
```

**Step 3: Review and customize outlines**
- Edit generated outlines in `batch_output/`
- Fill in [Draft] placeholders
- Adjust examples and cases

**Step 4: Generate chapters**
- Use master prompt with each outline
- Generate chapters sequentially or in parallel

**Step 5: Validate all chapters**
```bash
for file in batch_output/chapter_*.md; do
    python scripts/validate_chapter.py "$file"
    python scripts/chapter_stats.py "$file"
done
```

**Benefits**:
- Consistent variables across all chapters
- Ensures continuity (next_topic matches next chapter)
- Saves time on variable collection
- Batch validation and quality checks

## Best Practices

### 1. Always Start with Variables
Don't skip variable collection. Incomplete variables lead to generic, low-quality chapters.

### 2. Reference the Gold Standard
Before generating, review `references/gold-standard-example.md` to calibrate quality expectations.

### 3. Enforce Self-Review
The master prompt includes mandatory self-review. Don't skip this step—it's what ensures quality.

### 4. Validate Output
Use `scripts/validate_chapter.py` to catch missing depth layers or structural elements.

### 5. Iterate Based on Feedback
After generating a chapter, gather feedback from:
- K12 students (can they understand ≥70%?)
- Teachers (is the pacing appropriate?)
- Subject matter experts (is the content accurate?)

Use feedback to refine the master prompt or add examples to the gold standard.

### 6. Maintain Consistency
If creating multiple chapters for the same course:
- Keep `COURSE_NAME`, `TARGET_LEARNER`, `INDUSTRY_CONTEXT` consistent
- Ensure `NEXT_CHAPTER_TOPIC` matches the next chapter's `CHAPTER_TITLE`
- Build on concepts introduced in earlier chapters

## Troubleshooting

### Problem: Generated chapter is too short (< 20 pages)

**Solution**:
- Check that all 6 depth layers are present for each core concept
- Review the gold standard example—chapters should feel "slow and patient"
- Add more mini-cases and extended examples
- Expand the guided practice section

### Problem: Language is too complex for K12

**Solution**:
- Review `references/pedagogy-guidelines.md` for simplification strategies
- Avoid jargon without explanation
- Use more analogies and concrete examples
- Test with actual K12 students

### Problem: Content feels generic, not Vietnam-specific

**Solution**:
- Use specific Vietnam locations (District 10, HCMC; Hanoi Old Quarter)
- Reference local brands (Vinmart, Co.opmart, Bách Hóa Xanh)
- Include cultural context (Tết shopping, wet markets)
- Use Vietnamese names for characters (Cô Lan, Anh Minh)

### Problem: Self-review phase is skipped

**Solution**:
- Ensure the master prompt is loaded completely
- Explicitly instruct the AI to perform self-review
- Check that the output includes revisions, not just the first draft

## Advanced Usage

### Customizing the Master Prompt

For specific course needs, you can modify `references/master-prompt.md`:

1. **Adjust page count**: Change "10–20 textbook pages" to your target
2. **Add domain-specific rules**: Insert industry-specific requirements
3. **Modify depth layers**: Adapt the 6 layers to your pedagogical approach
4. **Change language**: Adapt for English-language textbooks

**Warning**: Maintain the core structure (absolute rules, depth layers, self-review) to preserve quality.

### Creating a Course Series

To create a **full course** (10+ chapters):

1. **Design the course outline** first (all chapter titles and core concepts)
2. **Create Chapter 1** as the gold standard
3. **Use Chapter 1** as the reference for subsequent chapters
4. **Maintain a glossary** of terms introduced in earlier chapters
5. **Build concept dependencies** (later chapters reference earlier concepts)

### Localization

To adapt for **non-Vietnam contexts**:

1. Update `INDUSTRY_CONTEXT` to your target region/industry
2. Replace Vietnam-specific examples with local equivalents
3. Adjust cultural references (holidays, brands, locations)
4. Keep the pedagogical structure unchanged

## References

- [Bloom's Taxonomy for K12 Education](https://en.wikipedia.org/wiki/Bloom%27s_taxonomy)
- [Scaffolding in Education](https://en.wikipedia.org/wiki/Instructional_scaffolding)
- [Cognitive Load Theory](https://en.wikipedia.org/wiki/Cognitive_load)
- Vietnam Ministry of Education K12 Standards

## Version History

- **v1.0** (2026-01-22): Initial skill creation with master prompt, chapter template, and pedagogy guidelines
