"""
Test Suite for Banking System ICA Practice
==========================================

Run tests by level:
    uv run pytest test_simulation.py -k "level_1" -v
    uv run pytest test_simulation.py -k "level_2" -v
    uv run pytest test_simulation.py -k "level_3" -v
    uv run pytest test_simulation.py -k "level_4" -v

Run all tests:
    uv run pytest test_simulation.py -v
"""

import pytest
from simulation import BankingSystem


# =============================================================================
# LEVEL 1: Basic Operations (10-15 minutes)
# =============================================================================


class TestLevel1BasicOperations:
    """Tests for create_account, deposit, and withdraw."""

    def test_level_1_create_account_success(self):
        """Can create a new account."""
        bank = BankingSystem()
        assert bank.create_account("acc1") is True

    def test_level_1_create_account_duplicate(self):
        """Cannot create duplicate account."""
        bank = BankingSystem()
        bank.create_account("acc1")
        assert bank.create_account("acc1") is False

    def test_level_1_create_multiple_accounts(self):
        """Can create multiple different accounts."""
        bank = BankingSystem()
        assert bank.create_account("acc1") is True
        assert bank.create_account("acc2") is True
        assert bank.create_account("acc3") is True

    def test_level_1_deposit_success(self):
        """Can deposit into existing account."""
        bank = BankingSystem()
        bank.create_account("acc1")
        assert bank.deposit("acc1", 100) == 100

    def test_level_1_deposit_multiple(self):
        """Multiple deposits accumulate correctly."""
        bank = BankingSystem()
        bank.create_account("acc1")
        assert bank.deposit("acc1", 100) == 100
        assert bank.deposit("acc1", 50) == 150
        assert bank.deposit("acc1", 25) == 175

    def test_level_1_deposit_nonexistent_account(self):
        """Cannot deposit into nonexistent account."""
        bank = BankingSystem()
        assert bank.deposit("acc1", 100) is None

    def test_level_1_deposit_invalid_amount(self):
        """Cannot deposit zero or negative amount."""
        bank = BankingSystem()
        bank.create_account("acc1")
        assert bank.deposit("acc1", 0) is None
        assert bank.deposit("acc1", -50) is None

    def test_level_1_withdraw_success(self):
        """Can withdraw from account with sufficient funds."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        assert bank.withdraw("acc1", 30) == 70

    def test_level_1_withdraw_multiple(self):
        """Multiple withdrawals work correctly."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        assert bank.withdraw("acc1", 20) == 80
        assert bank.withdraw("acc1", 30) == 50
        assert bank.withdraw("acc1", 50) == 0

    def test_level_1_withdraw_insufficient_funds(self):
        """Cannot withdraw more than balance."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        assert bank.withdraw("acc1", 150) is None
        # Balance should be unchanged
        bank.deposit("acc1", 0)  # This will fail, need get_balance

    def test_level_1_withdraw_nonexistent_account(self):
        """Cannot withdraw from nonexistent account."""
        bank = BankingSystem()
        assert bank.withdraw("acc1", 50) is None

    def test_level_1_withdraw_invalid_amount(self):
        """Cannot withdraw zero or negative amount."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        assert bank.withdraw("acc1", 0) is None
        assert bank.withdraw("acc1", -20) is None

    def test_level_1_withdraw_exact_balance(self):
        """Can withdraw exact balance amount."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        assert bank.withdraw("acc1", 100) == 0


# =============================================================================
# LEVEL 2: Transfers (20-30 minutes)
# =============================================================================


class TestLevel2Transfers:
    """Tests for transfer and get_balance."""

    def test_level_2_get_balance_new_account(self):
        """New account has zero balance."""
        bank = BankingSystem()
        bank.create_account("acc1")
        assert bank.get_balance("acc1") == 0

    def test_level_2_get_balance_after_deposit(self):
        """Balance reflects deposits."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        assert bank.get_balance("acc1") == 100

    def test_level_2_get_balance_nonexistent(self):
        """Nonexistent account returns None."""
        bank = BankingSystem()
        assert bank.get_balance("acc1") is None

    def test_level_2_transfer_success(self):
        """Can transfer between accounts."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.deposit("acc1", 100)
        assert bank.transfer("acc1", "acc2", 40) is True
        assert bank.get_balance("acc1") == 60
        assert bank.get_balance("acc2") == 40

    def test_level_2_transfer_insufficient_funds(self):
        """Cannot transfer more than balance."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.deposit("acc1", 100)
        assert bank.transfer("acc1", "acc2", 150) is False
        assert bank.get_balance("acc1") == 100
        assert bank.get_balance("acc2") == 0

    def test_level_2_transfer_nonexistent_source(self):
        """Cannot transfer from nonexistent account."""
        bank = BankingSystem()
        bank.create_account("acc2")
        assert bank.transfer("acc1", "acc2", 50) is False

    def test_level_2_transfer_nonexistent_destination(self):
        """Cannot transfer to nonexistent account."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        assert bank.transfer("acc1", "acc2", 50) is False
        assert bank.get_balance("acc1") == 100

    def test_level_2_transfer_to_self(self):
        """Cannot transfer to same account."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        assert bank.transfer("acc1", "acc1", 50) is False

    def test_level_2_transfer_invalid_amount(self):
        """Cannot transfer zero or negative amount."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.deposit("acc1", 100)
        assert bank.transfer("acc1", "acc2", 0) is False
        assert bank.transfer("acc1", "acc2", -20) is False

    def test_level_2_multiple_transfers(self):
        """Multiple transfers work correctly."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.create_account("acc3")
        bank.deposit("acc1", 100)
        bank.transfer("acc1", "acc2", 30)
        bank.transfer("acc2", "acc3", 20)
        bank.transfer("acc1", "acc3", 10)
        assert bank.get_balance("acc1") == 60
        assert bank.get_balance("acc2") == 10
        assert bank.get_balance("acc3") == 30


