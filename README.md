# ICA Style Practice Playground

A practice environment for CodeSignal Industry Coding Assessment (ICA) style problems, powered by Claude Code.

## Inspiration

This project was inspired by [PaulLockett/CodeSignal_Practice_Industry_Coding_Framework](https://github.com/PaulLockett/CodeSignal_Practice_Industry_Coding_Framework) — one of the few comprehensive resources for practicing the CodeSignal ICA format. Check it out for additional practice problems and insights into the assessment structure.

## Setup

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) package manager
- [Claude Code](https://claude.ai/claude-code) CLI

### Installation

```bash
# Clone the repository
git clone <repo-url>
cd interview_playground

# Install dependencies
uv sync
```

## Project Structure

```
interview_playground/
├── CLAUDE.md                  # Instructions for Claude Code
├── README.md                  # This file
├── Makefile                   # Test commands
├── pyproject.toml             # Python dependencies
│
└── ica_practice/
    ├── simulation.py          # Main problem file (implement here)
    ├── test_simulation.py     # Test suite by level
    │
    ├── levels/                # Level-specific documentation
    │   ├── LEVEL_1.md
    │   ├── LEVEL_2.md
    │   ├── LEVEL_3.md
    │   └── LEVEL_4.md
    │
    └── mini_problems/         # Smaller focused practice problems
        ├── coffee_shop.py
        ├── task_scheduler.py
        └── ...
```

## Running Tests

Use the Makefile to run tests for each level:

```bash
# Test individual levels
make test-1    # Level 1: Basic Operations
make test-2    # Level 2: Intermediate
make test-3    # Level 3: Aggregation & Reports
make test-4    # Level 4: Advanced Features

# Test all levels
make test-all
```

## How to Practice

### Option 1: Self-Paced Practice

1. Open `ica_practice/levels/LEVEL_1.md` to read the requirements
2. Implement the methods in `ica_practice/simulation.py`
3. Run `make test-1` to check your solution
4. Move to the next level when all tests pass
5. Repeat for levels 2, 3, and 4

**Tip:** Set a 90-minute timer to simulate real ICA conditions.

### Option 2: Mini Problems

For focused practice on specific concepts:

1. Choose a mini problem in `ica_practice/mini_problems/`
2. Read the corresponding `.md` file for requirements
3. Implement the solution
4. Run the appropriate `make test-*` command

## Using Claude Code

This repository is designed to work with Claude Code for generating new problems and running mock interviews.

### Generate a New ICA Problem

Start Claude Code and ask it to create a new problem:

```
> Create a new ICA problem about a restaurant reservation system
```

Claude will generate:

- `simulation.py` with method stubs
- `test_simulation.py` with 40-60 tests
- Four `LEVEL_X.md` files with requirements
- Updated Makefile targets

### Generate a Mini Problem

For smaller, focused practice:

```
> Create a mini problem focusing on priority queues and scheduling
```

### Get Help While Practicing

Ask Claude to explain concepts or give hints:

```
> Explain how to sort by multiple criteria in Python
> Give me a hint for the top_spenders method
> What data structure should I use for FIFO processing?
```

### Run a Mock Interview

For live interview practice (Harvey-style), ask Claude to be your interviewer:

```
> Run a live mock interview with me
```

Claude will:

1. **Introduce the problem** — scenario and Level 1 requirements only
2. **Ask clarifying questions** — evaluate your questions before coding
3. **Watch you code** — provide hints if you get stuck
4. **Request test cases** — ask what tests you would write
5. **Progress through levels** — reveal each level as you complete the previous
6. **Debrief at the end** — feedback on problem solving, code quality, and communication

**Important:** During a mock interview, Claude will NOT reveal all levels upfront. This simulates a real interview where requirements are given incrementally.

## ICA Format Overview

The CodeSignal Industry Coding Assessment (ICA) format:

| Aspect      | Details                                       |
| ----------- | --------------------------------------------- |
| Time        | 90 minutes                                    |
| Structure   | 1 problem, 4 progressive levels               |
| Scoring     | 200-600 points                                |
| Expectation | You are NOT expected to complete all 4 levels |

### Level Breakdown

| Level | Time Estimate | Typical Features                         |
| ----- | ------------- | ---------------------------------------- |
| 1     | 10-15 min     | Create, read, basic validation           |
| 2     | 20-30 min     | Relationships between entities           |
| 3     | 30-60 min     | History, reports, sorting, top-N         |
| 4     | 30-60 min     | Scheduling, dependencies, advanced logic |

## Core Concepts to Know

### Data Structures

- `dict` — lookups, counting, tracking state
- `set` — duplicate detection, O(1) membership
- `list` — ordered storage, iteration
- `deque` — FIFO queues
- `heapq` — priority queues

### Common Patterns

```python
# Counting
counts[key] = counts.get(key, 0) + 1

# Sorting with multiple criteria (descending score, ascending name)
sorted(items, key=lambda x: (-x[1], x[0]))

# FIFO Queue
from collections import deque
queue = deque()
queue.append(item)
item = queue.popleft()

# Integer division for percentages
result = (amount * percent) // 100
```

## Tips for Success

1. **Read requirements carefully** before coding
2. **Handle edge cases** — empty input, zero, negative, duplicates
3. **Test incrementally** — run tests after each level
4. **Think about data structures** upfront — they affect later levels
5. **Don't optimize prematurely** — get it working first

## Contributing

To add new problems:

1. Follow the templates in `CLAUDE.md`
2. Create all required files (simulation, tests, level READMEs)
3. Update the Makefile with test targets
4. Test that all levels are solvable

## License

MIT
