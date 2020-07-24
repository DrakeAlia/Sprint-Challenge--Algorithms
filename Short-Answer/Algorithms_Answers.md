#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 
* My Answer: O(n)
* My Reason:
The loop is set up to run through a length that is n * n * n, which is equivalent to n^3. This would indicate cubic time, a is incremented by n*n on each run of the loop, not 1. Therefore, the difference between this increment and the overall loop length is n. So our runtime is for this problem would be O(n)

* Problem:
a = 0
    while (a < n * n * n):
      a = a + n * n

b)
* My Answer: O(n log n)
* My Reason:
The outer loop is looping through n, while the inner loop is looping through log n, as the pointer is being multiplied by 2 each time, instead of incrementing by 1.

* Problem:
sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

c)
* My Answer: O(n)
* My Reason:
This algorithm is recursive, however it is only calling itself once, and thus basically making a for loop that counts n down by 1 each time through.

* Problem:

def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)


## Exercise II

* Question:

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

* My Response:

This problem is best solved using a binary search, using binary search we can reduce the search to log n time. The floors are acting like a sorted array, so where the bottom floors are non-egg-breaking floors and the top floors are egg-breaking floors. Here we are simply trying to find the point at which they transition. We would start by dropping an egg from the middle floor and the middle floor + 1. 

If the lower of the two does not break, but the higher one does break than f is the middle floor + 1. However if both eggs were to break then we would go halfway towards ground level and repeat the process with two adjacent floors there. If both eggs do not break in our initial drop, we would go halfway towards the roof and drop from two adjacent floors there.

We would keep subdividing in this manner, halving the number of floors we are looking at until we find the floor that is the tipping point for eggs breaking. The runtime of this solution would be O(log n)
