def majorityElement(arr):
    length = len(arr)
    candidate = None
    count = 0
    # finding candidate by using boyer-moore algorithm
    for num in arr:
        if count == 0:
            candidate = num
        if candidate == num:
            count +=1
        else:
            count -=1

    # verifying the candidate
    count = 0
    for num in arr:
        if num == candidate:
            count +=1

    if count > length // 2:
        return candidate
    else:
        return -1

def main():
    arr = [3, 1, 3, 3, 2]
    result = majorityElement(arr)
    print(result)

if __name__ == "__main__":
    main()