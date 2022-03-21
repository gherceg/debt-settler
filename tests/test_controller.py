from unittest import TestCase

from controller import create_debt_records, get_amount_to_pay_with_remainder
from exceptions import TotalAmountOwedIsNotZero
from model import Contributor

class TestCreateDebtRecords(TestCase):
    
    def test_empty_contributors_returns_none(self):
        result = create_debt_records([])
        self.assertIsNone(result)

    def test_raises_exception_if_total_amount_spent_does_not_equal_zero(self):
        contributors = [Contributor('test1', 10), Contributor('test2', -5)]
        with self.assertRaises(TotalAmountOwedIsNotZero):
            _ = create_debt_records(contributors)

    def test_successful_two_contributors(self):
        contributors = [Contributor('test1', 10), Contributor('test2', -10)]
        debt_records = create_debt_records(contributors)
        self.assertEqual(1, len(debt_records))
        self.assertEqual(debt_records[0].debtee, 'test1')
        self.assertEqual(debt_records[0].debtor, 'test2')
        self.assertEqual(debt_records[0].amount, 10)

    def test_successful_three_contributors(self):
        contributors = [Contributor('test1', 15), Contributor('test2', 5), Contributor('test3', -20)]
        debt_records = create_debt_records(contributors)
        print(debt_records)
        self.assertEqual(2, len(debt_records))
        self.assertEqual(debt_records[0].debtee, 'test1')
        self.assertEqual(debt_records[0].debtor, 'test3')
        self.assertEqual(debt_records[0].amount, 15)

        self.assertEqual(debt_records[1].debtee, 'test2')
        self.assertEqual(debt_records[1].debtor, 'test3')
        self.assertEqual(debt_records[1].amount, 5)


class TestGetAmountToPayWithRemainder(TestCase):

    def test_remainder_of_zero(self):
        debtee = Contributor('test1', 5)
        debtor = Contributor('test2', 5)
        amount_to_pay, remainder = get_amount_to_pay_with_remainder(debtee, debtor)
        self.assertEqual(amount_to_pay, 5)
        self.assertEqual(remainder, 0)

    def test_positive_remainder(self):
        debtee = Contributor('test1', 10)
        debtor = Contributor('test2', 5)
        amount_to_pay, remainder = get_amount_to_pay_with_remainder(debtee, debtor)
        self.assertEqual(amount_to_pay, 5)
        self.assertEqual(remainder, 5)

    def test_negative_remainder(self):
        debtee = Contributor('test1', 5)
        debtor = Contributor('test2', 10)
        amount_to_pay, remainder = get_amount_to_pay_with_remainder(debtee, debtor)
        self.assertEqual(amount_to_pay, 5)
        self.assertEqual(remainder, -5)

