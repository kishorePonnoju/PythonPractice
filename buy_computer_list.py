current_choice="_"
Computer_list=[]

while current_choice != "0":
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == "1":
            Computer_list.append("computer")
        elif current_choice == "2":
            Computer_list.append("monitor")
        elif current_choice == "3":
            Computer_list.append("Keyboard")
        elif current_choice == "4":
            Computer_list.append("mouse")
        elif current_choice == "5":
            Computer_list.append("mouse mat")
        elif current_choice == "6":
            Computer_list.append("hdmi Cable")    
    else:
        print("Please add options fromthe list below:")
        print("1: Computer")
        print("2: Monitor")
        print("3: Keyboard")
        print("4: mouse")
        print("5: mouser mat")
        print("6: hdmi Cable")
        print("0: to finish")

    current_choice = input()

print(Computer_list)

