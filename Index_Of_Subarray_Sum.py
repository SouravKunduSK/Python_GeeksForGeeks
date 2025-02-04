def subarray_sum(arr, target):
    length = len(arr)
    left = 0
    current_sum = 0

    for right in range(length):
        current_sum += arr[right]

        while current_sum>target and left<=right:
            current_sum -=arr[left]
            left +=1

            
        if current_sum == target:
            return [left+1, right+1]
        
    return [-1]

def main():
    arr = [1, 2, 3, 7, 5]
    target = 12
    sub_array = subarray_sum(arr, target)
    print(sub_array) 

if __name__ == "__main__":
    main()