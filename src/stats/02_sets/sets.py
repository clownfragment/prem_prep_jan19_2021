
'''
list/set trick
-remove duplicates through sets
'''

lst = [6,5,4,3,2,4,1,6,8,7,9,6,3,5,4,6,9,8,7,6,5,4]

l1 = list(set(lst))

# print(l1)


def dedupe_in_order(lst):
    deduped = []

    for element in lst:
        if element not in deduped:
            deduped.append(element)
    return deduped

print(lst)
print(dedupe_in_order(lst))