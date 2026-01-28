# Claude Code Instructions: ICA Practice Problem Generator

This repository is a skeleton for generating CodeSignal ICA-style practice problems. When asked to create a new problem, follow these instructions.

## Repository Structure

```
ica_practice/
├── simulation.py              # Main solution file (class with method stubs)
├── test_simulation.py         # Test suite organized by level
├── levels/
│   ├── LEVEL_1.md             # Level 1 requirements
│   ├── LEVEL_2.md             # Level 2 requirements
│   ├── LEVEL_3.md             # Level 3 requirements
│   └── LEVEL_4.md             # Level 4 requirements
└── mini_problems/             # Smaller focused practice problems
```

## Creating a New ICA Problem

When the user asks for a new ICA problem, generate ALL of the following:

### 1. Choose a Real-World Scenario

Good scenarios are domain-agnostic and relatable:

- Banking/payment systems
- Order management (restaurant, e-commerce)
- Reservation/booking systems
- Task/job schedulers
- Inventory management
- Messaging/notification systems
- File/document management

### 2. Design 4 Progressive Levels

| Level | Time      | Complexity    | Typical Features                    |
| ----- | --------- | ------------- | ----------------------------------- |
| 1     | 10-15 min | Basic CRUD    | Create, read, simple validation     |
| 2     | 20-30 min | Relationships | Transfers, lookups between entities |
| 3     | 30-60 min | Aggregation   | History, reports, sorting, top-N    |
| 4     | 30-60 min | Advanced      | Scheduling, callbacks, dependencies |

**Key principle:** Each level MUST build on the previous. Code from Level 1 should be used in Level 4.

### 3. Generate Files

#### simulation.py Template

```python
"""
CodeSignal Industry Coding Assessment Practice
===============================================

PROBLEM: [Scenario Name]

[Brief description of the scenario]

Time Limit: 90 minutes (not expected to complete all levels)

RUNNING TESTS:
    Level 1: make test-1
    Level 2: make test-2
    Level 3: make test-3
    Level 4: make test-4
    All:     make test-all
"""

from typing import Optional


class [SystemName]:
    """
    [Brief description]

    LEVEL 1: [Category Name]
    - method_1(args) -> return_type
    - method_2(args) -> return_type

    LEVEL 2: [Category Name]
    - method_3(args) -> return_type
    - method_4(args) -> return_type

    LEVEL 3: [Category Name]
    - method_5(args) -> return_type
    - method_6(args) -> return_type

    LEVEL 4: [Category Name]
    - method_7(args) -> return_type
    - method_8(args) -> return_type
    """

    def __init__(self):
        """Initialize the system."""
        pass

    # Level 1, 2, 3, 4 methods with pass (NO implementation hints)
```

**IMPORTANT:** The simulation.py file should contain:

- Docstring with problem description and test commands
- Class docstring listing all methods by level
- Method stubs with ONLY `pass` (no implementation hints)
- Type hints on all methods
- Docstrings describing behavior, args, returns, and examples

#### test_simulation.py Template

- Organize tests by level using classes: `TestLevel1...`, `TestLevel2...`, etc.
- Each level should have 8-15 tests
- Include tests for:
  - Happy path (basic success)
  - Edge cases (empty, zero, negative)
  - Error conditions (not found, duplicates, invalid input)
  - Boundary conditions
- Test names should be descriptive: `test_level_1_create_account_duplicate`

#### LEVEL_X.md Template

```markdown
# Level X: [Category Name]

**Time Estimate:** XX-XX minutes

## Overview

[1-2 sentences describing what this level adds]

## Methods to Implement

### `method_name`

\`\`\`python
def method_name(self, arg1: type1, arg2: type2) -> return_type
\`\`\`

[Brief description of what the method does]

| Input          | Output                 |
| -------------- | ---------------------- |
| Valid input    | Expected output        |
| Invalid case 1 | `False` / `None` / etc |
| Invalid case 2 | `False` / `None` / etc |

---

[Repeat for each method]

## Edge Cases to Handle

- [List of edge cases]

## Run Tests

\`\`\`bash
make test-X
\`\`\`

## Example Usage

\`\`\`python
[Working code examples]
\`\`\`
```

### 4. Update Makefile

Add test targets for the new problem:

```makefile
test-1:
	uv run pytest ica_practice/test_simulation.py -k "level_1" -v
```

## Concepts to Cover Across Levels

### Level 1-2 (Fundamentals)

- Dictionary operations (create, read, update)
- Input validation (positive numbers, non-empty strings)
- Duplicate detection (using sets)
- Basic arithmetic (balances, counts)

### Level 3 (Intermediate)

