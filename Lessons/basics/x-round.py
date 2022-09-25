# Ahmad is more precise about bills, more than the company it self!
decimal_places = 3
bill_charge = 104.498
ahmad_charge = 104.497514

if bill_charge != ahmad_charge:
    print("Error: Bill charge mismatch.")
    print(f"bill_charge: {bill_charge}")
    print(f"ahmad_charge: {ahmad_charge}")

ahmad_charge = round(ahmad_charge, decimal_places)
bill_charge = round(bill_charge, decimal_places)
if bill_charge != ahmad_charge:
    print("Error: Bill charge mismatch for sure.")
    print(f"bill_charge: {bill_charge}")
    print(f"ahmad_charge: {ahmad_charge}")
else:
    print("Correct! Bill charge matches.")
    print(f"bill_charge: {bill_charge}")
    print(f"ahmad_charge: {ahmad_charge}")
