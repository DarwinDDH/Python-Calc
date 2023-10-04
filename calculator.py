lgHours = int(input("First question: how many hours did you work as a lifeguard this pay period? "))
print("Total LG Hours: " + str(lgHours))

hgHours = int(input("How many hours did you work as a Head Guard this pay period? "))
print("Total HG Hours: " + str(hgHours))

wseHours = int(input("How many hours did you work as a Swim instructor this pay period? "))
print("Total WSE Hours: " + str(wseHours))

overlapWSE = int(input("Do any of your WSE hours overlap on a LG/HG shift? If so, enter the amount, or put 0"))
print("Total overlap hours: " + str(overlapWSE))

print("Stats to note: \n Current LG Pay: $20/hr \n Current HG Pay: $20.50/hr \n Current WSE Pay: $21.50/hr")

def totalHours():
    return (lgHours + hgHours + wseHours  - overlapWSE)

print("For this pay period, you worked a total of " + str(totalHours()) + "hours! (accounts for overlap) ")

lgAmount = lgHours * 20.00
hgAmount = hgHours * 20.50
wseAmount = wseHours * 21.50

grossPay = (lgAmount + hgAmount + wseAmount)
print("This pay period you grossed: $" + str(grossPay))

fedTax = "8.29"
fedTaxVar = .0829

print("The current federal income tax rate is " + fedTax + "%. ")

netPay = grossPay - (grossPay * fedTaxVar)

print("this pay period you netted: $" + str(netPay))