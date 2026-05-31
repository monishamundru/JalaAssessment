# To Copy an array to another array
arr1=[1,2,3,4]
def copy(arr1):
    arr2=arr1.copy()
    return arr2
print(copy(arr1))

#To insert an element at a specific position in the array
arr=[1,2,3,4]
def insert_value(ele,pos,arr):
    arr.insert(pos,ele)
    return arr
ele=int(input("enter the element: "))
pos=int(input("enter the position: "))
print(insert_value(ele,pos,arr))

# Find the min and max values of an array 
arr = [4, 2, 8, 1, 9]
def min_max(arr):
    print("Minimum value:", min(arr))
    print("Maximum value:", max(arr))

min_max(arr)


# To reverse an array of integer values
arr = [4, 2, 8, 1, 9]
def reverse(arr):
    arr.reverse()
    return arr
print(reverse(arr))


# To find duplicate values in the array
arr=[1,2,2,3,4,5]
def duplicates(arr):
    dup=[]
    count=0
    for i in arr:
        if arr.count(i)>1:
            dup.append(i)
            return dup
print(duplicates(arr))

