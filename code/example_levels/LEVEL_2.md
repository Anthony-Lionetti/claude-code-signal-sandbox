# EXAMPLE Level 2: Transfers

**Time Estimate:** 20-30 minutes

## Overview

Build on Level 1 by adding the ability to transfer money between accounts and query balances.

## Methods to Implement

### `get_balance(account_id: str) -> Optional[int]`

Get the current balance of an account.

| Input               | Output          |
| ------------------- | --------------- |
| Existing account    | Current balance |
| Nonexistent account | `None`          |

### `transfer(from_id: str, to_id: str, amount: int) -> bool`

Transfer money between two accounts.

| Input                           | Output  |
| ------------------------------- | ------- |
| Valid transfer                  | `True`  |
| Nonexistent source account      | `False` |
| Nonexistent destination account | `False` |
| Insufficient funds              | `False` |
| Zero or negative amount         | `False` |
| Transfer to self                | `False` |

## Key Considerations

1. **Atomicity**: A transfer should either fully succeed or fully fail. Don't deduct from the source if you can't credit the destination.

2. **Validation Order**: Check all conditions before modifying any state:
   - Both accounts exist
   - Amount is positive
   - Not transferring to self
   - Sufficient funds

## Edge Cases to Handle

- Transferring to/from nonexistent accounts
- Transferring to the same account (self-transfer)
- Transferring more than available balance
- Zero or negative transfer amounts
- Ensure balances are unchanged on failed transfers

## Run Tests

```bash
make test-2
```

## Example Usage

```python
bank = BankingSystem()
bank.create_account("alice")
bank.create_account("bob")
bank.deposit("alice", 100)

bank.get_balance("alice")              # 100
bank.get_balance("bob")                # 0
bank.get_balance("charlie")            # None

bank.transfer("alice", "bob", 40)      # True
bank.get_balance("alice")              # 60
bank.get_balance("bob")                # 40

bank.transfer("alice", "bob", 100)     # False (insufficient)
bank.transfer("alice", "alice", 10)    # False (self-transfer)
bank.transfer("alice", "charlie", 10)  # False (charlie doesn't exist)
```
