# To add integer values of an array
arr=[1,2,3,4]
def array_sum(arr):
    total=0
    for i in range(len(arr)):
        total+=arr[i]
    print(total)
array_sum(arr)

# To calculate the average value of an array of integers
arr=[1,2,3,4]
def  Average(arr):
    total=0
    for i in range(len(arr)):
        total+=arr[i]
        avg = total/len(arr)
    print(avg)
Average(arr)    


# To find the index of an array elements
arr=[1,2,3,4]
print(arr.index(3))


# To test if array contains a specific values
arr=[1,2,3,4]
def find_ele(arr):
    ele=int(input("enter your element to find: "))
    if ele in arr:
        print("Existed")
    else:
        print("Does't exist")
find_ele(arr)


# To remove specific element from an array
arr=[1,2,3,4]
def remove_ele(arr):
    ele=int(input("enter element to remove: "))
    # for i in range(len(arr)):
    if ele in arr:
        arr.remove(ele)
        return arr
    else:
        return "element not found"
print(remove_ele(arr))

