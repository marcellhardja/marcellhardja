# No.1
def acronym(name):
    name = name.replace("-","")
    shortened = ""
    i = 0
    while i<len(name):
        if name[i] == name[i].upper():
            shortened += name[i]
        i += 1
    print(shortened)


# No.2
def modulo():
    list = []
    list1 = []
    for j in range (0,10):
        list.append(int(input("Enter a number")))
    for i in range (0,10):
        list1.append(list[i]%42)
    list1 = set(list1)
    return len(list1)


# No.3
def AliceNBob(n):
    Alice = 0
    Bob = 0
    for i in range (0,n):
        number = int(input("Enter a number"))
        if number % 2 == 0:
            Bob +=1
        if number % 2 != 0:
            Alice +=1

    if Alice > Bob:
        print("Alice is the winner")
    else:
        print("Bob is the winner")


# No.4
def CupsAndBalls(moves):
    move_list = []
    position = [1,0,0]
    for i in range(0,moves):
        move_list.append(str(input("Which set? A/B/C")).upper())
    for j in range(0,len(move_list)):
        if move_list[j] =="A":
            position[0], position[1] = position[1], position[0]
        if move_list[j] =="B":
            position[1], position[2] = position[2], position[1]
        if move_list[j] == "C":
            position[0], position[2] = position[2], position[0]


    print("The ball is in position " + str(position.index(1)+1) )



while True:
    ui = str(input("Choose 1 for no.1, 2 for no.2, 3 for no.3, 4 for no.4; Type exit to finish): "))
    if ui == "1":
        acronym(str(input("Enter name")))
    elif ui == "2":
        print(modulo())
    elif ui == "3":
        AliceNBob(int(input("Enter number of rounds")))
    elif ui == "4":
        CupsAndBalls(int(input("Insert how many moves: ")))
    elif ui == "exit":
        break


