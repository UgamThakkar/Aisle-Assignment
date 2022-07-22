import sys
from math import ceil

def Salestax(itemlist):
    exclusive = ['meds', 'book','chocolate','bar', 'food','pills','chocolates']

    finalList = []
    finalPrice = []
    oldSum = 0
    newSum = 0
    temp = 20
    
    for items in itemlist:
        tempListItem = items.split()
        
        tempListItem = [x.replace(' ','') for x in tempListItem]
        
        
        exemptFlag = False

        #checking if the item is exclusive
        for item in tempListItem:
            if item in exclusive:
                exemptFlag = True
        
        if exemptFlag:
            oldSum += float(tempListItem[-1])

            #getting the price of a single product/item
            priceofOne = float(tempListItem[-1])/float(tempListItem[0])

            newPrice = (float(tempListItem[-1])*0.05) + float(tempListItem[-1])

            newPrice = newPrice * float(tempListItem[0])

            newPrice = ceil(round(newPrice, 2) * temp)/temp

            newSum += newPrice

            tempString = ' '.join(tempListItem[:-1])
            
            print(tempString+' '+ str(newPrice))
            finalPrice.append(newPrice)
            print("1")
        
        else:
            #checking if the item is imported
            if 'imported' in tempListItem:
                oldSum += float(tempListItem[-1])
                priceofOne = float(tempListItem[-1])/float(tempListItem[0])

                newPrice = (float(priceofOne) *0.15) + float(priceofOne)

                newPrice = newPrice * float(tempListItem[0])

                newSum += newPrice
                newPrice =ceil(round(newPrice,2)*temp)/temp
                tempString = ' '.join(tempListItem[:-1])
                print(tempString+' '+str(newPrice))
                finalPrice.append(newPrice)
                print("2")
        
            else:
                #if none of the cases above are applicable then this else case would be executed
                oldSum+= float(tempListItem[-1])
                priceofOne = float(tempListItem[-1])/float(tempListItem[0])
                newPrice = (float(priceofOne) *0.10) + float(tempListItem[-1])

                newPrice = newPrice * float(tempListItem[0])
                newSum +=newPrice
                newPrice = ceil(round(newPrice,2)*temp)/temp
                tempString = ' '.join(tempListItem[:-1])
                print(tempString+' '+str(newPrice))
                finalPrice.append(newPrice)
                print("3")
    print("Sales Taxes:",round(((round(newSum, 2) * temp) / temp)-oldSum,2))
    print("total:", round(newSum, 2) * temp / temp)   

# itemlist = ['1 imported box of food at 10.00','1 imported bottle of perfume at 47.50']      
# itemlist =list(map(str, input("Enter Products: ").split()))
# itemlist = list(input("Enter Item: ").splitlines())
itemlist = sys.stdin.readlines().split()
Salestax(itemlist)