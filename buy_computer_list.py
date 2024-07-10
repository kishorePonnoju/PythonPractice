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
        print("Adding {}".format(current_choice))
        index = int(current_choice)-1
        Computer_list.append(available_list[index])
    else:
        print("Please add options fromthe list below:")
        for index,item in enumerate(available_list):
            print("{0}:{1}".format(index+1,item))

    current_choice = input()

print(Computer_list)

