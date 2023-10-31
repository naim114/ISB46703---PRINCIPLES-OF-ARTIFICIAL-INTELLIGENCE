import random

# # Exercise 1
# print("\n***********************")
# print("Exercise 1")
# print("***********************\n")


# def select_second_element(x):
#     if len(x) >= 2:
#         return x[1]
#     else:
#         return None


# ans_e1 = select_second_element(input("Please enter some text: "))

# print(ans_e1)


# # Exercise 2
# print("\n***********************")
# print("Exercise 2")
# print("***********************\n")

# teams_list = [
#     ["Guardiola", "Ederson", "De Bruyne", "Ake", "Cancelo", "Walker",
#         "Foden", "Silva", "Grealish", "Rodrigo", "Haaland", "Alvarez"],
#     ["Arteta", "Ramsdale", "Odegaard", "Saliba", "White", "Zinchenko",
#         "Jorginho", "Havertz", "Rice", "Saka", "Martinelli", "Jesus"],
#     ["Ten Hagg", "Martinez", "Onana", "Shaw", "Varane", "Casemiro",
#         "Fernandes", "McTominay", "Antony", "Sancho", "Rashford"],
# ]


# def best_team_manager(best_team):
#     return best_team[0]


# def second_best_team_random_player(second_team):
#     return random.choice(second_team)


# def third_best_team_captain(third_team):
#     return third_team[1]


# print("Best team's manager: " + best_team_manager(teams_list[0]))
# print("Second best team's random player: " +
#       second_best_team_random_player(teams_list[1]))
# print("Third team's team captain: " +
#       third_best_team_captain(teams_list[2]))


# # Exercise 3
# print("\n***********************")
# print("Exercise 3")
# print("***********************\n")


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[0]
#     less = [x for x in arr[1:] if x <= pivot]
#     greater = [x for x in arr[1:] if x > pivot]

#     return quick_sort(less) + [pivot] + quick_sort(greater)


# randomList = random.sample(range(1, 1000), 100)
# sortedList = quick_sort(randomList)
# print(sortedList)

# Exercise 4
# print("\n***********************")
# print("Exercise 4")
# print("***********************\n")

# purchase_date = ("25-Jan-21", "25-Jan-21", "25-Jan-21", "25-Jan-21")
# purchase_price = (43.5, 42.8, 42.1, 37.58)
# shares = (25, 50, 75, 100)
# symbol = ("CAT", "DD", "EK", "GM")
# current_price = (92.45, 51.49, 34.87, 37.58)

# cat = ("25-Jan-21", 43.5, 25, "CAT", 92.45)
# dd = ("25-Jan-21", 42.8, 50, "DD", 51.49)
# ek = ("25-Jan-21", 42.1, 75, "EK",  34.87)
# gm = ("25-Jan-21", 37.58, 100, "GM", 37.58)
# portfolio = [cat, dd, ek, gm]

# # Exercise 5
# print("\n***********************")
# print("Exercise 5")
# print("***********************\n")

# print("<<<<<<< Exercise 5.1 >>>>>>>\n")

# dict_one = {
#     "name": "Router1",
#     "IP": "1.1.1.1",
#     "username": "zframes",
#     "pwd": "zframes"
# }


# def get_key(key: str):
#     return str(dict_one.get(key))


# def check_key_add(key: str):
#     if key in dict_one:
#         print("Key exist! The value is: " + get_key(key))
#     else:
#         new_value = input(
#             "Key doesnt exist. Please enter the value to add to existing dictionairy: ")
#         dict_one[key] = new_value

#         print("Dictionairy updated! here's the new look: ", dict_one)

# check_key_add(input("Please enter key: "))

# print("\n<<<<<<< Exercise 5.2 >>>>>>>\n")

# dict_two = {
#     "Ethernet0": ["1.1.1.1", "up"],
#     "Ethernet1": ["2.2.2.2", "down"],
#     "Serial0": ["3.3.3.3", "up"],
#     "Serial1": ["4.4.4.4", "up"],
# }


# def get_interface_status(interface: str):
#     if interface in dict_two:
#         return dict_two.get(interface)[1]
#     else:
#         return "None"


# status = get_interface_status(input("Enter interface to get status: "))

# print("Status: " + status)

# def get_status_up():
#     for i in dict_two:
#         if dict_two.get(i)[1] == "up":
#             print(i + ": " + dict_two.get(i)[0])


# print("\nActive interface: \n")

# get_status_up()


# def add_to_dict_two():
#     print("\n")
#     key: str = input("Enter key for new entry: ")
#     ip: str = input("Enter ip for new entry: ")
#     status: str = input("Enter status for new entry: ")

#     dict_two[key] = [ip, status]

#     print("Current dict: \n")

#     print("Dictionairy updated! here's the new look: ", dict_two)


# add_to_dict_two()