- Transaction/history tracking
- Sorting with multiple criteria (`key=lambda x: (-x[1], x[0])`)
- Aggregation (top-N, totals, averages)
- String formatting for reports

### Level 4 (Advanced)

- Queues and scheduling (`deque`, `heapq`)
- Timestamp-based processing
- Percentage calculations with integer division
- Dependencies or state machines

## Common Patterns to Include

### Counting Pattern

```python
counts[key] = counts.get(key, 0) + 1
```

### Sorting with Multiple Criteria

```python
sorted(items, key=lambda x: (-x[1], x[0]))  # Descending by [1], ascending by [0]
```

### FIFO Queue

```python
from collections import deque
queue = deque()
queue.append(item)      # Add
item = queue.popleft()  # Remove
```

### Priority Queue

```python
import heapq
heapq.heappush(heap, (priority, item))
priority, item = heapq.heappop(heap)
```

### Integer Division for Percentages

```python
result = (amount * percent) // 100
```

### Timestamp-Based Processing

```python
def operation(self, current_time):
    self._process_due(current_time)  # Always process scheduled items first
    # Then do the operation
```

## Quality Checklist

Before finalizing a new problem, verify:

- [ ] 4 levels with increasing complexity
- [ ] Each level builds on previous levels
- [ ] simulation.py has method stubs (pass only, no hints)
- [ ] test_simulation.py has 40-60 tests total
- [ ] 4 LEVEL_X.md files with full function signatures
- [ ] Makefile updated with test targets
- [ ] Edge cases covered in tests
- [ ] Examples in README files are accurate

## Mini Problems

For focused practice on specific concepts, create smaller problems in `mini_problems/`:

- Single concept focus (queues, sorting, etc.)
- 15-20 minute completion time
- 20-35 tests
- Separate README with function signatures

## Live Interview Mode

When the user asks for a "live interview", "mock interview", or "Harvey-style practice", YOU become the interviewer. Do NOT just generate files — run an interactive interview session.

### How to Run a Live Interview

1. **Introduce yourself and set expectations**
   ```
   "Hi, I'm your interviewer today. We'll be working through a coding problem
   together for about 45-60 minutes. I'll present the problem in stages, and
   each stage builds on the previous. Feel free to ask clarifying questions,
   and please think out loud as you work. Ready to begin?"
   ```

2. **Present Level 1 only** — Do NOT reveal later levels upfront
   - Give a brief scenario description
   - State the first 2-3 methods to implement
   - Ask: "Before you start coding, do you have any clarifying questions?"

3. **Evaluate their clarifying questions**
   - Good questions: "What should happen if X?" "Can Y be negative?"
   - If they don't ask, gently prompt: "What assumptions are you making about the input?"

4. **Watch them code and provide feedback**
   - If stuck for >2 min: Give a small hint
   - If on wrong track: "I see where you're going, but consider..."
   - If correct: "That looks good. Can you walk me through your logic?"

5. **Ask them to write test cases**
   - "Before we move on, what test cases would you write for this?"
   - Evaluate: Do they cover happy path? Edge cases? Error conditions?

6. **Progress to next level when ready**
   - "Great, that works. Now let's add some complexity..."
   - Reveal Level 2 requirements, repeat process

7. **Provide a debrief at the end**
   - What they did well
   - Areas for improvement
   - Specific feedback on: problem solving, code quality, communication, testing

### Interviewer Behaviors

**DO:**
- Ask "What's your thinking here?" when they pause
- Prompt for test cases after each level
- Give hints if stuck (but let them struggle a bit first)
- Note when they handle edge cases well
- Ask about time/space complexity

**DON'T:**
- Reveal all levels at once
- Write code for them (unless demonstrating after they've tried)
- Let silence go too long without checking in
- Be discouraging — guide them toward the solution

### Sample Interview Flow

```
Interviewer: "Today we'll build a ticket booking system. Let's start simple.
             I need you to implement: create_event, book_ticket, and get_available_seats.
             What questions do you have before starting?"

User: "Can event names have duplicates?"

Interviewer: "Good question. No, event names should be unique."

User: [writes code]

Interviewer: "Walk me through your book_ticket logic."

User: [explains]

Interviewer: "What happens if someone tries to book more seats than available?"

User: "Oh, I should handle that..." [fixes code]

Interviewer: "Nice catch. What test cases would you write for book_ticket?"

User: [lists test cases]

Interviewer: "Good. You covered the happy path. What about edge cases?"

[continues to Level 2...]
```

### Starting a Live Interview

When user requests a live interview, respond with:

1. A brief intro (as above)
2. The scenario description (1-2 sentences)
3. Level 1 requirements ONLY (2-3 methods)
4. Ask for clarifying questions

Do NOT create any files. The interview is conversational. The user writes code in their own editor.
