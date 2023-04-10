#Name: Eyob Chekle
#Assignment: Tip Calculator v.2
#Date: 9/1/2022
#Description: Calculate tips based on total and tip percent

def main():
    #Title
    print("Tip Calculator")
    print()

    #Collect User Input
    costOfMeal = float(input("Enter Cost of Meal: "))

    #TipOptions
    tipOptions = ["15%", "20%", "25%"]

    #Run the for loop to iterate 3 times and calculate the tip amount and total
    for x in tipOptions:
        print()
        print(x)

        #Calculate the Tip Amounts and the Total Amount for 15%
        if x == "15%":
            tipAmount = costOfMeal * 0.15
            tipAmount = round(tipAmount, 2)
            print("Tip Amount: ", tipAmount)

            totalAmount = tipAmount + costOfMeal
            totalAmount = round(totalAmount, 2)
            print("Total Amount: ", totalAmount)

        #Calculate the Tip Amounts and the Total Amount for 20%
        elif x == "20%":
            tipAmount = costOfMeal * 0.20
            tipAmount = round(tipAmount, 2)
            print("Tip Amount: ", tipAmount)

            totalAmount = tipAmount + costOfMeal
            totalAmount = round(totalAmount, 2)
            print("Total Amount: ", totalAmount)

        #Calculate the Tip Amounts and the Total Amount for 25%
        elif x == "25%":
            tipAmount = costOfMeal * 0.25
            tipAmount = round(tipAmount, 2)
            print("Tip Amount: ", tipAmount)

            totalAmount = tipAmount + costOfMeal
            totalAmount = round(totalAmount, 2)
            print("Total Amount: ", totalAmount)
        








if __name__ == "__main__":
    main()

    
