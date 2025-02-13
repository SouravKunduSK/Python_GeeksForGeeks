def leaders(arr):
    length = len(arr)
    leaders_list = []
    leader = arr[-1]
    leaders_list.append(leader)

    for i in range(length-2,-1,-1):
        if arr[i] >= leader:
            leader = arr[i]
            leaders_list.append(leader)

    result = leaders_list[::-1]
    return result

def main():
    arr = [30, 10, 10, 5]
    result = leaders(arr)
    print(result)

if __name__ == "__main__":
    main()