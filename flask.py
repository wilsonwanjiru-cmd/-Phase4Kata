class SmallestUnsortedSubarray:
    def find_unsorted_subarray(self, arr):
        n = len(arr)

        if n <= 1:
            return [0, 0]

        # Find the left boundary of the unsorted subarray
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        # If the array is already sorted, return [0, 0]
        if left == n - 1:
            return [0, 0]

        # Find the right boundary of the unsorted subarray
        right = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        # Find the minimum and maximum values in the unsorted subarray
        subarray_min = min(arr[left:right + 1])
        subarray_max = max(arr[left:right + 1])

        # Expand the left boundary to include any elements smaller than the minimum
        while left > 0 and arr[left - 1] > subarray_min:
            left -= 1

        # Expand the right boundary to include any elements larger than the maximum
        while right < n - 1 and arr[right + 1] < subarray_max:
            right += 1

        return [left, right]

    def render(self):
        arr = [1, 2, 3, 6, 4, 4]
        result = self.find_unsorted_subarray(arr)

        print("Original Array:", arr)
        print("Smallest Unsorted Subarray:", result)


# Example usage:
smallest_unsorted_subarray = SmallestUnsortedSubarray()
smallest_unsorted_subarray.render()
