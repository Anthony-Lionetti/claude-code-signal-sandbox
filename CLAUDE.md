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

**15 archetypes covering common ICA patterns:**

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

### 1. Time-Series Key-Value Store

**Forcing function:** `get(key, timestamp)` must return value at or before timestamp in O(log n)

| Level | Methods                                                   | DSA Required                                      |
| ----- | --------------------------------------------------------- | ------------------------------------------------- |
| 1     | `set(key, value, timestamp)`, `get(key, timestamp)`       | Binary search on sorted timestamps per key        |
| 2     | `get_range(key, t_start, t_end)` → list of values         | Binary search for range bounds                    |
| 3     | `delete_before(key, timestamp)`                           | Efficient deletion while maintaining sorted order |
| 4     | `compact(max_entries_per_key)` keeping only most recent N | Merge/cleanup across all keys                     |

**Why it's hard:** Naive dict-of-lists requires O(n) scan. Must use `bisect` module or maintain sorted structure.

---

### 2. Filesystem with Path Operations

**Forcing function:** `list_files(prefix)` and `autocomplete(partial_path)` in O(k) where k = results

| Level | Methods                                         | DSA Required             |
| ----- | ----------------------------------------------- | ------------------------ |
| 1     | `create(path)`, `exists(path)`                  | Trie structure for paths |
| 2     | `list(directory)` → immediate children          | Trie traversal           |
| 3     | `find(prefix)` → all paths starting with prefix | DFS from trie node       |
| 4     | `delete(path)` with cascade, `move(src, dst)`   | Subtrie manipulation     |

**Why it's hard:** Naive dict requires O(n) prefix scan. Trie gives O(prefix_len + results).

---

### 3. Task Scheduler with Dependencies

**Forcing function:** `get_next_task()` must respect dependencies and priorities in O(log n)

| Level | Methods                                         | DSA Required                          |
| ----- | ----------------------------------------------- | ------------------------------------- |
| 1     | `add_task(id, priority)`, `get_next_task()`     | Heap for priority queue               |
| 2     | `add_dependency(task_id, depends_on_id)`        | Graph + in-degree tracking            |
| 3     | `complete_task(id)` → unblocks dependents       | Update heap when dependencies resolve |
| 4     | `get_execution_order()` → full topological sort | Kahn's algorithm or DFS               |

**Why it's hard:** Must combine heap (priority) with graph (dependencies). Neither alone works.

---

### 4. LRU Cache with Expiration

**Forcing function:** `get()` and `put()` must be O(1), TTL expiration on access

| Level | Methods                                         | DSA Required                                |
| ----- | ----------------------------------------------- | ------------------------------------------- |
| 1     | `put(key, value)`, `get(key)` with LRU eviction | OrderedDict or HashMap + Doubly Linked List |
| 2     | Add `capacity` limit, evict least recent        | Move-to-end on access                       |
| 3     | Add `ttl` parameter, expire on access           | Store timestamps, check on get              |
| 4     | `cleanup()` batch removal of expired, `stats()` | Iterate without breaking O(1) ops           |

**Why it's hard:** Dict alone can't track recency order. List alone can't do O(1) lookup.

---

### 5. Range Query System (Interval-based)

**Forcing function:** `query_overlap(start, end)` must be better than O(n)

| Level | Methods                                                 | DSA Required                                  |
| ----- | ------------------------------------------------------- | --------------------------------------------- |
| 1     | `add_interval(id, start, end)`, `point_query(x)`        | Sorted list + binary search, or interval tree |
| 2     | `query_overlap(start, end)` → all overlapping intervals | Efficient range search                        |
| 3     | `remove_interval(id)`                                   | Maintain sorted structure                     |
| 4     | `merge_overlapping()` → consolidate intervals           | Sweep line algorithm                          |

**Why it's hard:** Naive O(n) scan fails for large datasets. Need sorted structure or tree.

---

### 6. Autocomplete / Search Suggestions

**Forcing function:** `suggest(prefix, k)` must return top-k by frequency in O(prefix + k log k)

| Level | Methods                                            | DSA Required                     |
| ----- | -------------------------------------------------- | -------------------------------- |
| 1     | `record(word)`, `suggest(prefix)` → all matches    | Trie with word storage           |
| 2     | Track frequency, return sorted by frequency        | Store counts at trie nodes       |
| 3     | `suggest(prefix, k)` → top k only                  | Heap for top-k selection         |
| 4     | `delete(word)`, `suggest_fuzzy(prefix, max_edits)` | Trie manipulation, edit distance |

