# def max_water(height):
#     left = 0
#     right = len(height) - 1
#     ans = 0

#     while left < right:
#         # calculate area
#         area = min(height[left], height[right]) * (right - left)
#         ans = max(ans, area)

#         # move pointer
#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1

#     return ans
# arr = [1,8,6,2,5,4,8,3,7]
# print(max_water(arr))   # Output: 49

height = [1,8,6,2,5,4,8,3,7]

left = 0                      # start pointer
right = len(height) - 1       # end pointer
max_area = 0                  # store max result
while left < right:
    width = right - left      # distance between lines

    # find smaller height
    min_height = min(height[left], height[right])

    area = width * min_height # calculate area

    max_area = max(max_area, area)  # update max

    # move pointer with smaller height
    
    if height[left] < height[right]:
        left += 1             # move left pointer
    else:
        right -= 1            # move right pointer
print("Max Water:", max_area)