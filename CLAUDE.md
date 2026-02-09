# Claude Code Instructions: ICA Practice Problem Generator

This repository generates CodeSignal ICA-style practice problems that test **data structure and algorithm knowledge**, not just CRUD operations.

## Core Philosophy

**Real ICAs are "narrow but deep":**

- Few methods per level (2-3), but each requires careful DSA choices
- Implicit or explicit time complexity constraints that force specific data structures
- Level 1 data structure choice determines success in Level 4

**Anti-patterns to avoid:**

- ❌ 5+ simple dictionary operations per level
- ❌ Methods that can all be solved with `dict` + basic loops
- ❌ No performance requirements

**Patterns to adhear to:**

- ✅ 2-3 methods that require binary search, tries, heaps, etc.
- ✅ Explicit O(log n) or O(1) requirements
- ✅ Level 1 setup that makes Level 4 possible (or impossible if wrong)

## Repository Structure

```
code/
├── simulation.py              # Main solution file (class with method stubs)
├── test_simulation.py         # Test suite organized by level
├── levels/
│   ├── LEVEL_1.md             # Level 1 requirements
│   ├── LEVEL_2.md             # Level 2 requirements
│   ├── LEVEL_3.md             # Level 3 requirements
│   └── LEVEL_4.md             # Level 4 requirements
```

## Problem Archetypes (Choose One)

Each archetype has a **forcing function**: a constraint that makes naive solutions fail.

**16 archetypes covering common ICA patterns:**

| #   | Archetype                | Core DSA                              | Forcing Function                              |
| --- | ------------------------ | ------------------------------------- | --------------------------------------------- |
| 1   | Time-Series KV Store     | Binary search (`bisect`)              | `get(key, timestamp)` floor query in O(log n) |
| 2   | Filesystem Paths         | Trie                                  | `find(prefix)` in O(prefix + results)         |
| 3   | Task Scheduler           | Heap + Graph                          | Dependencies + priorities combined            |
| 4   | LRU Cache                | OrderedDict / DLL                     | O(1) get/put with recency tracking            |
| 5   | Range Queries            | Sorted list + bisect                  | `query_overlap()` better than O(n)            |
| 6   | Autocomplete             | Trie + Heap                           | `suggest(prefix, k)` top-k by frequency       |
| 7   | Leaderboard              | SortedList                            | `get_rank()` in O(log n)                      |
| 8   | Rate Limiter             | Deque + bisect                        | Sliding window in O(log n)                    |
| 9   | Banking System           | Dict + Heap + Log                     | Atomic transfers, rollback, top-k activity    |
| 10  | KV with Scans            | Trie or sorted keys + secondary index | Prefix scan + value range scan                |
| 11  | Constrained Cache        | LRU/LFU + inverted index              | Size-based eviction + tag queries             |
| 12  | Cloud Database           | Consistent hashing                    | `add_node()` without full redistribution      |
| 13  | Inventory + Reservations | Dict + expiration queue               | Atomic bundle reserve, TTL expiration         |
| 14  | Message Queue            | Deque + state machine                 | ack/nack with timeout redelivery              |
| 15  | Package Manager          | Graph + topological sort              | Cycle detection, install order                |
| 16  | Web Crawler              | BFS + Set + Deque + Threading         | Domain restriction, async/concurrent fetching |

---

## Level Design Guidelines

| Level | Time      | Methods | Complexity                | What's Tested                         |
| ----- | --------- | ------- | ------------------------- | ------------------------------------- |
| 1     | 15-20 min | 2-4     | O(log n) or O(1) required | Core data structure choice            |
| 2     | 20-25 min | 2-3     | Builds on L1 structure    | Extending the data structure          |
| 3     | 25-30 min | 1-2     | O(log n) compound ops     | Combining operations correctly        |
| 4     | 25-30 min | 1-2     | Full system complexity    | Edge cases, cleanup, advanced queries |

**Total: 6-12 methods across all levels** (not 15-20)

## File Generation

### simulation.py Template

```python
from typing import Optional, List


class [SystemName]:
    """
    [One-line description]

    Performance requirements:
    - [method1]: O(log n) / O(1)
    - [method2]: O(log n) / O(k) where k is result size
    """

    def __init__(self):
        """Initialize the system."""
        pass
```

**IMPORTANT:**

- Class docstring should mention performance requirements
- No method stubs — let each LEVEL.md introduce methods
- No hints about data structures

### test_simulation.py Guidelines

