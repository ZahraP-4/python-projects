#Program to test functions a to j.

#Define constant variables for testing.
TEST_ONE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]		    	
TEST_TWO =  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]   
TEST_THREE = [1, 25, 25, 4, 5, 4, 7, 60, 9, 10]                                                        
TEST_FOUR = [75, 54, 7, 9, 87, 8, 30]                                                        

def main():
    test_cases = [TEST_ONE, TEST_TWO, TEST_THREE, TEST_FOUR] 
    for test_num in range(len(test_cases)):
        print("Run test: ", test_num + 1)
        test_functions(test_cases[test_num])
        print("")

def test_functions(test) :
   print("The original data for all functions is: ", test)

   #a. Demonstrate swapping the first and last element.
   data = list(test)
   swapFirstLast(data)         #call this function      
   print("After swapping first and last: ", data)

   #b. Demonstrate shifting to the right.
   data = list(test)
   shiftRight(data)            #call this function
   print("After shifting right: ", data)

   #c. Demonstrate replacing even elements with zero.
   data = list(test)
   replaceEven(data)           #call this function
   print("After replacing even elements: ", data)

   #d. Demonstrate replacing values with the larger of their neighbors.
   data = list(test)
   replaceNeighbors(data)      #call this function
   print("After replacing with neighbors: ", data)

   #e. Demonstrate removing the middle element.
   data = list(test)
   removeMiddle(data)          #call this function
   print("After removing the middle element(s): ", data)

   #f. Demonstrate moving even elements to the front of the list.
   data = list(test)
   evenToFront(data)           #call this function
   print("After moving even elements: ", data)

   #g. Demonstrate finding the second largest value.
   print("The second largest value is: ", secondLargest(test))

   #h. Demonstrate testing if the list is in increasing order.
   print("The list is in increasing order: ", isIncreasing(test))

   #i. Demonstrate testing if the list contains adjacent duplicates.
   print("The list has adjacent duplicates: ", hasAdjacentDuplicate(test))

   #j. Demonstrate testing if the list contains duplicates.
   print("The list has duplicates: ", hasDuplicate(test))

#Complete the codes for the functions a. to j. below.

#a.
def swapFirstLast(data:list)->None :
    '''Swap the first and last element in a list.'''
    if len(data) >= 2:
        swap = data[0]
        data[0] = data[-1]
        data[-1] = swap


#b.
def shiftRight(data:list) ->None:
    '''Shift the elements to the right.'''
    length = len(data)
    if length >= 2:
        last_value = data[length - 1]
        index = length - 1
        while index > 0:
            data[index] = data[index - 1]
            index -= 1
        data[0] = last_value


#c.
def replaceEven(data:list)->None :
    '''Replace all even elements in the list with 0.'''
    index = 0
    while index < len(data):
        if data[index] % 2 == 0:
            data[index] = 0
        index += 1


#d.
def replaceNeighbors(data:list)->None :
    '''Replace each value with the larger of its neighbors.'''
    length = len(data)
    original_list = list(data)
    index = 1
    while index <= length - 2:
        left_neighbor = original_list[index - 1]
        right_neighbor = original_list[index + 1]
        if left_neighbor >= right_neighbor:
            data[index] = left_neighbor
        else:
            data[index] = right_neighbor
        index += 1


#e.
def removeMiddle(data:list) ->None:
    '''Remove the middle element or elements from a list.'''
    length = len(data)
    if length % 2 == 1:
        middle_index = length // 2
        del data[middle_index]
    else:
        right_index = length // 2
        left_index = right_index - 1
        del data[right_index]
        del data[left_index]


#f.
def evenToFront(data:list) ->None:
    '''Move even elements to the front of the list.'''
    even_numbers = []
    odd_numbers = []
    index = 0
    while index < len(data):
        if data[index] % 2 == 0:
            even_numbers.append(data[index])
        else:
            odd_numbers.append(data[index])
        index += 1
    data[:] = []
    even_index = 0
    while even_index < len(even_numbers):
        data.append(even_numbers[even_index])
        even_index += 1
    odd_index = 0
    while odd_index < len(odd_numbers):
        data.append(odd_numbers[odd_index])
        odd_index += 1


#g.
def secondLargest(data:list)->int :
    '''Identify the second largest value in a list.
        return the second largest value in the list'''
    largest = data[0]
    second = data[0]
    index = 1
    while index < len(data):
        if data[index] > largest:
            second = largest
            largest = data[index]
        elif data[index] > second and data[index] != largest:
            second = data[index]
        index += 1
    return second


#h.
def isIncreasing(data:list) -> bool:
    '''Determine whether or not the list is in increasing order.
        return True if the list is in increasing order, False otherwise'''
    index = 0
    result = True
    while index < len(data) - 1:
        if data[index] > data[index + 1]:
            result = False
        index += 1
    return result


#i.
def hasAdjacentDuplicate(data:list) -> bool:
    '''Determine if the list contains adjacent duplicate elements.
       return True if the list contains adjacent duplicates, False otherwise'''
    index = 0
    result = False
    while index < len(data) - 1:
        if data[index] == data[index + 1]:
            result = True
        index += 1
    return result


#j.
def hasDuplicate(data:list)->bool :
    '''Determine if the list contains duplicate elements.
        return True if the list contains duplicates, False otherwise'''
    seen_values = []
    index = 0
    result = False
    while index < len(data):
        current_value = data[index]
        if current_value in seen_values:
            result = True
        else:
            seen_values.append(current_value)
        index += 1
    return result

   
if __name__ == "__main__":
    main()
