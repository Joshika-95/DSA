arr1=["Violet","Red","Blue","Green","Black"]
arr2=["Violet","Black","Pink","Orange","Yellow"]
matched = []
unmatched = []

for x in arr1:
    if x in arr2:
        matched.append(x)
    else:
        unmatched.append(x)

for x in arr2:
    if x not in arr1:
        unmatched.append(x)

print("Matched:", matched)
print("Unmatched:", unmatched)
