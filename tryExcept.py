

try:
    print(x)

except:
    print("There is error")


try:
    print(x)
except NameError:
    print("Naming erro")
except:
    print("error")