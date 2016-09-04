# Task 3
inBal = float(raw_input('Enter the outstanding balance on your credit card: '))
AIR = float(raw_input('Enter the credit card interest rate as a percentage: '))/100
Bal = inBal
upper = round((inBal*(1+(AIR/12.0))**12.0)/12.0,2)
lower = round(inBal/12.0,2)
eps = 0.1
lower = round(inBal/12.0,2)
upper = round((inBal*(1+AIR/12.0)**12.0)/12.0,2)
while abs(Bal)>eps:
    Bal = inBal
    MP = round((upper+lower)/2.0,2)
    for month in range(1,13):
        Bal = round(Bal*(1+AIR/12.0)-MP,2)
    if Bal>0:
        lower = MP
    else:
        upper = MP
print 'RESULTS'
print 'Monthly payment to pay off debt in one year: ' + str(MP)
print 'Balance: $' + str(Bal)