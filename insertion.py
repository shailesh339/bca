def insertion(arr):
    n = len(arr)
    for i in  range(n):
        key = arr[i]
        prev = i-1
        while prev >= 0 and arr[prev]> key :
            arr[prev+1] = arr[prev]
            prev = prev -1
        arr [prev+1]= key
    print(arr) 

arr = [10,20,30,45,65,84,15,21,32,1,55,1,5,45,4,16,4,]
insertion(arr)      