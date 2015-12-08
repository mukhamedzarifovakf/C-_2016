from decimal import Decimal
Summa = float(input())
Summa0 = Summa
Percent = float(input())
mPercent = Percent / 1200
Years = int(input())
Months = Years * 12
K = 1 + mPercent
Payment = ((Summa * mPercent *(K ** Months)/ (K ** Months - 1)))
print(Payment)
print(Payment * Months - Summa)
Rests = []
for i in range(Months):
    print(Summa, end = ' ')
    Rest.append(Summa)
    if i != Months - 1:
        print(Payment, end = ' ')
        print(mPercent * Summa, end = ' ')
        print(Payment - mPercent * Summa, end = ' ')
        print()
        Summa = Summa * (1 + mPercent) - Payment
    else:
        print((mPercent + 1) * Summa, end = ' ')
        print(mPercent * Summa, end = ' ')
        print(Summa)
        Summa = 0

import numpy as np
import matplotlib.pyplot as plt

#график остатка (в целом)
Months_numbers = []
Months_numbers.append(i for i in range(1, Months))

plt.subplot(2, 2, 1)
plt.bar(Months, Rests)
plt.xticks(Months_numbers, Months_numbers)
plt.ylabel('Остаток по кредиту')
plt.xlabel('Месяц')
plt.subplots_adjust(left = 0.15)