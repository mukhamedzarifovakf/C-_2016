from decimal import Decimal, getcontext
getcontext().prec = 2
Summa = float(input())
Percent = float(input())
mPercent = Percent / 1200
Years = int(input())
Months = Years * 12
K = 1 + mPercent
#K = Decimal(1 + mPercent)
Payment = Decimal(Summa * mPercent *(K ** Months)/ (K ** Months - 1))
#Decimal(Payment).quantize(0.01)
print(Payment)
print(Payment * Months - Summa)