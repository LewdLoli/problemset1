balance = input('Enter the outstanding balance on your credit card: ')
annualInterest = input('Enter the annual credit card interest rate as a decimal: ')
low = balance / 12
high = (balance * (1 + (annualInterest/12)) **12)/12
newBalance = balance

while (1):
    newBalance = balance
    monthlyPayment = (low + high) / 2

    for month in range (1, 13):
        interest = round(balance * annualInterest / 12, 2)
        newBalance = newBalance + interest - monthlyPayment
        if newBalance <= 0:
            break

    if (high - low) > 0.000001:
        print 'RESULT\nMonthly payment to pay off debt in 1 year: $%.2f\nNumber of months needed: %d\nBalance: $%.2f' % (monthlyPayment, month, newBalance)
        break
    elif newBalance < 0:
        high = monthlyPayment
    else:
        low = monthlyPayment