# =============================================================================
# LEVEL 3: Transaction History & Reports (30-60 minutes)
# =============================================================================


class TestLevel3HistoryAndReports:
    """Tests for get_transaction_history and top_spenders."""

    def test_level_3_history_empty(self):
        """New account has empty history."""
        bank = BankingSystem()
        bank.create_account("acc1")
        assert bank.get_transaction_history("acc1") == []

    def test_level_3_history_nonexistent(self):
        """Nonexistent account returns None."""
        bank = BankingSystem()
        assert bank.get_transaction_history("acc1") is None

    def test_level_3_history_deposit(self):
        """Deposit is recorded in history."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        history = bank.get_transaction_history("acc1")
        assert history == ["deposit: +100"]

    def test_level_3_history_withdraw(self):
        """Withdrawal is recorded in history."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        bank.withdraw("acc1", 30)
        history = bank.get_transaction_history("acc1")
        assert history == ["deposit: +100", "withdraw: -30"]

    def test_level_3_history_transfer(self):
        """Transfer is recorded in both accounts."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.deposit("acc1", 100)
        bank.transfer("acc1", "acc2", 40)

        history1 = bank.get_transaction_history("acc1")
        assert history1 == ["deposit: +100", "transfer_out: -40 to acc2"]

        history2 = bank.get_transaction_history("acc2")
        assert history2 == ["transfer_in: +40 from acc1"]

    def test_level_3_history_order(self):
        """History maintains chronological order."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.deposit("acc1", 100)
        bank.withdraw("acc1", 10)
        bank.transfer("acc1", "acc2", 20)
        bank.deposit("acc1", 50)

        history = bank.get_transaction_history("acc1")
        assert history == [
            "deposit: +100",
            "withdraw: -10",
            "transfer_out: -20 to acc2",
            "deposit: +50",
        ]

    def test_level_3_top_spenders_basic(self):
        """Top spenders returns accounts by outgoing amount."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.deposit("acc1", 200)
        bank.deposit("acc2", 200)
        bank.withdraw("acc1", 50)
        bank.withdraw("acc2", 80)

        assert bank.top_spenders(2) == ["acc2", "acc1"]

    def test_level_3_top_spenders_includes_transfers(self):
        """Top spenders includes outgoing transfers."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.create_account("acc3")
        bank.deposit("acc1", 200)
        bank.deposit("acc2", 200)
        bank.withdraw("acc1", 30)
        bank.transfer("acc2", "acc3", 100)

        # acc2: 100 outgoing, acc1: 30 outgoing, acc3: 0
        assert bank.top_spenders(3) == ["acc2", "acc1", "acc3"]

    def test_level_3_top_spenders_alphabetical_tie(self):
        """Tied accounts are sorted alphabetically."""
        bank = BankingSystem()
        bank.create_account("charlie")
        bank.create_account("alice")
        bank.create_account("bob")
        bank.deposit("charlie", 100)
        bank.deposit("alice", 100)
        bank.deposit("bob", 100)
        bank.withdraw("charlie", 50)
        bank.withdraw("alice", 50)
        bank.withdraw("bob", 50)

        assert bank.top_spenders(3) == ["alice", "bob", "charlie"]

    def test_level_3_top_spenders_n_greater_than_accounts(self):
        """Returns all accounts if n exceeds account count."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")

        result = bank.top_spenders(10)
        assert len(result) == 2

    def test_level_3_top_spenders_empty(self):
        """Returns empty list when no accounts exist."""
        bank = BankingSystem()
        assert bank.top_spenders(5) == []


# =============================================================================
# LEVEL 4: Scheduled Payments & Cashback (30-60 minutes)
# =============================================================================


class TestLevel4ScheduledPayments:
    """Tests for schedule_payment, process_scheduled_payments, apply_cashback."""

    def test_level_4_schedule_payment_success(self):
        """Can schedule a payment."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.deposit("acc1", 100)
        assert bank.schedule_payment("acc1", "acc2", 50, "pay1") is True

    def test_level_4_schedule_payment_duplicate_id(self):
        """Cannot schedule with duplicate ID."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.deposit("acc1", 100)
        bank.schedule_payment("acc1", "acc2", 30, "pay1")
        assert bank.schedule_payment("acc1", "acc2", 20, "pay1") is False

    def test_level_4_schedule_payment_nonexistent_account(self):
        """Cannot schedule with nonexistent accounts."""
        bank = BankingSystem()
        bank.create_account("acc1")
        assert bank.schedule_payment("acc1", "acc2", 50, "pay1") is False
        assert bank.schedule_payment("acc2", "acc1", 50, "pay2") is False

    def test_level_4_schedule_payment_to_self(self):
        """Cannot schedule payment to same account."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        assert bank.schedule_payment("acc1", "acc1", 50, "pay1") is False

    def test_level_4_schedule_payment_invalid_amount(self):
        """Cannot schedule with invalid amount."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        assert bank.schedule_payment("acc1", "acc2", 0, "pay1") is False
        assert bank.schedule_payment("acc1", "acc2", -10, "pay2") is False

    def test_level_4_process_payments_success(self):
        """Process scheduled payments successfully."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.deposit("acc1", 100)
        bank.schedule_payment("acc1", "acc2", 30, "pay1")
        bank.schedule_payment("acc1", "acc2", 20, "pay2")

        assert bank.process_scheduled_payments() == 2
        assert bank.get_balance("acc1") == 50
        assert bank.get_balance("acc2") == 50

    def test_level_4_process_payments_fifo(self):
        """Payments processed in FIFO order."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.create_account("acc3")
        bank.deposit("acc1", 100)
        bank.schedule_payment("acc1", "acc2", 60, "pay1")
        bank.schedule_payment("acc1", "acc3", 60, "pay2")  # Will fail

        # First payment should succeed, second should fail
        assert bank.process_scheduled_payments() == 1
        assert bank.get_balance("acc1") == 40
        assert bank.get_balance("acc2") == 60
        assert bank.get_balance("acc3") == 0

    def test_level_4_process_payments_empty(self):
        """Processing with no scheduled payments returns 0."""
        bank = BankingSystem()
        assert bank.process_scheduled_payments() == 0

    def test_level_4_process_payments_clears_queue(self):
        """Processing clears the queue."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.deposit("acc1", 100)
        bank.schedule_payment("acc1", "acc2", 30, "pay1")
        bank.process_scheduled_payments()
        # Processing again should return 0
        assert bank.process_scheduled_payments() == 0

    def test_level_4_cashback_success(self):
        """Cashback calculated correctly."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        bank.withdraw("acc1", 50)
        # 10% of 50 = 5
        assert bank.apply_cashback("acc1", 10) == 5
        assert bank.get_balance("acc1") == 55

    def test_level_4_cashback_includes_transfers(self):
        """Cashback includes outgoing transfers."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.create_account("acc2")
        bank.deposit("acc1", 200)
        bank.withdraw("acc1", 50)
        bank.transfer("acc1", "acc2", 50)
        # Total outgoing: 100, 20% = 20
        assert bank.apply_cashback("acc1", 20) == 20

    def test_level_4_cashback_nonexistent_account(self):
        """Cashback on nonexistent account returns None."""
        bank = BankingSystem()
        assert bank.apply_cashback("acc1", 10) is None

    def test_level_4_cashback_invalid_percent(self):
        """Invalid cashback percentage returns None."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        bank.withdraw("acc1", 50)
        assert bank.apply_cashback("acc1", -5) is None
        assert bank.apply_cashback("acc1", 101) is None

    def test_level_4_cashback_zero_spending(self):
        """Cashback with no spending returns 0."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        assert bank.apply_cashback("acc1", 10) == 0

    def test_level_4_cashback_integer_division(self):
        """Cashback uses integer division (floor)."""
        bank = BankingSystem()
        bank.create_account("acc1")
        bank.deposit("acc1", 100)
        bank.withdraw("acc1", 33)
        # 10% of 33 = 3.3, floored to 3
        assert bank.apply_cashback("acc1", 10) == 3


