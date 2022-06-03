# my = []
# myy = []
# for i in range(9):
#     que = int(input("Enter number here: "))
#     my.append(que)
#     myy.append(my[-1]*que)
# print(myy)

# my = []
# myy = []
# for i in range(9):
#     que = int(input("Enter number here: "))
#     my.append(que)
# for m in my:
#     n = int(input('enter no>>'))


    # myy.append(my[-1]*que)
# print(myy)
    
# list = [i for i in range (9)]
# for j in list:
#     list2 = []
#     # m =list[-1]
#     n = j*list[-1]
#     list2.append(n)
# print(list2)
# # print(list2.append(n))


my = []
myy = []
for i in range(9):
    que = int(input('Enter number: '))
    my.append(que)
for j in my:
    k = j * my[-1]
    myy.append(k)
print(k)
