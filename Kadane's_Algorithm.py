def maxSubarraySum(arr):
    max_sum = arr[0]
    current_sum = 0

    for value in arr:
        current_sum += value
        max_sum = max(current_sum, max_sum)
        if(current_sum<0):
            current_sum = 0
        
    return max_sum






def main():
    arr = [2, 3, -8, 7, -1, 2, 3]
    sum = maxSubarraySum(arr)
    print(sum)

if __name__ == "__main__":
    main()