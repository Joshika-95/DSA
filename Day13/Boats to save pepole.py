people = [3,2,2,1]
limit = 3
people.sort()
left, right = 0, len(people) - 1
boats = 0

while left <= right:
    if people[left] + people[right] <= limit:
        left += 1  # take light person
    right -= 1  # always take heaviest
    boats += 1  # one boat used
print(boats)  # Output: 3
