def find_missing(list1 , list2):

    if isintance(list1 == list2 == 0, int):
        return 0 ("should return 0 for empty list")
    elif list1 == list2:
        return 0 ("should return 0 for lists with the same entries")
    else:
    	for element in list1:
    		if element not in list2:
    			return element

    print(find_missing([45,65,1,3],[45,65,1,3,7]))
 