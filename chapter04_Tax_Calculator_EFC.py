#Assignment: Chapter 4 Tax Calculator
#Name: Eyob Chekle
#Date: 9/8/2022
#Description: Calculate the total of items, then sales tax, then total w/ salestax

import CalculationsFunctions as PCM


def main():
    print("Sales Tax Calculator")
    print()

    #Begin While Loop
    #Ask for input of items
    again = 'y'
    itemTotal = 0
    counter = 0
    
    while again == 'y':
        #Ask for item input
        print("Enter items (Enter '-99.0' to end): ")
        print()

        itemTotal = itemTotal + float(input("Cost of item: "))

        #Calculate Sales Tax
        totalSalesTax = 0
        totalSalesTax = PCM.calculateSalesTax(itemTotal)

        #Calculate Total after Tax
        totalAfterSalesTax = 0
        totalAfterSalesTax = PCM.calculateAfterTaxTotal(itemTotal)

        #Print outputs
        print()
        print("Total: ", round(itemTotal,2))
        print("Sales tax: ", totalSalesTax)
        print("Total after tax: ", totalAfterSalesTax)
        print()

        #Break the while loop
        again = input("Enter 'y' to enter a new item: ")



























##        while counter != 99:
##            counter = float(input("Cost of item: "))
##            itemTotal = itemTotal + counter
##            print(itemTotal)
            

            

            #itemTotal = itemTotal + float(input("Cost of item: "))
            #print(itemTotal)
        
        

        
        
        
##        #Create a counter for the items using a while loop
##        counter = 0
##
##        while counter != '-99.0':
##            itemTotal = counter
##            itemTotal += float(input("Cost of item: "))
##            print(itemTotal)

        
    




if __name__ == "__main__":
    main()
