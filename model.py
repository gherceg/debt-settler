from collections import namedtuple

Contributor = namedtuple('Contributor', 'name amount_owed')
DebtRecord = namedtuple('DebtRecord', 'debtee debtor amount')
