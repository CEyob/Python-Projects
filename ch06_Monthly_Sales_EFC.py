#Name: Eyob Chekle
#Assignment: CH06 Monthly Sales Output
#9/15/2022
#This program will display monthly sales data, and calculate total and average sale amounts

#Function for displaying menu
def displayMenu():
    print("Command Menu")
    print("monthly - View monthly sales")
    print("yearly - View yearly summary")
    print("edit - Edit sales for a month")
    print("exit - Exit program")

#Function for viewing monthly sales
def viewMonthly(myList):
    print("Month - Sales")
    #Attempt at a for loop to itterate through the loop and display months
    for row in myList:
        print(row[0] + " - " + str(row[1]) + ".\n")

    print()

#Function for viewing total and average sale amounts
def viewYearly(myList):
    total = 0
    for item in myList:
        total = total + int(item[1])
    print("Yearly total: ", total, "\nMonthly Average: ", round(total/12,2))


#Function attempt at editing list   
def editSales(myList):
    month = input("Three-letter Month: ")

    #Search for matching month
    i = 0
    listIndex = -1
    while i < len(myList):
        if myList[i][0] == month:
            listIndex = i
            break
        i += 1

    #If match is found then ask for input for new value
    if listIndex != -1:
        salesEdit = str(input("Sales Amount: "))
        chosenEdit = myList[listIndex].pop(listIndex)
        myList[listIndex].insert(listIndex, salesEdit)
        print("Sales amount for ", month, " was modified")
    else:
        print("Invalid Three Letter Month!")

    print()
            
        




def main():
    print("Monthly Sales Program")
    print()

    #Create my list in which the month and amount of sales are included
    monthlySales =    [['Jan', '616'], ['Feb', '466'], ['Mar', '796'], ['Apr', '238'], 
			  ['May', '310'], ['Jun', '726'], ['Jul', '987'], ['Aug', '604'], 
			  ['Sep', '951'], ['Oct', '958'], ['Nov', '238'], ['Dec', '610']]
    #print(monthlySales)
    displayMenu()

    #While loop to keep repeating the menu choices for user
    while True:
        command = input("\nEnter Option Choice: ")

        #Calls the function to view all the monthly sales
        if command == 'monthly':
            viewMonthly(monthlySales)
        #Calls the function for yearly totals
        elif command == 'yearly':
            viewYearly(monthlySales)
        #Calls the function to edit sales for a month
        elif command == 'edit':
            editSales(monthlySales)
        elif command == 'exit':
            break
        else:
            print("This is not a valid option. Please try again.\n")
            displayMenu()

    print("Bye!")
            
            


        









if __name__ == "__main__":
    main()
    

    

    
