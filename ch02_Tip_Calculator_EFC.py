#Name: Eyob F. Chekle
#Date: 8/25/2022
#Project: Chapter 2 Tip Calculator

#Input to ask for Cost of Meal
print("Tip Calculator!")
print(" ")

costOfMeal = input("Enter Cost of Meal: ")

costOfMeal = float(costOfMeal)

#Input to ask for Tip Percent
tipPercent = input("Enter Tip Percent: ")

tipPercent = float(tipPercent)

#Process the Tip Amount

tipAmount = costOfMeal * (tipPercent / 100)

tipAmount = float(tipAmount)

tipAmount = round(tipAmount, 2)

#Process the Total Amount
totalAmount = costOfMeal + tipAmount
totalAmount = round(totalAmount, 2)

#Outputs
print(" ")
print("Tip amount: ", tipAmount)
print("Total Amount: ", totalAmount)


