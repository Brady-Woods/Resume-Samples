'''
Given an array of integers greater than zero, find if it is possible to split it in two (without reordering the elements), such that the sum of the two resulting arrays is the same. Print the resulting arrays.
https://careercup.com/question?id=5716403849003008
'''

numbers = [4, 5, 6, 2, 4, 6, 8, 3, 3, 2, 4, 6, 5, 3, 6, 7, 8, 6]
total = sum(numbers)
print(total / 2)
left = []
right = numbers.copy()
if (total % 2) == 0:
    for i in numbers:
        left.append(i)
        right.remove(i)
        if sum(left) == (total / 2):
            print(str(left) + " total: "+ str(sum(left)))
            print(str(right) + " total: " + str(sum(right)))
            break
        elif sum(left) > (total / 2):
            print("impossible, by adding " + str(i) + " to the list we exceeded the target of " + str(total / 2))
            print(str(left) + " total: "+ str(sum(left)))
            print(str(right) + " total: " + str(sum(right)))
            break
        else:
            print(str(left) + " total: "+ str(sum(left)))
            print(str(right) + " total: " + str(sum(right)))
else:
    print("impossible, sum of numbers is not even.")