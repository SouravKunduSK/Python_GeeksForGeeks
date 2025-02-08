def getSecondLargest(arr):

    if(len(arr)<2):
        return -1
    
    first = float('-inf')
    second = float('-inf')
    for num in arr:
        if(num>first):
            second = first
            first = num

        elif(num>second and num !=first):
            second = num

    if(first == second or second == float('-inf')):
        return -1
    else:
        return second
        

def main():
    arr = [10,10,5]
    second_largest = getSecondLargest(arr)
    print(second_largest)

if __name__ == "__main__":
    main()