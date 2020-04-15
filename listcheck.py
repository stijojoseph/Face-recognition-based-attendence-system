test_list1 = ['a','b','c'] 
test_list2 = ['c','a','b'] 
  
# printing lists 
print ("The first list is : " + str(test_list1)) 
print ("The second list is : " + str(test_list2)) 
  
# sorting both the lists 
test_list1.sort() 
test_list2.sort() 
  
# using == to check if  
# lists are equal 
if test_list1 == test_list2: 
    print ("The lists are identical") 
else : 
    print ("The lists are not identical") 