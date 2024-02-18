from decimal import Decimal
a = 0.5
print("a:{a:0.30f}".format(a=a))
b = 0.1
print("b:{b:0.30f}".format(b=b))

charge = Decimal(3.5)
print(charge)

print(Decimal(99.99) - Decimal(99.973))
print(Decimal("99.99") - Decimal("99.973"))