- **8-12 tests per level** (not 15+)
- **Include performance-forcing tests:**
  ```python
  def test_level_1_large_dataset_performance(self):
      """Should handle 10,000 operations efficiently."""
      for i in range(10000):
          system.add(f"key_{i}", i, i)
      # This would timeout with O(n) implementation
      result = system.get("key_5000", 5000)
      assert result == 5000
  ```
- Test edge cases for the specific DSA:
  - Binary search: exact match vs. floor value
  - Trie: empty prefix, single char, overlapping prefixes
  - Heap: ties in priority, empty heap

**IMPORTANT!:**

- Ensure the level is included in the unit test. So for level one, create names like `def test_level_1_<unit_test>(self):`
- Ensure the existing `makefile` commands run the unit tests properly. See file below.

  ```makefile
  .PHONY: test-1 test-2 test-3 test-4 test-all

  test-1:
     uv run pytest code/test_simulation.py -k "level_1" -v

  test-2:
     uv run pytest code/test_simulation.py -k "level_1 or level_2" -v

  test-3:
     uv run pytest code/test_simulation.py -k "level_1 or level_2 or level_3" -v

  test-4:
     uv run pytest code/test_simulation.py -k "level_1 or level_2 or level_3 or level_4" -v

  test-all:
     uv run pytest code/test_simulation.py -v
  ```

### LEVEL_X.md Template

```markdown
# Level X: [Feature Name]

**Time Estimate:** XX-XX minutes  
**Methods to Implement:** X

## Overview

[What this level adds and WHY it's challenging]

## Performance Requirements

| Method        | Time Complexity | Space Complexity |
| ------------- | --------------- | ---------------- |
| `method_name` | O(log n)        | O(1)             |

## Methods

### `method_name(arg1: type, arg2: type) -> return_type`

[2-3 sentence description]

**Behavior:**

- [Key behavior 1]
- [Key behavior 2]
- Returns `X` if [condition]

**Examples:**
| Input | Output | Explanation |
|-------|--------|-------------|
| `method("a", 5)` | `True` | [why] |
| `method("b", -1)` | `False` | [edge case] |

---

## Run Tests

\`\`\`bash
make test-X
\`\`\`
```

**DO NOT include:**

- Hints about which data structure to use
- Implementation suggestions
- "Consider using X" comments

## DSA Patterns Candidates Must Know

### Binary Search (bisect module)

```python
import bisect

# Find insertion point (leftmost)
idx = bisect.bisect_left(sorted_list, target)

# Find value at or before target (floor)
idx = bisect.bisect_right(timestamps, target) - 1
if idx >= 0:
    return values[idx]

# Insert while maintaining sort
bisect.insort(sorted_list, value)
```

