from exceptions import TotalAmountOwedIsNotZero
from model import Contributor, DebtRecord

def settle_debt(contributors):
    if not contributors:
        return None
    
    total = sum(p.amount_owed for p in contributors)
    if total != 0 and total >= 0.01:
        raise TotalAmountOwedIsNotZero(f'Difference is {total}')

    debt_records = []
    debtees = list(filter(lambda c: c.amount_owed > 0, contributors))
    debtors = list(filter(lambda c: c.amount_owed < 0, contributors))
    # save us from a bunch of absolute values below
    debtors = list(map(lambda c: Contributor(c.name, abs(c.amount_owed)), debtors))
    
    while len(debtees) > 0:
        debtees.sort(key=lambda c: c.amount_owed)
        debtors.sort(key=lambda c: c.amount_owed)
        debtee = debtees.pop()
        debtor = debtors.pop()
        record, remainder = create_debt_record(debtee, debtor)
        debt_records.append(record)
        if remainder > 0:
            debtees.append(Contributor(name=debtee.name, amount_owed=remainder))
        elif remainder < 0:
            debtors.append(Contributor(name=debtor.name, amount_owed=abs(remainder)))

    return debt_records

def create_debt_record(debtee, debtor):
    if debtee.amount_owed > debtor.amount_owed:
        record = DebtRecord(debtee=debtee.name, debtor=debtor.name, amount=debtor.amount_owed)
    elif debtee.amount_owed < debtor.amount_owed:
        record = DebtRecord(debtee=debtee.name, debtor=debtor.name, amount=debtee.amount_owed)
    else:
        record = DebtRecord(debtee=debtee.name, debtor=debtor.name, amount=debtee.amount_owed)

    return record, round(debtee.amount_owed - debtor.amount_owed, 2)
