from controller import create_debt_records
from model import Contributor
from view import get_contributors

contributors = get_contributors()
debt_records = create_debt_records(contributors)
for record in debt_records:
    print(f'{record.debtor} pays {record.debtee} ${round(record.amount, 2)}')
