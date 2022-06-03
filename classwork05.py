# key = input('your pin>>')
# key2 = input('your password>>')
# total = ((f'{key},{key2}'))
# me = []
# me.append(total)
# # print(me)
# if (key == key) or (key2 == key2):
#     print('successful')

# elif (key != key) and (key2 != key2):
#     print('error')

name = input("Enter your name>>")
pan =  ["*123#", "1234"]
pin = input('enter pin>>>')
password = input('enter password>>>')
if pin == pan[0] and password == pan[1]:
    print(f"{name} can login successfully")

else:
    print("you can't login")


