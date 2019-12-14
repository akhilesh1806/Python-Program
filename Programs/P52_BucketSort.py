# Author: AKHILESH
# This program will illustrate how to implement bucket sort algorithm

# Wikipedia says: Bucket sort, or bin sort, is a sorting algorithm that works by distributing the
# elements of an array into a number of buckets. Each bucket is then sorted individually, either using 
# a different sorting algorithm, or by recursively applying the bucket sorting algorithm. It is a
# distribution sort, and is a cousin of radix sort in the most to least significant digit flavour.
# Bucket sort is a generalization of pigeonhole sort. Bucket sort can be implemented with comparisons
# and therefore can also be considered a comparison sort algorithm. The computational complexity estimates
# involve the number of buckets.

#  Time Complexity of Solution:
#  Best Case O(n); Average Case O(n); Worst Case O(n)

def bucketSort(array): 
    bucket = [] 
    for i in range(len(array)): 
        bucket.append([])
        
    for j in array: 
        index_b = int(10 * j) 
        bucket[index_b].append(j) 
    
    for i in range(len(array)): 
        bucket[i] = sorted(bucket[i])
        
    k = 0
    for i in range(len(array)): 
        for j in range(len(bucket[i])): 
            array[k] = bucket[i][j] 
            k += 1
    return array 
array = [.42, .32, .33, .52, .37, .47, .51] 
print("Sorted Array in descending order is") 
print(bucketSort(array))
