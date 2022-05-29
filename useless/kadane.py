from xmlrpc.client import MININT


def maxSum(arr):
    max = MININT
    curr = 0
    for i in range(len(arr)-1):
        curr = curr + arr[i]
        if curr > max:
            max = curr
        
        if curr < 0:
            curr = 0
    return max
    
    
arr = [5, -4, -2,6,1]
print(maxSum(arr))
