my_dict = {"Taly": 1974, "Kat": 1995, "Lena": 1971}
print(my_dict)
print(my_dict["Taly"])
print(my_dict.get("July"))
my_dict.update({"Kira": 2014, "Nika": 1973})
a = my_dict.pop("Kat")
print(a)
print(my_dict)
my_set = {1, 2, 3, 2, 3, 3, "Собака", "Собака", True, (1, 2, 3)}
print(my_set)
my_set.add(4)
my_set.add("Кот")
my_set.remove(1)
print(my_set)