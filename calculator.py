lgHours = input("First question: how many hours did you work as a lifeguard this pay period? ")
print("Total LG Hours: " + lgHours)

hgHours = input("How many hours did you work as a Head Guard this pay period? ")
print("Total HG Hours: " + hgHours)

wseHours = input("How many hours did you work as a Swim instructor this pay period? ")
print("Total WSE Hours: " + wseHours)

overlapWSE = input("Do any of your WSE hours overlap on a LG/HG shift? If so, enter the amount, or put 0")
print("Total overlap hours: " + overlapWSE)

print("Stats to note: \n Current LG Pay: $20/hr \n Current HG Pay: $20.50/hr \n Current WSE Pay: $21.50/hr")

print("Your total amount of hours for this pay period is: " + totalHours(lgHours, hgHours))

totalHours = (lgHours + hgHours + wseHours) - overlapWSE
print("For this pay period, you worked a total of " + totalHours + " (accounts for overlap) hours! ")

lgAmount = lgHours * 20
hgAmount = hgHours * 20.50
wseAmount = wseHours * 21.50

grossPay = (lgAmount + hgAmount + wseAmount)
print("This pay period you grossed: $" + totalPay)

fedTax = 8.29

print("The current federal income tax rate is " + fedTax + "%. ")

netPay = grossPay - (grossPay * fedTax)