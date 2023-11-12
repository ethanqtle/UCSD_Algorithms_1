#Order of growth: O(n^2)
#Why? Because there are two nested loops, each of which is O(n)
def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

#Order of growth: O(n)
#Why? Because the max function is O(n) and the remove function is O(n)
def my_max_pairwise_product(numbers):
    # find the largest number in numbers
    max1 = max(numbers)
    # find the next largest number in numbers 
    # by removing the largest number from numbers
    numbers.remove(max1)
    max2 = max(numbers)
    return max1 * max2 



if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(my_max_pairwise_product(input_numbers))

