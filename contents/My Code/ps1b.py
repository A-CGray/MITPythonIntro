# Task 2
inBal = float(raw_input('Enter the outstanding balance on your credit card: '))
AIR = float(raw_input('Enter the credit card interest rate as a percentage: '))/100
payment = 0
IP = 0
PP = 0
TP = 0
MP = 0
Bal = inBal
while Bal > 0 & MP<inBal:
    MP +=10
    #print str(MP)
    Bal = inBal
    for month in range(1,13):
        Bal = round(Bal*(1+AIR/12.0)-MP,2)
        if Bal<0:
            break
print 'RESULT'
print 'Monthly payment to pay off debt in 1 year: ' + str(MP)
print 'Number of months needed: ' + str(month)
print 'Balance: $' + str(Bal)