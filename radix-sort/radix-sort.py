# problem: given an array, sort in increasing order
# O(n) time O(n) auxilary space
import random

# Trick is to sort array according to digits(10 buckets)
# Starting from least significant digit going to most significant digit
def sort(arr):
  m = max(arr)
  exp = 1
  while(int(m/exp)>0):
    count_sort(arr,exp)
    exp*=10
  return arr

def count_sort(arr, exp):
  res = [0 for i in range(len(arr))]
  digits = [0,0,0,0,0,0,0,0,0,0]

  for num in arr:
    digits[int(num/exp)%10]+=1

  for i in range(1,10):
    digits[i] += digits[i-1]

  for i in range(len(arr)-1,-1,-1):
    res[digits[int(arr[i]/exp)%10]-1] = arr[i]
    digits[int(arr[i]/exp)%10]-=1
  for i in range(0,len(arr)):
    arr[i] = res[i]
  
arr = list(range(1000))
random.shuffle(arr)

print(arr)
sort(arr) 
print(arr)