---

### 7. Leaderboard / Ranking System

**Forcing function:** `get_rank(player_id)` must be O(log n), not O(n)

| Level | Methods                                       | DSA Required                                |
| ----- | --------------------------------------------- | ------------------------------------------- |
| 1     | `add_score(player_id, score)`, `top_k(k)`     | Heap or sorted structure                    |
| 2     | `get_rank(player_id)` → 1-indexed rank        | Need ordered set with indexing (SortedList) |
| 3     | `get_players_in_range(min_rank, max_rank)`    | Range query on sorted structure             |
| 4     | `reset_scores()`, `get_percentile(player_id)` | Maintain count for percentile calc          |

**Why it's hard:** Dict gives O(n) rank lookup. Need `sortedcontainers.SortedList` or similar.

---

### 8. Rate Limiter

**Forcing function:** `is_allowed(user_id, timestamp)` in O(log n) with sliding window

| Level | Methods                                            | DSA Required                        |
| ----- | -------------------------------------------------- | ----------------------------------- |
| 1     | `is_allowed(user_id, timestamp)` with fixed window | Dict + deque per user               |
| 2     | Sliding window (last N seconds)                    | Binary search to remove old entries |
| 3     | Multiple rate limits (e.g., 10/min AND 100/hour)   | Multiple windows per user           |
| 4     | `get_stats(user_id)` → usage patterns              | Efficient aggregation               |

---

### 9. Banking / Transaction System

**Forcing function:** `transfer()` must be atomic, `get_top_k_by_activity()` in O(k log k), `rollback()` requires transaction log

| Level | Methods                                                                        | DSA Required                                               |
| ----- | ------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| 1     | `create_account(id)`, `deposit(id, amount)`, `withdraw(id, amount)` → bool     | Dict with validation (overdraft protection)                |
| 2     | `transfer(from_id, to_id, amount)` → bool, `get_balance(id)`                   | Atomic operations (both succeed or both fail)              |
| 3     | `get_top_k_by_activity(k)` → list of (id, tx_count), `get_history(id)`         | Heap for top-k, transaction log per account                |
| 4     | `rollback(transaction_id)` → bool, `schedule_transfer(from, to, amount, time)` | Transaction IDs, scheduled queue with timestamp processing |

**Why it's hard:**

