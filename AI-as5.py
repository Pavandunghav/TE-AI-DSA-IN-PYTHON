# ass5
# selection sort in python

def selection(n, li):

    sorted = []

    for i in range(n):
        min = li[i]

        for j in range(i+1, n):

            if (li[j] < min):

                min = li[j]

        sorted.append(min)

    return (sorted)


def bubble(n, li):

    # sorted = []

    for i in range(n):

        for j in range(n-i-1):

            if (li[j] > li[j+1]):

                li[j], li[j+1] = li[j+1], li[j]

    return (li)
    # print(sorted)


def shellSort(n, arr):

	# Start with a big gap, then reduce the gap
	n = len(arr)
	gap = n/2

	# Do a gapped insertion sort for this gap size.
	# The first gap elements a[0..gap-1] are already in gapped
	# order keep adding one more element until the entire array
	# is gap sorted
	while gap > 0:

		for i in range(gap, n):

			temp = arr[i]

			j = i
			while j >= gap and arr[j-gap] > temp:
				arr[j] = arr[j-gap]
				j -= gap

			arr[j] = temp
		gap /= 2

return(arr)





# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(n,arr):
	
	if (n := len(arr)) <= 1:
	return
	for i in range(1, n):
		
		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >=0 and key < arr[j] :
				arr[j+1] = arr[j]
				j -= 1
		arr[j+1] = key
  
  
    return(arr)




# Function to find the partition position
def partition(array, low, high):

	# choose the rightmost element as pivot
	pivot = array[high]

	# pointer for greater element
	i = low - 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1



def quickSort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quickSort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quickSort(array, pi + 1, high)

    return arr

















    
    

def main():

    n = int(input("ENTER THE NO. OF ELEMENT :"))

    li = []
    for i in range(n):
        el = int(input("\nENTER THE ELEMENT:"))
        li.append(el)

    flag = "Y"

    while (flag != "N"):

        print("SELECT FROM THE BELOW:")
        print(('''       1]SELECTION
        2]BUBBLE 
        3]INSERTION
        
        4]QUICK
        5]SHELL'''))
        
        ch=int(input(""))

        if (ch == 1):
            
            
            print(f"BEFORE SORTING :{li}")
            print(f"LIST AFTER THE SORTING{selection(n, li)}")
            

        elif (ch == 2):

            bubble(n, li)
            
            print(f"THE LIST BEFORE THE SORTING: {li}")
            print(f"THE LIST AFTER THE SORTING :{bubble(n,li)}")
            
        

        elif (ch == 3):

            insertionsort(n, li)
            
        
        
        elif (ch == 4):

            quicksort(n, li)
            
            
            
        
        
        elif (ch == 5):

            shellsort(n, li)
              
            
        
            
        
            

        flag = str(input("Do You Want To Conitnue(Y/N)?"))


main()
