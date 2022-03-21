from controller import settle_debt
from model import Contributor
from view import get_contributors

contributors = get_contributors()
records = settle_debt(contributors)
for record in records:
    print(f'{record.debtor} pays {record.debtee} ${round(record.amount, 2)}')
