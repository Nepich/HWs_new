def some_func(some_list):
    some_dict = {}
    for element in some_list:
        if element not in some_dict:
            some_dict[element] = 1
        else:
            some_dict[element] += 1
    max_entries = max(some_dict.values())
    answer = []
    for key, value in some_dict.items():
        if value == max_entries:
            answer.append(key)
    return answer
