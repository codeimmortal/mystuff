list1 = [1,2,3,'himasnhu']

# three method are there in list
# append() , extend(), insert()

list1.append(4) # added at end 4
list1.append((2,0))
list1.extend((5,6,5)) # added multiple value
list1.insert(3,'insert') # added in position
print(list1)

# delete del , pop(),remove()

del list1[8] #del the 8 position value
print('del',list1)
a = list1.pop(4) #del the 4 position value also return it
print(list1)
list1.remove(5) # remove the value what is passed inside the remove
print(list1)

#searching the value

print('list[0:2]',list1[0:4])
print('list[0:4]',list1[0:4:2])
print('list[0:4]',list1[::-1])

# some basic method of list sort , count , index
list2 = [1,2,5,3,6,7]
list2.sort(reverse=True)
print(list2.index(2))
print(list2.count(3))