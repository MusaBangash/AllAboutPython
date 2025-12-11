



while True:
    user= input("Enter input:")
    with open("drink.txt","a") as file:
        file.write(user+"\n")