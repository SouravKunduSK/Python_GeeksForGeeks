def missingNumber(arr):
    n = len(arr) + 1
    sum_till_n = n*(n+1)/2
    sum_of_array = 0
    for i in range(len(arr)):
        sum_of_array += arr[i]

    missing_number = sum_till_n - sum_of_array

    return int(missing_number)


def main():
    arr = [1]
    result = missingNumber(arr)
    print(result)

if __name__ == "__main__":
    main()