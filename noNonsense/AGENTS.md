# NoNonsense DSA Learning Project

## Project Overview

This is a focused Data Structures and Algorithms (DSA) learning project that emphasizes practical problem-solving over theoretical collection. The project follows a "retriever" approach rather than a "collector" mindset, focusing on mastering core algorithmic patterns through hands-on practice.

## Learning Philosophy

The project implements a structured learning methodology:
- **Pattern.md**: One-page handwritten summaries for daily memorization and re-typing
- **Template files**: Skeleton code with blanks (___) to fill without looking
- **Driver files**: Three problems per pattern (Easy → Medium → Medium+) with pass/fail driver code

## Technology Stack

- **Primary Languages**: Python 3, Java
- **Documentation**: Markdown files
- **Learning Approach**: Pattern-based algorithmic problem solving

## Project Structure

```
noNonsense/
├── guideline.md                    # Main learning methodology and 15 core patterns
├── AGENTS.md                       # This file - project documentation for AI agents
└── 01_two_pointers/                # First pattern module
    ├── notesOnTwoPointer.md       # Learning notes and key concepts
    ├── skeleton.java              # Java template for two-pointer problems
    ├── skeleton.py                # Python template for two-pointer problems
    ├── skeleton.class             # Compiled Java template
    └── practiceQuestions/         # LeetCode problem implementations
        ├── twoSumLeetcode.md
        ├── twoSumTwoSortedLeetcode.md
        ├── reverseString.md
        ├── MoveZeroes.md
        └── validPalindrom.md
```

## Core Algorithmic Patterns

The project covers 15 fundamental algorithmic patterns:

1. **Two Pointers** - Array traversal without extra space
2. **Sliding Window** - Subarray/substring problems  
3. **Fast & Slow Pointers** - LinkedList cycles, mid-finding
4. **Binary Search** - Not just sorted arrays
5. **Merge Intervals** - Calendar/scheduling problems
6. **Cyclic Sort** - O(n) sorting for 1→N range
7. **In-place LinkedList** - Space efficiency
8. **BFS/DFS** - Tree/Graph traversal
9. **Two Heaps** - Median/streams problems
10. **Subsets** - Backtracking pattern
11. **Greedy** - Local → Global optimum
12. **Prefix Sum + HashMap** - Subarray sum problems
13. **Stack** - Next greater/valid parentheses
14. **Dynamic Programming (Tabulation)** - Bottom-up approach
15. **Bit Manipulation** - XOR tricks

## Code Organization

### Template Structure
Each pattern includes skeleton templates in both Java and Python:
- Basic algorithmic structure with placeholder logic
- Standard pointer initialization and movement patterns
- Common edge case handling

### Practice Questions
Each pattern module contains LeetCode problem solutions with:
- Problem statement and requirements
- Algorithm explanation and approach
- Implementation with error analysis
- Key learnings and common mistakes

## Development Conventions

### Code Style Guidelines
- **Internal Logic**: Always use 0-based indexing for algorithmic operations
- **Output**: Convert to required indexing when returning positions
- **Variable Naming**: Use descriptive single letters (i, j for pointers, n for length)
- **Comments**: Focus on algorithmic logic rather than syntax

### Python Conventions
- Use type hints where applicable (List[int], etc.)
- Follow LeetCode class structure for consistency
- Implement in-place modifications when required

### Java Conventions  
- Use standard Java collections (ArrayList, List)
- Include proper imports at the top
- Follow standard Java naming conventions

## Testing Strategy

- **Manual Testing**: Each solution includes test cases with expected outputs
- **LeetCode Validation**: All problems are validated against LeetCode test cases
- **Error Analysis**: Document common mistakes and their solutions
- **Learning Notes**: Track personal mistakes and insights for improvement

## Key Learning Rules

### 4️⃣ Important Rule (Memorize This)
- **Internal logic**: Always 0-based indexing when working with indices
- **Output**: Convert to required indexing when returning positions

### Fundamental Data Structures to Master
- list, dict, set, deque, heapq (Python)
- Control structures: for, while, if-else, def
- Operations: slicing, sorting, lambda functions

## Build and Run Instructions

### Python Files
```bash
python skeleton.py
python practiceQuestions/[problem].py
```

### Java Files
```bash
javac skeleton.java
java skeleton
```

## Current Progress

The project is currently focused on Pattern 1: Two Pointers, with 5 LeetCode problems implemented and documented. Each subsequent pattern will follow the same structure with templates, practice questions, and detailed learning notes.

## Notes for AI Agents

When working with this project:
1. Maintain the existing learning-focused structure
2. Preserve the pattern-based organization
3. Follow the established documentation format for new problems
4. Include error analysis and learning insights
5. Respect the 0-based indexing rule for internal logic
6. Convert to required indexing only in final output/return statements