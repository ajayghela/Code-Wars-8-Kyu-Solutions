#Given an array of integers your solution should find the smallest integer.

#For example:

#Given [34, 15, 88, 2] your solution will return 2
#Given [34, -345, -1, 100] your solution will return -345
#You can assume, for the purpose of this kata, that the supplied array will not be empty.

#set the smallest value to none
#traverse throught set
#replace the smallest value
#if the value is not smaller ignore
#print smallest value.

def find_smallest_int(arr):
   i = arr[0]
   for val in arr:
        if val < i:
            i = val
   return i

def find_smallest_int(arr):
    print(arr.sort()[0])