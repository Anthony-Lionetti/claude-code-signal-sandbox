# EXAMPLE Level 1: Basic Operations

**Time Estimate:** 10-15 minutes

## Overview

Implement the foundational account operations: creating accounts, depositing money, and withdrawing money.

## Methods to Implement

### `create_account(account_id: str) -> bool`

Create a new account with the given ID.

| Input               | Output  |
| ------------------- | ------- |
| New account ID      | `True`  |
| Existing account ID | `False` |

### `deposit(account_id: str, amount: int) -> Optional[int]`

Deposit money into an account.

| Input                          | Output      |
| ------------------------------ | ----------- |
| Valid account, positive amount | New balance |
| Nonexistent account            | `None`      |
| Zero or negative amount        | `None`      |

### `withdraw(account_id: str, amount: int) -> Optional[int]`

Withdraw money from an account.

| Input                           | Output      |
| ------------------------------- | ----------- |
| Valid account, sufficient funds | New balance |
| Nonexistent account             | `None`      |
| Zero or negative amount         | `None`      |
| Insufficient funds              | `None`      |

## Edge Cases to Handle

- Duplicate account creation
- Deposits/withdrawals on nonexistent accounts
- Zero or negative amounts
- Withdrawing more than the balance
- Withdrawing the exact balance (should succeed, leaving 0)

## Run Tests

```bash
make test-1
```

## Example Usage

```python
bank = BankingSystem()
bank.create_account("acc1")      # True
bank.create_account("acc1")      # False (duplicate)
bank.deposit("acc1", 100)        # 100
bank.deposit("acc1", 50)         # 150
bank.withdraw("acc1", 30)        # 120
bank.withdraw("acc1", 200)       # None (insufficient)
bank.deposit("fake", 100)        # None (doesn't exist)
```
