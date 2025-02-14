def findDuplicates(arr):
    newList = []
    seen = set()
    if(len(arr)<=1):
        return []
    
    for num in arr:
        if num in seen:
            
            newList.append(num)
        else:
            seen.add(num)
    return newList

def main():
    arr = [2, 3, 1, 2, 3]
    result = findDuplicates(arr)
    print(result)

if __name__ == "__main__":
    main()