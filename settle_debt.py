from collections import namedtuple

class TotalAmountOwedIsNotZero(Exception):
    pass

Participant = namedtuple('Participant', 'name amount_owed')
DebtRecord = namedtuple('DebtRecord', 'debtee debtor amount')

def settle_debt(participants):
    if not participants:
        return None
    
    total = sum(p.amount_owed for p in participants)
    if total != 0 and total >= 0.01:
        raise TotalAmountOwedIsNotZero(f'Difference is {total}')

    debt_records = []
    debtees = list(filter(lambda p: p.amount_owed > 0, participants))
    debtors = list(filter(lambda p: p.amount_owed < 0, participants))
    # save us from a bunch of absolute values below
    debtors = list(map(lambda p: Participant(p.name, abs(p.amount_owed)), debtors))
    
    while len(debtees) > 0:
        debtees.sort(key=lambda p: p.amount_owed)
        debtors.sort(key=lambda p: p.amount_owed)
        debtee = debtees.pop()
        debtor = debtors.pop()
        record, remainder = create_debt_record(debtee, debtor)
        debt_records.append(record)
        if remainder > 0:
            debtees.append(Participant(name=debtee.name, amount_owed=remainder))
        elif remainder < 0:
            debtors.append(Participant(name=debtor.name, amount_owed=abs(remainder)))

    return debt_records

def create_debt_record(debtee, debtor):
    if debtee.amount_owed > debtor.amount_owed:
        record = DebtRecord(debtee=debtee.name, debtor=debtor.name, amount=debtor.amount_owed)
    elif debtee.amount_owed < debtor.amount_owed:
        record = DebtRecord(debtee=debtee.name, debtor=debtor.name, amount=debtee.amount_owed)
    else:
        record = DebtRecord(debtee=debtee.name, debtor=debtor.name, amount=debtee.amount_owed)

    return record, round(debtee.amount_owed - debtor.amount_owed, 2)
