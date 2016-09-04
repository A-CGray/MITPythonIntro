# Problem Set 1
# Name: Alasdair Christison gray
# Time Spent: 30 min + tbc
# Task 1
Bal = float(raw_input('Enter the outstanding balance on your credit card: '))
AIR = float(raw_input('Enter the credit card interest rate as a percentage: '))/100
MMP = float(raw_input('Enter the credit card minimum monthly payment as a percentage: '))/100
payment = 0
IP = 0
PP = 0
TP = 0
for month in range(1,13):
    payment = round(MMP*Bal, 2)
    IP = round(AIR/12.0*Bal,2)
    PP = round(payment - IP,2)
    Bal += round(-PP,2)
    TP += payment
    print 'Month '+str(month)+':'
    print 'Minimum Monthly Payment: $' + str(payment)
    print 'Principle paid: $' + str(PP)
    print 'Remaining Balance: $' + str(Bal)
print 'RESULT'
print 'Total amount paid: $' + str(TP)
print 'Remaining Balance: $' + str(Bal)