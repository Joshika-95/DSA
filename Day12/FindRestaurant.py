def findRestaurant(list1, list2):
    d = {}
    
    # store list1 items with index
    for i in range(len(list1)):
        d[list1[i]] = i

    min_sum = 100000
    result = []

    # check list2
    for j in range(len(list2)):
        if list2[j] in d:
            s = j + d[list2[j]]
            
            if s < min_sum:
                min_sum = s
                result = [list2[j]]
            elif s == min_sum:
                result.append(list2[j])

    return result


# Example
list1 = ["Shogun", "KFC", "Burger King"]
list2 = ["KFC", "Shogun", "Burger King"]

print(findRestaurant(list1, list2))