
def distinct_list(items):
    result = []

    for item in items:
        if item not in result:
            result.append(item)

    return result

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]

print("Original List:", sample_list)
print("Distinct List:", distinct_list(sample_list))