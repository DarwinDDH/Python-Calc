import math


lgHours = int(input("First question: how many hours did you work as a lifeguard this pay period? "))
print("Total LG Hours: " + str(lgHours))


hgHours = int(input("How many hours did you work as a Head Guard this pay period? "))
print("Total HG Hours: " + str(hgHours))


wseHours = int(input("How many hours did you work as a Swim instructor this pay period? "))
print("Total WSE Hours: " + str(wseHours))


overlapWSE = int(input("Do any of your WSE hours overlap on a LG/HG shift? If so, enter the amount, or put 0: "))
print("Total overlap hours: " + str(overlapWSE))


print("Stats to note: \n Current LG Pay: $20/hr \n Current HG Pay: $20.50/hr \n Current WSE Pay: $21.50/hr")


def totalHours():
    return(lgHours + hgHours + wseHours - overlapWSE)

print("For this pay period, you worked a total of " + str(totalHours()) + "hours! (accounts for overlap) ")


lgAmount = lgHours * 20.00
hgAmount = hgHours * 20.50
wseAmount = wseHours * 21.50


grossPay = (lgAmount + hgAmount + wseAmount)
print("This pay period you grossed: $" + str(grossPay))


fedTax = "8.29"
fedTaxVar = .0829


print("The current federal income tax rate is " + fedTax + "%. ")


lgTax = round(lgAmount * fedTaxVar, 2)
hgTax = round(hgAmount * fedTaxVar, 2)
wseTax = round(wseAmount * fedTaxVar, 2)


lgNet = round(lgAmount - lgTax, 2)
hgNet = round(hgAmount - hgTax, 2)
wseNet = round(wseAmount - wseTax, 2)


netPay = round(grossPay - (grossPay * fedTaxVar), 2)


print("this pay period you netted: $" + str(netPay))


print("Now lets organize our data in a neater table format.")
#12 characters in Net Amount Column


print("-----------------------------------------------------------------------------------")
print("| Position | Pay Rate | Hours Worked | Gross Amount | Taxable Amount | Net Amount |")
print("|---------------------------------------------------------------------------------|")
print("| LG | $20/hr | " + str(lgHours) + " | $" + str(lgAmount) + " | $" + str(lgTax) + " | $" + str(lgNet) + " |")
print("|---------------------------------------------------------------------------------|")
print("| HG | $20/hr | " + str(hgHours) + " | Gross Amount | Taxable Amount | Net Amount |")
print("|---------------------------------------------------------------------------------|")
print("| LG | $20/hr | " + str(wseHours) + " | Gross Amount | Taxable Amount | Net Amount |")
print("|---------------------------------------------------------------------------------|")











