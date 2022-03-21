from controller import settle_debt
from model import Contributor

contributors = [
    Contributor('Bobby', 991.11),
    Contributor('Lisa', -870.49),
    Contributor('Peter', 510.60),
    Contributor('Mikaela', 339.77),
    Contributor('Toby', -662.16),
    Contributor('Rebecca', -273.29),
    Contributor('Graham', 383.92),
    Contributor('Alicia', -419.46),
]

records = settle_debt(contributors)
for record in records:
    print(f'{record.debtor} pays {record.debtee} ${round(record.amount, 2)}')
