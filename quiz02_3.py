
input_key = ""
balance = 0
while(True):

    input_key = input("method:")
    if(input_key == "q"):
        break


    if(input_key == "d"):
        amount = int(input("Amount: "))
        balance = balance + amount
        print("Balance:", balance)
    elif(input_key == "w"):
        amount = int(input("Amount: "))
        balance = balance -  amount
        print("Balance:", balance)
    else:
        print("?")
