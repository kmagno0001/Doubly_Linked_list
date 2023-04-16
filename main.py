from doubly_linked_list import Doubly_linked_list

lst = Doubly_linked_list(10)
lst.add(20)
lst.add(1, 0)
lst.add(3)
lst.add(5)
lst.add(2,1)
lst.add(22, 0)

print(lst)

lst.remove(22)
lst.remove(1)
lst.remove(5)

print(lst)