### Trie

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.data = None  # Store associated data

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path: str, data=None):
        node = self.root
        for char in path:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.data = data

    def find_prefix(self, prefix: str) -> List[str]:
        """Return all strings starting with prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        # DFS from this node to collect all endings
        results = []
        self._collect(node, prefix, results)
        return results
```

### Heap with Custom Priority

```python
import heapq

# Min-heap (negate for max-heap)
heap = []
heapq.heappush(heap, (priority, tiebreaker, item))
priority, _, item = heapq.heappop(heap)

# Lazy deletion pattern
while heap and heap[0][2] in deleted_set:
    heapq.heappop(heap)
```

### OrderedDict for LRU

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

### SortedList for Ranking

```python
from sortedcontainers import SortedList

sl = SortedList()
sl.add((score, player_id))
rank = len(sl) - sl.bisect_left((score, player_id))  # 1-indexed from top
```

### Deque for Sliding Window

```python
from collections import deque

window = deque()
# Add with timestamp
window.append((timestamp, value))
# Remove expired (older than cutoff)
while window and window[0][0] < cutoff:
    window.popleft()
```

### Atomic Transactions (All-or-Nothing)

```python
def transfer(self, from_id, to_id, amount):
    # Validate BEFORE modifying anything
    if from_id not in self.accounts or to_id not in self.accounts:
        return False
    if self.accounts[from_id] < amount:
        return False

    # Only modify after all validation passes
    self.accounts[from_id] -= amount
    self.accounts[to_id] += amount

    # Log for rollback capability
    tx_id = self.next_tx_id
    self.next_tx_id += 1
    self.tx_log[tx_id] = ('transfer', from_id, to_id, amount)
    return tx_id

def rollback(self, tx_id):
    if tx_id not in self.tx_log:
        return False
    tx_type, *args = self.tx_log[tx_id]
    if tx_type == 'transfer':
        from_id, to_id, amount = args
        # Reverse the operation
        self.accounts[to_id] -= amount
        self.accounts[from_id] += amount
    del self.tx_log[tx_id]
    return True
```

### Inverted Index (Tag → Items)

```python
class TaggedCache:
    def __init__(self):
        self.items = {}  # filename → (size, tags)
        self.tag_index = defaultdict(set)  # tag → set of filenames

    def put(self, filename, size, tags):
        # Remove old tags if updating
        if filename in self.items:
            old_tags = self.items[filename][1]
            for tag in old_tags:
                self.tag_index[tag].discard(filename)

        # Add new entry
        self.items[filename] = (size, tags)
        for tag in tags:
            self.tag_index[tag].add(filename)

    def get_by_tag(self, tag):
        return list(self.tag_index.get(tag, set()))

    def delete(self, filename):
        if filename not in self.items:
            return False
        _, tags = self.items[filename]
        for tag in tags:
            self.tag_index[tag].discard(filename)
        del self.items[filename]
        return True
```

### Lazy TTL Expiration

```python
class TTLStore:
    def __init__(self):
        self.data = {}  # key → (value, expires_at)

    def set_with_ttl(self, key, value, ttl, current_time):
        expires_at = current_time + ttl
        self.data[key] = (value, expires_at)

    def get(self, key, current_time):
        if key not in self.data:
            return None
        value, expires_at = self.data[key]
        if current_time >= expires_at:
            # Lazy expiration: delete on access
            del self.data[key]
            return None
        return value

    def cleanup(self, current_time):
        """Eager cleanup - call periodically or when memory pressure."""
        expired = [k for k, (v, exp) in self.data.items() if current_time >= exp]
        for k in expired:
            del self.data[k]
        return len(expired)
```

### Consistent Hashing (Simplified)

```python
import bisect
import hashlib

class ConsistentHash:
    def __init__(self, nodes=None, virtual_nodes=100):
        self.virtual_nodes = virtual_nodes
        self.ring = []  # Sorted list of (hash, node_id)
        self.ring_hashes = []  # Just hashes for bisect
        self.nodes = set()

        for node in (nodes or []):
            self.add_node(node)

    def _hash(self, key):
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def add_node(self, node_id):
        self.nodes.add(node_id)
        for i in range(self.virtual_nodes):
            h = self._hash(f"{node_id}:{i}")
            idx = bisect.bisect(self.ring_hashes, h)
            self.ring_hashes.insert(idx, h)
            self.ring.insert(idx, (h, node_id))

    def get_node(self, key):
        if not self.ring:
            return None
        h = self._hash(key)
        idx = bisect.bisect(self.ring_hashes, h) % len(self.ring)
        return self.ring[idx][1]
```

### Topological Sort with Cycle Detection

```python
def topological_sort(self, start_node):
    """Returns nodes in dependency order, or raises if cycle exists."""
    UNVISITED, IN_PROGRESS, COMPLETED = 0, 1, 2
    state = defaultdict(int)
    result = []

    def dfs(node):
        if state[node] == COMPLETED:
            return True
        if state[node] == IN_PROGRESS:
            return False  # Cycle detected

        state[node] = IN_PROGRESS
        for neighbor in self.graph.get(node, []):
            if not dfs(neighbor):
                return False

        state[node] = COMPLETED
        result.append(node)
        return True

    if not dfs(start_node):
        raise ValueError("Cycle detected")

    return result  # Dependencies come first

# Kahn's Algorithm (BFS alternative)
def kahn_topological_sort(self, nodes):
    in_degree = defaultdict(int)
    for node in nodes:
        for dep in self.graph.get(node, []):
            in_degree[node]  # Ensure exists
            in_degree[dep] += 1

    queue = deque([n for n in nodes if in_degree[n] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in self.reverse_graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(nodes):
        raise ValueError("Cycle detected")
    return result
```

### Message Queue State Machine

```python
from enum import Enum
from collections import deque, defaultdict

class MessageState(Enum):
    PENDING = 1
    IN_FLIGHT = 2
    ACKED = 3

class MessageQueue:
    def __init__(self):
        self.queues = defaultdict(deque)  # topic → deque of message_ids
        self.messages = {}  # message_id → (topic, payload, state, consumed_at)
        self.next_id = 0

    def publish(self, topic, payload):
        msg_id = self.next_id
        self.next_id += 1
        self.messages[msg_id] = (topic, payload, MessageState.PENDING, None)
        self.queues[topic].append(msg_id)
        return msg_id

    def consume(self, topic, current_time):
        self._requeue_expired(topic, current_time)

        if not self.queues[topic]:
            return None

        msg_id = self.queues[topic].popleft()
        topic, payload, _, _ = self.messages[msg_id]
        self.messages[msg_id] = (topic, payload, MessageState.IN_FLIGHT, current_time)
        return msg_id, payload

    def ack(self, msg_id):
        if msg_id not in self.messages:
            return False
        topic, payload, state, _ = self.messages[msg_id]
        if state != MessageState.IN_FLIGHT:
            return False
        self.messages[msg_id] = (topic, payload, MessageState.ACKED, None)
        return True

    def nack(self, msg_id):
        """Return message to queue for reprocessing."""
        if msg_id not in self.messages:
            return False
        topic, payload, state, _ = self.messages[msg_id]
        if state != MessageState.IN_FLIGHT:
            return False
        self.messages[msg_id] = (topic, payload, MessageState.PENDING, None)
        self.queues[topic].appendleft(msg_id)  # Front of queue
        return True
```

### Web Crawler - BFS with Visited Set

```python
from collections import deque
from urllib.parse import urlparse, urldefrag

class WebCrawler:
    def crawl(self, seed_url: str) -> set:
        """Basic BFS crawl returning all reachable URLs."""
        visited = set()
        queue = deque([seed_url])

        while queue:
            url = queue.popleft()
            normalized = self._normalize(url)

            if normalized in visited:
                continue
            visited.add(normalized)

            # get_links is provided by the framework
            for link in get_links(url):
                if self._normalize(link) not in visited:
                    queue.append(link)

        return visited

    def _normalize(self, url: str) -> str:
        """Remove fragments and normalize URL."""
        url_without_fragment, _ = urldefrag(url)
        # Remove trailing slash for consistency
        return url_without_fragment.rstrip('/')

    def _get_domain(self, url: str) -> str:
        """Extract domain from URL."""
        parsed = urlparse(url)
        return parsed.netloc.lower()

    def crawl_same_domain(self, seed_url: str) -> set:
        """Only crawl URLs on the same domain as seed."""
        seed_domain = self._get_domain(seed_url)
        visited = set()
        queue = deque([seed_url])

        while queue:
            url = queue.popleft()
            normalized = self._normalize(url)

            if normalized in visited:
                continue
            if self._get_domain(url) != seed_domain:
                continue  # Skip external links

            visited.add(normalized)

            for link in get_links(url):
                if self._normalize(link) not in visited:
                    queue.append(link)

        return visited
```

### Web Crawler - Concurrent with Thread Safety

```python
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from urllib.parse import urlparse, urldefrag

class ConcurrentWebCrawler:
    def __init__(self):
        self.visited = set()
        self.visited_lock = Lock()
        self.results = set()
        self.results_lock = Lock()

    def crawl_concurrent(self, seed_url: str, max_workers: int = 4) -> set:
        """Thread-safe concurrent crawling."""
        seed_domain = self._get_domain(seed_url)

        with self.visited_lock:
            self.visited.add(self._normalize(seed_url))

        to_crawl = [seed_url]

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            while to_crawl:
                # Submit batch of URLs to crawl
                futures = {
                    executor.submit(self._fetch_links, url, seed_domain): url
                    for url in to_crawl
                }
                to_crawl = []

                for future in as_completed(futures):
                    new_links = future.result()
                    for link in new_links:
                        normalized = self._normalize(link)
                        with self.visited_lock:
                            if normalized not in self.visited:
                                self.visited.add(normalized)
                                to_crawl.append(link)

        return self.visited

    def _fetch_links(self, url: str, allowed_domain: str) -> list:
        """Fetch URL and return valid links (thread-safe)."""
        with self.results_lock:
            self.results.add(self._normalize(url))

        links = get_links(url)  # Provided helper
        return [
            link for link in links
            if self._get_domain(link) == allowed_domain
        ]

    def _normalize(self, url: str) -> str:
        url_without_fragment, _ = urldefrag(url)
        return url_without_fragment.rstrip('/')

    def _get_domain(self, url: str) -> str:
        return urlparse(url).netloc.lower()
```

### Web Crawler - With Depth Limit and Rate Limiting

```python
import time
from collections import deque
from threading import Lock

class RateLimitedCrawler:
    def __init__(self):
        self.last_request_time = 0
        self.rate_lock = Lock()

    def crawl_with_limits(
        self,
        seed_url: str,
        max_depth: int,
        requests_per_second: float
    ) -> set:
        """Crawl with depth limit and rate limiting."""
        min_interval = 1.0 / requests_per_second
        visited = set()
        # Queue holds (url, depth)
        queue = deque([(seed_url, 0)])
        seed_domain = self._get_domain(seed_url)

        while queue:
            url, depth = queue.popleft()
            normalized = self._normalize(url)

            if normalized in visited:
                continue
            if depth > max_depth:
                continue
            if self._get_domain(url) != seed_domain:
                continue

            # Rate limiting
            self._wait_for_rate_limit(min_interval)

            visited.add(normalized)

            # Only queue children if we haven't hit max depth
            if depth < max_depth:
                for link in get_links(url):
                    if self._normalize(link) not in visited:
                        queue.append((link, depth + 1))

        return visited

    def _wait_for_rate_limit(self, min_interval: float):
        """Ensure minimum time between requests."""
        with self.rate_lock:
            now = time.time()
            elapsed = now - self.last_request_time
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            self.last_request_time = time.time()

    def _normalize(self, url: str) -> str:
        from urllib.parse import urldefrag
        url_without_fragment, _ = urldefrag(url)
        return url_without_fragment.rstrip('/')

    def _get_domain(self, url: str) -> str:
        from urllib.parse import urlparse
        return urlparse(url).netloc.lower()
```

## Quality Checklist

Before finalizing a problem, verify:

- [ ] **Total methods across all levels: 6-8** (not more)
- [ ] **Level 1 requires non-trivial DSA** (not just dict)
- [ ] **Explicit time complexity in requirements** (O(log n), O(1), etc.)
- [ ] **Tests include large dataset cases** that would timeout naive solutions
- [ ] **Each level has 2-3 methods max**
- [ ] **No hints about data structures** in any file
- [ ] **Problem archetype is clearly defined** (time-series, trie-based, etc.)

## Live Interview Mode

When user requests "live interview" or "mock interview":

### Setup

1. **Choose an archetype** and present only the scenario + Level 1
2. **State performance requirements explicitly:**
   > "Your `get(key, timestamp)` method needs to run in O(log n) time. There will be up to 100,000 entries per key."
3. **Ask:** "Before coding, what data structure are you thinking of using, and why?"

### During Interview

- **If they choose dict + linear scan:**
  > "That would work for correctness. What's the time complexity? The requirement is O(log n)."
- **If stuck on DSA choice (>3 min):**
  > "What operations do you need to support? Is there a data structure that gives you O(log n) lookup on sorted data?"
- **After they implement Level 1:**
  > "Walk me through how your data structure handles [edge case]. Now let's add Level 2..."

### What to Evaluate

1. **Data structure choice** — Did they recognize what was needed?
2. **Edge case handling** — Empty inputs, exact matches, boundaries
3. **Code clarity** — Is the DSA implemented cleanly?
4. **Complexity awareness** — Can they state the Big-O?

### Debrief Template

```
**What went well:**
- [DSA recognition, clean code, etc.]

**Areas to improve:**
- [Missed edge case, suboptimal structure, etc.]

**Key takeaway:**
- This problem required [X data structure] because [reason].
- Practice: [specific LeetCode problems or concepts]
```

## Example Problem: Time-Series KV Store

### Scenario (given to candidate)

> "Design a time-series key-value store. Each key can have multiple values at different timestamps. You need to retrieve the value at or before a given timestamp efficiently."

### Level 1 (15-20 min)

```python
def set(self, key: str, value: int, timestamp: int) -> None
def get(self, key: str, timestamp: int) -> Optional[int]
```

- `get` returns the value with the largest timestamp ≤ given timestamp
- **Requirement: O(log n) per operation**

### Level 2 (20-25 min)

```python
def get_range(self, key: str, start_ts: int, end_ts: int) -> List[int]
```

- Returns all values where `start_ts <= timestamp <= end_ts`
- **Requirement: O(log n + k)** where k is result size

### Level 3 (25-30 min)

```python
def delete_before(self, key: str, timestamp: int) -> int
```

- Removes all entries with timestamp < given timestamp
- Returns count of deleted entries
- **Requirement: O(log n + deleted)**

### Level 4 (25-30 min)

```python
def compact(self, max_entries: int) -> int
```

- For each key, keep only the most recent `max_entries` values
- Returns total count of deleted entries
- **Requirement: O(total_keys × log n)**
