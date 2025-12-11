



def read_menu(filename):
    f=open(filename)
    temp= f.readlines()
    results=[]
    for item in temp:
        new_item=item.strip()
        results.append(new_item)

    return results

drinks=read_menu("drink.txt")
flavors=read_menu("flaovr.txt")


def menu(choices,title):
    print(title)

    for i,c in enumerate(choices,start=1):
        print(i,c)
        
    while(True):

        try:

            choice= int(input("enter your choices: "))

            if 1<=choice<=len(choices):
                return choices[choice-1]
            else:
                print(f"Please enter number between 1 and {len(choices)}")
        
        except:

            print("Invalid Input! Please enter only number")


dri= menu(drinks,"Musa's Coffee Shop Drinks Menu")
print(dri)


