
Shopping_list = ["milk",
                 "pasta",
                 "egg",
                 "spam",
                 "bread",
                 "rice"]
another_list = Shopping_list
print(id(another_list))
print(id(Shopping_list))

Shopping_list +=["cookies"]
print(Shopping_list)
print(id(Shopping_list))
print(id(another_list))