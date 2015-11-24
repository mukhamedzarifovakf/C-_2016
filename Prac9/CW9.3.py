import decimal
#getcontext().prec = 2
Summa = decimal.Decimal(input())
Percent = decimal.Decimal(input())
mPercent = Percent / 1200
Years = int(input())
Months = Years * 12
K = 1 + mPercent
Payment = decimal.Decimal(str((Summa * mPercent *(K ** Months)/ (K ** Months - 1))))
Payment.quantize(0.01)
print(Payment)
print(decimal.Decimal(str(Payment * Months - Summa)))