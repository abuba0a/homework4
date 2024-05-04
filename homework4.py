tuple_=(67,'Груша',[87,'DOG',4,25],True,1)
immutable_var = tuple_
print(immutable_var)
tuple_[2][1]='CAT'
print('immutable_list: ',immutable_var)
print()
food=[67,'Груша',87,'DOG',True,1]
mutable_list=food
print(mutable_list)
food[1]='Яблоко'
print(mutable_list)
food.extend('CAT')
print(mutable_list)
food.remove(True)
food.extend(['CAT'])
print('mutable_list: ',mutable_list)
