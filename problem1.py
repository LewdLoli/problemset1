balance = input('Enter the outstanding balance on your credit card: ')
interest = input('Enter the annual credit card interest rate as a decimal: ')
rate = input('Enter the minimum monthly payment rate as a decimal: ')
totalPaid = 0

for x in range(1, 13):
    minimumPayment = balance * rate
    interestPaid = (interest / 12.0) * balance
    principalPaid = minimumPayment - interestPaid
    balance -= principalPaid
    totalPaid += principalPaid + interestPaid

    print 'Month: %d' % (x)
    print 'Minimum monthly payment: $%.2f' % (minimumPayment)
    print 'Principle paid: $%.2f' % (principalPaid)
    print 'Remaining balance: $%.2f' % (balance)

print 'RESULT\nTotal amount paid: $%.2f\nRemaining balance: $%.2f' % (totalPaid, balance)
