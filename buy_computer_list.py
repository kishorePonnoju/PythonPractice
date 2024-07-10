current_choice="_"
Computer_list=[]
available_list=["Computer",
                "Monitor",
                "Keyboard",
                "Mouse",
                "Mouse mat",
                "hdmi"]
valid_choice = [str(i) for i in range(1,len(available_list)+1)]

while current_choice != "0":
    if current_choice in valid_choice:
        index = int(current_choice)-1
        choose_item = available_list[index]
        if choose_item in Computer_list:
            print("Removing {}".format(current_choice))
            Computer_list.remove(choose_item)
        else:
            print("Adding {}".format(current_choice))
            Computer_list.append(choose_item)
    else:
        print("Please add options fromthe list below:")
        for index,item in enumerate(available_list):
            print("{0}:{1}".format(index+1,item))

    current_choice = input()

print(Computer_list)

