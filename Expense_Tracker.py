# Expense tracker project

Expenseslist = [] #list 
print("Welcome to Expense Tracker")

while True:
    print("=====MENU=====")
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Show Total Kharcha")
    print("4.Exit")
    
    choice = 0
    try:
        choice = int(input("Enter Your Choice: "))
    except ValueError:
        print("Please enter a valid menu number (1-4)")

# 1.ADD EXPENSE
    if(choice == 1 ):
        date = (input ("Enter Date (DD-MM-YYYY):"))
        category = input("Enter Category: (Food, Travel, Cloth, Books) :")
        description = input("Enter Description:")
        amount = float (input("Enter The Amount :"))

        expense ={
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
        }

        Expenseslist.append(expense)
        print("\n Expense is added successfully")

# 2. View Expense

    elif(choice == 2):
        if(len(Expenseslist)== 0):
            print("No Expenses Added. Go and Do More Expense.")
        else:
            print("===== These is your Expense=====")
            print("-" * 80)
            print(f"{'No.':<5}{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':<10}")
            print("-" * 80)

            for count, each_Expense in enumerate(Expenseslist, start=1):
               print(f"{count:<5}"
                     f"{each_Expense['date']:<15}"
                     f"{each_Expense['category']:<15}"
                     f"{each_Expense['description']:<25}"
                     f"₹{each_Expense['amount']:<10}")
            
# 3.Show Total Expense 

    elif(choice == 3):
        total = 0
        for each_Expense in Expenseslist:
            total+= each_Expense["amount"]

        print("\n Total Expense =", total)

# 4.Exit
    elif(choice == 4):
        print("Thank visit again")
        break
    else:
        print("Invalid Choice Try Again")