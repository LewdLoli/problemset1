balance = input('Enter the outstanding balance on your credit card: ')
interest = input('Enter the annual credit card interest rate as a decimal: ')
monthlyRate = interest / 12.0
monthlyPayment = 10
month = 0
newBalance = balance

while newBalance >= 0:
    month += 1
    if month > 12:
        month = 0
        newBalance = balance
        monthlyPayment += 10
    else:
        newBalance = newBalance * (1 + monthlyRate) - monthlyPayment

print 'RESULT\nMonthly payment to pay off debt in 1 year: $%.2f\nNumber of months needed: %d\nBalance: $%.2f' % (monthlyPayment, month, newBalance)
