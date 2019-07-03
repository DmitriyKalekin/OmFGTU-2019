
# def walk():
#     print("гопник гуляет")

# def attack():
#     print("гопник атакует")    


# commands = {
#     "a": attack,
#     "w": walk,
#     "q": quit
# }

# try:
#     cmd = None
#     while cmd != "x":
#         print(">>> ", end="")
#         cmd = input()
#         print("вы ввели", cmd)
#         if cmd not in commands:
#             continue
        
#         invoker = commands[cmd]
#         invoker()
# except KeyboardInterrupt:
#     print("Выход произошёл по CTRL + С")        



l = []


s = 0
for i in range(0, 50):
    s += i
print(s)
    

l = [j for j in range(0, 50)]
d = { j:j**2 for j in range(0, 10)}
print(d)



print(sum(l))
