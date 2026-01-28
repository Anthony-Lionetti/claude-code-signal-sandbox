# EXAMPLE Level 4: Scheduled Payments & Cashback

**Time Estimate:** 30-60 minutes

## Overview

Add support for scheduling future payments and applying cashback rewards. This level introduces deferred execution and reward calculations.

## Methods to Implement

### `schedule_payment(from_id: str, to_id: str, amount: int, schedule_id: str) -> bool`

Schedule a future payment (NOT executed immediately).

| Input                          | Output  |
| ------------------------------ | ------- |
| Valid scheduling               | `True`  |
| Nonexistent source/destination | `False` |
| Duplicate `schedule_id`        | `False` |
| Zero or negative amount        | `False` |
| Transfer to self               | `False` |

**Important:** Does NOT check if funds are available. That check happens at execution time.

### `process_scheduled_payments() -> int`

Process all scheduled payments in FIFO (first-in, first-out) order.

| Scenario                           | Behavior                              |
| ---------------------------------- | ------------------------------------- |
| Payment succeeds                   | Transfer executed, removed from queue |
| Payment fails (insufficient funds) | Skipped and removed from queue        |
| No scheduled payments              | Returns `0`                           |

Returns the count of successfully processed payments.

### `apply_cashback(account_id: str, cashback_percent: int) -> Optional[int]`

Apply cashback based on total spending (withdrawals + outgoing transfers).

| Input                        | Output                |
| ---------------------------- | --------------------- |
| Valid account, valid percent | Cashback amount added |
| Nonexistent account          | `None`                |
| Percent < 0 or > 100         | `None`                |
| Zero spending                | `0`                   |

**Note:** Uses integer division (floor). Example: 10% of 33 = 3 (not 3.3)

## Data Structure Hints

Add a queue for scheduled payments:

```python
from collections import deque

self.scheduled = deque()        # Queue of (from_id, to_id, amount)
self.schedule_ids = set()       # Track used schedule IDs
```

Or use a list:

```python
self.scheduled = []             # List of {"from": str, "to": str, "amount": int, "id": str}
self.schedule_ids = set()
```

## Key Considerations

1. **FIFO Order**: First scheduled = first processed
2. **Clear Queue**: All payments are removed after processing (even failed ones)
3. **Reuse `transfer()`**: When processing payments, you can reuse your transfer logic
4. **Track Spending**: You should already have this from Level 3's `top_spenders()`

## Edge Cases to Handle

- Duplicate schedule IDs
- Scheduling without sufficient funds (allowed - checked at execution)
- Processing an empty queue
- Processing same queue twice (should return 0 second time)
- Cashback with zero spending
- Cashback percentage edge cases (0%, 100%, negative, >100)
- Integer division for cashback calculation

## Run Tests

```bash
make test-4
```

## Example Usage

```python
bank = BankingSystem()
bank.create_account("alice")
bank.create_account("bob")
bank.deposit("alice", 100)

# Schedule payments
bank.schedule_payment("alice", "bob", 30, "pay1")  # True
bank.schedule_payment("alice", "bob", 30, "pay2")  # True
bank.schedule_payment("alice", "bob", 30, "pay1")  # False (duplicate ID)

# Process - all should succeed (100 >= 30 + 30 + 30? No, only 2 will succeed)
bank.process_scheduled_payments()  # 2 (third would fail if it existed)

bank.get_balance("alice")  # 40
bank.get_balance("bob")    # 60

# Cashback: alice spent 60 in transfers
bank.apply_cashback("alice", 10)  # 6 (10% of 60)
bank.get_balance("alice")         # 46
```

## Congratulations!

If you've made it through all 4 levels, you've built a complete banking system with:

- Account management
- Deposits and withdrawals
- Transfers
- Transaction history
- Spending reports
- Scheduled payments
- Cashback rewards

This covers the typical scope and progression of a CodeSignal ICA.
