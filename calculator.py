import math

#Goal Amount Calculator function
def goalAmountCalc(num):
    #LG Hours
    goalAmountLeft = num - netPay
    remainder = goalAmountLeft + (goalAmountLeft * fedTaxVar) 
    lgHourGoal = remainder / 20.0

    print("In order to reach $" + str(num) + ", you need this many more hours as a LG: " + str(lgHourGoal))
     




#End goal mamount calculator function
lgHours = float(input("First question: how many hours did you work as a lifeguard this pay period? "))
print("Total LG Hours: " + str(lgHours))

hgHours = float(input("How many hours did you work as a Head Guard this pay period? "))
print("Total HG Hours: " + str(hgHours))

wseHours = float(input("How many hours did you work as a Swim instructor this pay period? "))
print("Total WSE Hours: " + str(wseHours))

overlapWSE = float(input("Do any of your WSE hours overlap on a LG/HG shift? If so, enter the amount, or put 0: "))
print("Total overlap hours: " + str(overlapWSE))


def totalHours():
    return (lgHours + hgHours + wseHours  - overlapWSE)

print("For this pay period, you worked a total of " + str(totalHours()) + "hours! (accounts for overlap) ")

lgAmount = lgHours * 20.80
hgAmount = hgHours * 20.50
wseAmount = wseHours * 21.50

grossPay = (lgAmount + hgAmount + wseAmount)
print("This pay period you grossed: $" + str(grossPay))

fedTax = "7.65"
fedTaxVar = .0765

print("The current federal income tax rate is " + fedTax + "%. ")

lgTax = round(lgAmount * fedTaxVar, 2)
hgTax = round(hgAmount * fedTaxVar, 2)
wseTax = round(wseAmount * fedTaxVar, 2)
totalTax = round(wseTax + hgTax + lgTax, 2)

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
print("|    LG    | $20.8/hr |      " + str(lgHours) + "    |    $" + str(lgAmount) + "     |     $" + str(lgTax) + "     |   $" + str(lgNet) + " |")
print("|---------------------------------------------------------------------------------|")
print("|    HG    | $20.5/hr |      " + str(hgHours) + "    |    $" + str(hgAmount) + "     |     $" + str(hgTax) + "     |   $" + str(hgNet) + " |")
print("|---------------------------------------------------------------------------------|")
print("|    WSE   | $21.5/hr |      " + str(wseHours) + "    |    $" + str(wseAmount) + "     |     $" + str(wseTax) + "     |   $" + str(wseNet) + " |")
print("|---------------------------------------------------------------------------------|")
print("|          |  Total   |      " + str(totalHours()) + "    |    $" + str(grossPay) + "     |     $" + str(totalTax) + "     |   $" + str(netPay) + " |")

goalCalc = input("Would you like to figure out how many more hours you must work in order to reach a certain amount of money? Y / N ")
if goalCalc == "Y" or goalCalc == "y" or goalCalc == "yes" or goalCalc == "Yes":
    goalAmount = float(input("What is your desired goal amount to make this pay period?: "))
    goalAmountCalc(goalAmount)




else: 
    print("Okay, look forward to making $" + str(netPay) + " this pay period!")
