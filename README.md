# BA Business Discover Skills

A collection of OpenSkills designed for Business Analysts to research domains and author educational content.

## 🛠️ Available Skills

### 1. `compose-textbook-for-k12` ⭐ NEW
Comprehensive textbook chapter authoring system for K12 education with pedagogical depth, Vietnam retail context, and Business Analyst thinking framework.

#### 📦 Installation
```bash
# Clone the repository and move to skills folder
# (Already available in .claude/skills/ if you cloned this repo)
npx openskills read compose-textbook-for-k12
```

#### 🚀 Quick Start
1. **Initialize Variables**: Use the interactive script to collect chapter details.
   ```bash
   python3 .claude/skills/compose-textbook-for-k12/scripts/extract_variables.py
   ```
2. **Generate Outline**: Create a structured outline with 6 depth layers.
   ```bash
   python3 .claude/skills/compose-textbook-for-k12/scripts/generate_outline.py chapter_variables.md
   ```
3. **Generate Content**: Load the skill and use the Master Prompt.
   - Trigger: *"Dựa trên dàn ý này, hãy viết nội dung Chương 01 theo chuẩn K12."*
4. **Validate & Analyze**:
   ```bash
   python3 .claude/skills/compose-textbook-for-k12/scripts/chapter_stats.py output/chapter_01.md --detailed
   ```

#### 📄 One-Shot (Lecture Material to Chapter)
You can directly transform notes or slides into a chapter:
- **Trigger**: Gửi file tài liệu và yêu cầu: *"Dựa trên tài liệu này, hãy viết Chương 2 sách giáo khoa K12 về [Chủ đề]."*
- **Action**: Agent sẽ tự động trích xuất nội dung, ánh xạ vào **6 depth layers** và viết toàn bộ chương mà không cần bạn phải nhập biến số thủ công.

---

### 2. `business-domain-handbook`
Skill to research a new business domain specifically for Business Analysts. Use this to create domain-specific knowledge bases quickly.

#### 📦 Installation
```bash
# Install from the packaged zip
npx openskills install dist/business-domain-handbook.zip
```

#### 🚀 Quick Start
- Trigger with a request like:
  - *"Create a Business Analyst handbook for the Vietnam retail domain."*

---

## 🏗️ Project Structure

- `.claude/skills/`: Contains the actual skill implementation (SKILL.md, references, scripts).
- `dist/`: Packaged `.tar.gz` and `.zip` files for distribution.
- `docs/`: Master prompts and development documentation.

## 🧠 Core Principles

### 1. Depth & Pedagogy (for K12)
Every learning concept must follow the **6 Mandatory Depth Layers**:
1. Intuitive Explanation
2. Common Misunderstanding
3. Small Concrete Example (Vietnam context)
4. Extended Mini-Case
5. Decision-Making Relevance
6. Reflective Question

### 2. Domain Decomposition (for BA)
Break any domain into these 6 lenses:
- Business Goals & Value
- Stakeholders & Users
- Core Workflows
- Information & Data
- Systems & Tools
- Pain Points & Constraints

## 🚀 Pushing for Excellence
- **Textbook Quality**: We aim for 10-20 pages of depth, not just summaries.
- **Decision-Useful Knowledge**: We don't just "study", we hunt answers to high-value questions.
- **K12 Accessibility**: Complex concepts must be explainable to a 10th grader.

---
*Created by the Business Discover team.*
