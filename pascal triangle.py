pascal= []
# To input the size of the pascal triangle
size = int(input("Enter the size of the pascal triangle:"))
# The i will keep on repeating until it reaches the size inputted
for i in range(size):
# Printing the []
    print(pascal)
    newlist=[]
# Add 1 in index[0] of every list
    newlist.append(1)
# The j will keep on repeating until it reaches the length of the list -1 in order for it not to be out of range
    for j in range(len(pascal)-1):
# To add the number from the curret value of j index with the value of j+1 index
        newlist.append(pascal[j]+pascal[j+1])
    newlist.append(1)
    pascal=newlist
