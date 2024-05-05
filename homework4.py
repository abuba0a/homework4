tuple_=(67,'Груша',[87,'DOG',4,25],True,1)
immutable_var = tuple_
print(immutable_var)
tuple_[2][1]='CAT'
print('immutable_list: ',immutable_var)
print()
list_=[67,'Груша',87,'DOG',True,1]
mutable_list=list_
print(mutable_list)
list_[1]='Яблоко'
print(mutable_list)
list_.extend('CAT')
print(mutable_list)
list_.remove(True)
list_.extend(['CAT'])
list_.remove('C')
list_.remove('A')
list_.remove('T')
print('Mutable list: ',mutable_list)
