def special_percentile(percent : int, numbers : list) -> float:
    sorted_numbers = sorted(numbers)
    the_place = (percent * len(sorted_numbers)) / 100
    return sorted_numbers[int(the_place)]
print(special_percentile(25, [40, 10, 20, 30]))
print(special_percentile(25, [50, 10, 40, 20, 30]))
print(special_percentile(50, [9, 1, 7, 3]))
