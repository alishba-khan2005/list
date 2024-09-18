list=["alishba","wariaa","maryam","eshal","mahnoor"]
print("--------INVITATION--------")
for names in list:
    print("you are invited to dinner",names)
print("maryam can't come to dinner")
guest_ncoming="maryam"
new_guest="adeena"
list.remove(guest_ncoming)
list.insert(2,new_guest)
print(list)
for names in list:
    print("you are invited to dinner",names)



#second code
def print_square():
    squares=[]
    for i in range(1,8):
        square=i*i
        squares.append(square)
    print(squares)
print_square()



#third code
list=[2,6,8,4,0,5,3,7]
list.sort()
print(list)
list.reverse()
print(list)
list.pop(1)#remove the iten at index mentioned
print(list)
list.pop()#remove the last item
print(list)
print(list.append(10))

def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")
describe_pet("chloe")