- Level 2: Transfer must handle insufficient funds atomically (don't deduct if deposit fails)
- Level 3: Naive sort is O(n log n); heap gives O(n + k log k)
- Level 4: Rollback requires storing enough state to reverse; scheduled transfers need time-based processing

---

### 10. In-Memory KV Database with Scans

**Forcing function:** `scan(prefix)` in O(prefix + results), `scan_by_value_range()` requires secondary index

| Level | Methods                                                                | DSA Required                                  |
| ----- | ---------------------------------------------------------------------- | --------------------------------------------- |
| 1     | `set(key, value)`, `get(key)`, `delete(key)`                           | Dict for O(1) basic ops                       |
| 2     | `scan(prefix)` → all keys starting with prefix, `keys()`               | Trie for prefix scan OR sorted keys + bisect  |
| 3     | `set_with_ttl(key, value, ttl)`, `get(key, current_time)`              | Lazy expiration + optional cleanup structure  |
| 4     | `scan_by_value_range(min_val, max_val)` → keys where min ≤ value ≤ max | Secondary index (sorted by value) with bisect |

**Why it's hard:**

- Level 2: Dict keys don't support prefix scan efficiently; need trie or sorted structure
- Level 3: TTL requires timestamp tracking; lazy vs eager expiration tradeoff
- Level 4: Secondary index is a separate sorted structure mapping value→keys

**Key insight:** This is different from Time-Series KV — here we're scanning by key prefix and value ranges, not by timestamp.

---

### 11. Constrained File Cache

**Forcing function:** `put()` with size-based eviction in O(log n), `get_files_by_tag()` requires inverted index

| Level | Methods                                                                                            | DSA Required                                 |
| ----- | -------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| 1     | `put(filename, size)`, `get(filename)` → size, cache has `max_capacity`                            | Dict + track total size, LRU or LFU eviction |
| 2     | `put(filename, size, tags: List[str])`, `get_files_by_tag(tag)`                                    | Inverted index: tag → set of filenames       |
| 3     | `evict_lru(bytes_needed)` → list of evicted files, `pin(filename)` (pinned files can't be evicted) | Separate tracking for pinned vs unpinned     |
| 4     | `get_stats()` → hit rate, miss rate, `defragment()` → compact by removing gaps                     | Access tracking, size management             |

**Why it's hard:**

- Level 1: Must track total size and evict when full; eviction order matters
- Level 2: Inverted index for tag lookups; must update index on eviction
- Level 3: Pinned files complicate eviction; may need to skip pinned items
- Level 4: Hit/miss tracking requires counting gets; defragment is conceptual reorganization

**Eviction policies to know:**

- **LRU:** Evict least recently used (OrderedDict)
- **LFU:** Evict least frequently used (dict + heap or frequency buckets)
- **Size-based:** Evict largest or smallest first (heap by size)

---

### 12. Cloud Database Simulation (Distributed KV)

**Forcing function:** `get()` with consistency levels, `rebalance()` requires consistent hashing understanding

| Level | Methods                                                                             | DSA Required                                         |
| ----- | ----------------------------------------------------------------------------------- | ---------------------------------------------------- |
| 1     | `put(key, value)`, `get(key)`, data distributed across N nodes via `hash(key) % N`  | Dict per node, hash-based routing                    |
| 2     | `add_node()`, `remove_node()` with key redistribution                               | Track which keys moved; naive rehash is O(all keys)  |
| 3     | `put_with_replication(key, value, replicas=3)`, `get_with_quorum(key, min_nodes=2)` | Replicate to N consecutive nodes; read from multiple |
| 4     | `get_node_stats()` → keys per node, `simulate_failure(node_id)` → reroute reads     | Handle node failures gracefully, detect hot spots    |

**Why it's hard:**

- Level 2: Adding/removing nodes with simple modulo causes massive redistribution; consistent hashing minimizes movement
- Level 3: Replication means writes go to multiple nodes; quorum reads check consistency
- Level 4: Failure handling requires fallback routing

**Consistent Hashing insight:**

```python
# Simple modulo (bad): adding node moves ~100% of keys
node = hash(key) % num_nodes

# Consistent hashing (good): adding node moves ~1/N of keys
# Use a ring with virtual nodes
```

---

### 13. Inventory Management with Reservations

**Forcing function:** `reserve()` must be atomic with expiration, `fulfill()` must respect reservation time

| Level | Methods                                                                                                        | DSA Required                                        |
| ----- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| 1     | `add_item(sku, quantity)`, `get_quantity(sku)` → available count                                               | Dict with quantity tracking                         |
| 2     | `reserve(sku, quantity, reservation_id)` → bool, `cancel_reservation(reservation_id)`                          | Separate reserved vs available counts               |
| 3     | `reserve_with_expiry(sku, qty, res_id, expires_at)`, `fulfill(reservation_id, current_time)`                   | Expiration queue, process expired before operations |
| 4     | `get_low_stock(threshold)` → list of skus, `reserve_bundle([(sku, qty), ...], res_id)` → bool (all or nothing) | Bundle atomicity: all items must be available       |

**Why it's hard:**

- Level 2: Must track `total`, `reserved`, `available` where `available = total - reserved`
- Level 3: Expired reservations must return to available stock; need timestamp-ordered processing
- Level 4: Bundle reservation is atomic — if any item lacks stock, entire reservation fails

---

### 14. Message Queue System

**Forcing function:** `consume()` must be O(1), `ack/nack` with redelivery requires careful state management

| Level | Methods                                                                                            | DSA Required                                       |
| ----- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| 1     | `publish(topic, message)`, `consume(topic)` → message or None                                      | Dict of deques per topic                           |
| 2     | `consume(topic)` returns message_id, `ack(message_id)`, `nack(message_id)` → requeue               | Track in-flight messages separately                |
| 3     | `consume_with_timeout(topic, timeout, current_time)` → auto-nack if not acked                      | Timestamp tracking for in-flight, expiration check |
| 4     | `create_consumer_group(group_id, topic)`, `consume_group(group_id)` → round-robin across consumers | Partition messages across group members            |

**Why it's hard:**

- Level 2: Messages move from "pending" to "in-flight" to "acked"; nack puts back in pending
- Level 3: Must track when each message was consumed; auto-expire on timeout
- Level 4: Consumer groups require fair distribution and handling consumer failures

---

### 15. Package Manager / Dependency Resolver

**Forcing function:** `install(package)` must resolve transitive dependencies, detect cycles in O(V+E)

| Level | Methods                                                                                               | DSA Required                                 |
| ----- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| 1     | `register(package, dependencies: List[str])`, `is_registered(package)`                                | Dict storing adjacency list                  |
| 2     | `install(package)` → list of packages in install order                                                | Topological sort (DFS or Kahn's algorithm)   |
| 3     | `install(package)` returns False if cycle detected, `uninstall(package)` removes if no dependents     | Cycle detection, reverse dependency tracking |
| 4     | `register_with_version(pkg, version, deps: List[(pkg, version_constraint)])`, `install(pkg, version)` | Version comparison, constraint satisfaction  |

**Why it's hard:**

- Level 2: Must return correct install order (dependencies before dependents)
- Level 3: Cycle detection during topological sort; reverse deps for safe uninstall
- Level 4: Version constraints (>=1.0, <2.0) require parsing and comparison

**Topological sort pattern:**

```python
def install_order(self, package):
    visited = set()
    result = []
    temp_mark = set()  # For cycle detection

    def dfs(pkg):
        if pkg in temp_mark:
            raise CycleError()
        if pkg in visited:
            return
        temp_mark.add(pkg)
        for dep in self.dependencies[pkg]:
            dfs(dep)
        temp_mark.remove(pkg)
        visited.add(pkg)
        result.append(pkg)

    dfs(package)
    return result  # Dependencies come before dependents
```

---

### 16. Web Crawler

**Forcing function:** `crawl()` must handle cycles (visited set), `crawl_concurrent()` must be thread-safe, domain filtering in O(1)

| Level | Methods                                                                                | DSA Required                           |
| ----- | -------------------------------------------------------------------------------------- | -------------------------------------- |
| 1     | `crawl(seed_url)` → set of all reachable URLs                                          | BFS with deque + visited set           |
| 2     | `crawl(seed_url, same_domain_only=True)` → filter to same domain                       | URL parsing, domain extraction         |
| 3     | `crawl_concurrent(seed_url, max_workers)` → parallel fetching                          | Thread pool, thread-safe queue and set |
| 4     | `crawl(seed_url, max_depth, rate_limit_per_second)` → depth-limited with rate limiting | Depth tracking, time-based throttling  |

**Why it's hard:**

- Level 1: Must avoid infinite loops on cyclic links; BFS ensures shortest path discovery
- Level 2: URL normalization (fragments, trailing slashes, case) affects deduplication
- Level 3: Multiple threads accessing shared `visited` set and `queue` requires locks or thread-safe structures
- Level 4: Rate limiting requires timestamp tracking; depth requires passing depth through BFS

**Given helper function (typical in ICA):**

```python
def get_links(url: str) -> List[str]:
    """Fetches URL and returns all hyperlinks found in the document."""
    # Provided by the test framework - you don't implement this
    pass
```

**Key considerations:**

- **Fragment handling:** `example.com/page#section` should equal `example.com/page`
- **Normalization:** Trailing slashes, case sensitivity, protocol (http vs https)
- **Domain extraction:** `https://sub.example.com/path` → domain is `sub.example.com`

---

## Level Design Guidelines

| Level | Time      | Methods | Complexity                | What's Tested                         |
| ----- | --------- | ------- | ------------------------- | ------------------------------------- |
| 1     | 15-20 min | 2-3     | O(log n) or O(1) required | Core data structure choice            |
| 2     | 20-25 min | 2-3     | Builds on L1 structure    | Extending the data structure          |
| 3     | 25-30 min | 1-2     | O(log n) compound ops     | Combining operations correctly        |
| 4     | 25-30 min | 1-2     | Full system complexity    | Edge cases, cleanup, advanced queries |

**Total: 6-10 methods across all levels** (not 15-20)

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

### Expected Solution Insight

- Store: `Dict[str, List[Tuple[int, int]]]` where inner list is sorted by timestamp
- Use `bisect.bisect_right(timestamps, target) - 1` for floor queries
- Level 1 choice determines if Level 3-4 are tractable
