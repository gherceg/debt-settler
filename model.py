from collections import namedtuple

Participant = namedtuple('Participant', 'name amount_owed')
DebtRecord = namedtuple('DebtRecord', 'debtee debtor amount')
