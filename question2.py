class GroceryList:
    def __init__(self,budget):
        self.dict = {}
        self.budget = budget

    def addItem(self,item,quantity,price):
        if price>self.budget:
            print("Can't Buy the product ###(because budget left is {})".format(self.budget))
            return
        quantity = float(quantity.split()[0])
        if item in self.dict:
            self.dict[item]['Quantity']+=quantity
            self.dict[item]['Price']+=price
        else:
            self.dict[item] = {'Quantity':quantity,'Price':price}

        self.budget-=price
        print('Amount left : {}'.format(self.budget))

    def itemInBudget(self):
        for key in self.dict.keys():
            if self.dict[key]['Price']<=self.budget:
                print('Amount left can buy you {}'.format(key))
                return

    def budgetZero(self):
        return self.budget==0
    
    def displayGrocery(self):
        print('GROCERY LIST is:')
        print('Product name','Quantity','Price',sep='\t')
        
        for key in self.dict.keys():
            print(key,str(self.dict[key]['Quantity'])+'kg',self.dict[key]['Price'],sep='\t')

budget = int(input('Enter Your Budget : '))
grocery = GroceryList(budget)
flag = True
while(flag):
    if grocery.budgetZero():
        print("Your balance is Zero can't continue")
        break
    print('1.Add an item')
    print('2.Exit')
    choice = int(input('Enter your choice : '))

    if choice==1:
        item = input('Enter product : ')
        quantity = input('Enter quantity (in kg) : ')
        price = int(input('Enter Price : '))
        grocery.addItem(item,quantity,price)
    else:
        grocery.itemInBudget()
        flag=False


grocery.displayGrocery()