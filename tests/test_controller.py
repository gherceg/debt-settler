from unittest import TestCase

from controller import create_debt_record, settle_debt
from exceptions import TotalAmountOwedIsNotZero
from model import Contributor

class TestSettleDebt(TestCase):
    
    def test_empty_contributors_returns_none(self):
        result = settle_debt([])
        self.assertIsNone(result)

    def test_raises_exception_if_total_amount_spent_does_not_equal_zero(self):
        contributors = [Contributor('test1', 10), Contributor('test2', -5)]
        with self.assertRaises(TotalAmountOwedIsNotZero):
            _ = settle_debt(contributors)

    def test_successful_two_contributors(self):
        contributors = [Contributor('test1', 10), Contributor('test2', -10)]
        debt_records = settle_debt(contributors)
        self.assertEqual(1, len(debt_records))
        self.assertEqual(debt_records[0].debtee, 'test1')
        self.assertEqual(debt_records[0].debtor, 'test2')
        self.assertEqual(debt_records[0].amount, 10)

    def test_successful_three_contributors(self):
        contributors = [Contributor('test1', 15), Contributor('test2', 5), Contributor('test3', -20)]
        debt_records = settle_debt(contributors)
        print(debt_records)
        self.assertEqual(2, len(debt_records))
        self.assertEqual(debt_records[0].debtee, 'test1')
        self.assertEqual(debt_records[0].debtor, 'test3')
        self.assertEqual(debt_records[0].amount, 15)

        self.assertEqual(debt_records[1].debtee, 'test2')
        self.assertEqual(debt_records[1].debtor, 'test3')
        self.assertEqual(debt_records[1].amount, 5)


class TestCreateDebtRecord(TestCase):

    def test_remainder_of_zero(self):
        debtee = Contributor('test1', 5)
        debtor = Contributor('test2', 5)
        record, remainder = create_debt_record(debtee, debtor)
        self.assertEqual(record.debtee, debtee.name)
        self.assertEqual(record.debtor, debtor.name)
        self.assertEqual(record.amount, 5)
        self.assertEqual(remainder, 0)

    def test_positive_remainder(self):
        debtee = Contributor('test1', 10)
        debtor = Contributor('test2', 5)
        record, remainder = create_debt_record(debtee, debtor)
        self.assertEqual(record.debtee, debtee.name)
        self.assertEqual(record.debtor, debtor.name)
        self.assertEqual(record.amount, 5)
        self.assertEqual(remainder, 5)

    def test_negative_remainder(self):
        debtee = Contributor('test1', 5)
        debtor = Contributor('test2', 10)
        record, remainder = create_debt_record(debtee, debtor)
        self.assertEqual(record.debtee, debtee.name)
        self.assertEqual(record.debtor, debtor.name)
        self.assertEqual(record.amount, 5)
        self.assertEqual(remainder, -5)

