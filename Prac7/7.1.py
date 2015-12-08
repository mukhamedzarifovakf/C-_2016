from math import*
def A(x):
    y=None
    if (1/(exp(sin(x) + 1)))/(5/4 + (1/(x**15)))<0 or sin(x) + 1==0 or x**15==-4/5 or 1 + x**2<=0 or 1 + x**2==1:
        y='Neopredelen'
    else:
        y=log((1/(exp(sin(x) + 1)))/(5/4 + (1/(x**15))),1 + x**2)
    return y
print(A(x=1),A(x=10),A(x=1000))
