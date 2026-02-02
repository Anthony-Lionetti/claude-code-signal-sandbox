# EXAMPLE Level 3: Transaction History & Reports

**Time Estimate:** 30-60 minutes

## Overview

Add transaction tracking and reporting capabilities. This level requires you to refactor your existing code to record transactions as they happen.

## Methods to Implement

### `get_transaction_history(account_id: str) -> Optional[list[str]]`

Get the transaction history for an account in chronological order.

| Transaction Type  | Format                                    |
| ----------------- | ----------------------------------------- |
| Deposit           | `"deposit: +{amount}"`                    |
| Withdrawal        | `"withdraw: -{amount}"`                   |
| Outgoing transfer | `"transfer_out: -{amount} to {to_id}"`    |
| Incoming transfer | `"transfer_in: +{amount} from {from_id}"` |

| Input                        | Output                      |
| ---------------------------- | --------------------------- |
| Existing account             | List of transaction strings |
| Account with no transactions | `[]` (empty list)           |
| Nonexistent account          | `None`                      |

### `top_spenders(n: int) -> list[str]`

Get the top N accounts by total outgoing amount (withdrawals + outgoing transfers).

| Input                  | Output                                              |
| ---------------------- | --------------------------------------------------- |
| `n` accounts requested | List of account IDs sorted by spending (descending) |
| Tied spending amounts  | Sort alphabetically by account ID                   |
| `n` > total accounts   | Return all accounts                                 |
| No accounts exist      | `[]` (empty list)                                   |

## Refactoring Required

You'll need to modify your Level 1 and Level 2 code to track transactions:

1. **Add a transaction history list** for each account
2. **Update `deposit()`** to record the transaction
3. **Update `withdraw()`** to record the transaction
4. **Update `transfer()`** to record transactions for both accounts
5. **Track total outgoing amounts** per account for `top_spenders()`

## Run Tests

```bash
make test-3
```

## Example Usage

```python
bank = BankingSystem()
bank.create_account("alice")
bank.create_account("bob")
bank.deposit("alice", 100)
bank.withdraw("alice", 20)
bank.transfer("alice", "bob", 30)

bank.get_transaction_history("alice")
# ['deposit: +100', 'withdraw: -20', 'transfer_out: -30 to bob']

bank.get_transaction_history("bob")
# ['transfer_in: +30 from alice']

# alice spent 50 (20 withdraw + 30 transfer), bob spent 0
bank.top_spenders(2)
# ['alice', 'bob']
```
