from settle_debt import Participant, settle_debt

participants = [
    Participant('Bobby', 991.11),
    Participant('Lisa', -870.49),
    Participant('Peter', 510.60),
    Participant('Mikaela', 339.77),
    Participant('Toby', -662.16),
    Participant('Rebecca', -273.29),
    Participant('Graham', 383.92),
    Participant('Alicia', -419.46),
]

records = settle_debt(participants=participants)
for record in records:
    print(f'{record.debtor} pays {record.debtee} ${round(record.amount, 2)}')