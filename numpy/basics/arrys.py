import numpy as np

# creating arrays in numpy

arr = np.array([1, 2, 3, 4, 5, 6])


# copying the array
# copy creates a new array and changes doesnt affect the original array (deosnt own the data)
# view doesnot create a new array and changes made in view affects and alters the original array (owns the data)
new_arr = arr.copy()
new_arr[0] = 33
newarr = arr.view()
newarr[0] = 52
print(new_arr)
print(newarr)
print("owns the data:", new_arr.base)
print(arr)

# reshape from 1d array to 2d array
print(arr.reshape(2, 3))

print(arr[0])  # indexing in 1d array

# creating tuple in numpy

myTuple = np.array((1, 2, 3, 4, 5, 6))
x = list(myTuple)
x.pop()
myTuple = tuple(x)
print(myTuple)

# dimensions

# 2d array

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d[1, 2])
print("share of 2d array", arr2d.shape)

# converting 2d array to 1d
print(arr2d.reshape(-1))

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9,], [10, 11, 12]]])
print(arr3d[0, 1, 2])
print("shape of array: ", arr3d.shape)

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr.ndim)
print(arr2d.ndim)
print(arr3d.ndim)

# creating a higher dimension array

arr_any_dim = np.array([1, 2, 3, 4], ndmin=6)
print(arr_any_dim)

# creating arrays with defined data types

defined_array = np.array([1, 2, 3, 4, 5], dtype="S")
print(defined_array)

# converting the data type of a array

arr_float = np.array([1.2, 2.5, 4.6])
arr_int = arr_float.astype(int)
print(arr_int)

# splitting the array
array_to_spit = [1, 2, 3, 4, 5, 6, 7]
splitted_array = np.array_split(array_to_spit, 4)
print(splitted_array)
for i in range(len(splitted_array)):
    print(splitted_array[i])

# searchnig in an array
array_to_seacrh = np.array([1, 23, 4, 5, 2, 412, 21, 2, 2])
x = np.where(array_to_seacrh == 2)

sorted_array = np.sort(array_to_seacrh)
# it tells the index where the value should be inserted to maintain the sorted array
y = np.searchsorted(sorted_array, 2, side="right")
print("sorted Array: ", sorted_array)
print("index of 2s from right after sorting the array: ", y)
print("index of 2s: ", x)
