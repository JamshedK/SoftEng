def sum(array):
    total = 0
    for num in array:
        total += num
    return total

def product (array):
    res = 1
    for num in array:
        res = res = res * num
    return res

def reverse(array):
    return array[::-1]

if __name__ == '__main__':
    array = [1,2,3,4]
    print(sum(array))
    print(product(array))