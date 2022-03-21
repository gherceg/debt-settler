from functools import partial
from model import Contributor

def get_contributors():
    contributors = []

    total = int(input("Number of contributors: "))
    current = 0
    while current < total:
        name = input("Name: ")
        amount_owed = input("Amount owed ($): ")
        try:
            contributor = Contributor(name=name, amount_owed=round(float(amount_owed), 2))
        except ValueError as e:
            print(f'ValueError: {e}\nTry again')
            continue

        contributors.append(contributor)
        current += 1

    return contributors