'''highest peak with linear search'''
def linear_peak(A):
    max_peak_value = max_peak_index = -1
    peak = A[0]
    index = 0
    for i in range(1, len(A)-1):
        prev = A[i-1]
        curr = A[i]
        nxt = A[i+1]
        if curr > prev and curr > nxt:
            index = i
            peak = curr
        if peak > max_peak_value:
            max_peak_value, max_peak_index = peak, index
    if A[len(A)-1] > peak:
        return A[len(A)-1], len(A)-1
    return max_peak_value, max_peak_index

A = [35,5,20,2,90,25,80,25,115,40]
print(A,"\n",linear_peak(A))
#SAN linear search

'''highest peak with binary search'''
def binary_peak():
      def find_peak(A):
      if not A:
            return -1
      left,right=0,len(A)-1
      while left+1<right:
            mid=left + (right-left) //2
            if A[mid]<A[mid-1]:
                  right = mid
            elif A[mid]<A[mid+1]:
                  left=mid
            else:
                  return mid
      mid =left if A[left] > A[right] else right
      return mid

A=[35,5,20,2,40,25,80,25,15,40]
peak=find_peak(A)
print(A,"\n",A[peak])


#Rushik Vadher


def find_peak():
      pass

def largest_tasks():
      pass

def huffman_coding():
      pass
