#  Author: AKHILESH

#  Approach:
#  Counting sort, like radix sort and bucket sort,
#  is an integer based algorithm (i.e. the values of the input
#  array are assumed to be integers). Hence counting sort is
#  among the fastest sorting algorithms around, in theory. The
#  particular distinction for counting sort is that it creates
#  a bucket for each value and keep a counter in each bucket.
#  Then each time a value is encountered in the input collection,
#  the appropriate counter is incremented. Because counting sort
#  creates a bucket for each value, an imposing restriction is
#  that the maximum value in the input array be known beforehand.

#  Implementation notes:
#  1] Since the values range from 0 to k, create k+1 buckets.
#  2] To fill the buckets, iterate through the input list and
#  each time a value appears, increment the counter in its
#  bucket.
#  3] Now fill the input list with the compressed data in the
#  buckets. Each bucket's key represents a value in the
#  array. So for each bucket, from smallest key to largest,
#  add the index of the bucket to the input array and
#  decrease the counter in said bucket by one; until the
#  counter is zero.

#  Best Case O(n+k); Average Case O(n+k); Worst Case O(n+k),
#  where n is the size of the input array and k means the
#  values range from 0 to k.

def countingSort(array):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        count[array[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    for i in range(0, size):
        array[i] = output[i]
data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)
