class BinarySearch (list):
	list=[2,56,78, 98, 545,43
     a=length(list)
     b=step(list)

	def __init__(self, length, step):
		super(BinarySearch, self).__init__()
    	for item in range(1, length+1):
        	self.append(item * step)

        	self.length = len(self)

        	
        def Search(self , val):
            first = 0
            last = len(self) - 1
            index_val = 0
            found = False 

            count = 0

            while first <= last and not found:
                mid = (first + last) // 2
                if self[mid] == val:
                    found = True
                    index_val = mid
                else:
                    count += 1
                    if val < self[mid]:
                        last = mid - 1
                    else:
                        first = mid + 1
            return (count , index_val)



    