# =============================================================================
# Integration Tests
# =============================================================================


class TestIntegration:
    """End-to-end integration tests."""

    def test_integration_full_workflow(self):
        """Complete banking workflow."""
        bank = BankingSystem()

        # Create accounts
        bank.create_account("alice")
        bank.create_account("bob")
        bank.create_account("charlie")

        # Initial deposits
        bank.deposit("alice", 1000)
        bank.deposit("bob", 500)
        bank.deposit("charlie", 750)

        # Some transactions
        bank.transfer("alice", "bob", 200)
        bank.withdraw("charlie", 100)
        bank.transfer("bob", "charlie", 150)

        # Check balances
        assert bank.get_balance("alice") == 800
        assert bank.get_balance("bob") == 550
        assert bank.get_balance("charlie") == 800

        # Check top spenders (alice: 200, charlie: 100, bob: 150)
        assert bank.top_spenders(2) == ["alice", "bob"]

        # Schedule and process payments
        bank.schedule_payment("alice", "charlie", 100, "rent")
        bank.schedule_payment("bob", "alice", 50, "lunch")
        assert bank.process_scheduled_payments() == 2

        # Final balances
        assert bank.get_balance("alice") == 750
        assert bank.get_balance("bob") == 500
        assert bank.get_balance("charlie") == 900
