from decimal import Decimal
Summa = Decimal(input())
Percent = Decimal(input())
mPercent = Percent / 1200
Years = int(input())
Months = Years * 12
K = 1 + mPercent
Payment = Decimal(str((Summa * mPercent *(K ** Months)/ (K ** Months - 1)))).quantize(Decimal('0.01'))
print(Payment) #аннуитетный платеж
print(Decimal(str(Payment * Months - Summa))) #итоговая переплата
