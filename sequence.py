def strictly_increasing_sequence_if_delete_one_element(sequence):
    count = 0
    if len(sequence) > 1:
        for i in range(len(sequence) - 1):
            if count >= 2:
                return False
            else:
                if sequence[i] >= sequence[i + 1]:
                    if sequence[i] is sequence[0]:
                        count += 1
                    elif sequence[i - 1] >= sequence[i + 1]:
                        count += 2
                        return False
                    else:
                        count += 1
    return True

print(strictly_increasing_sequence_if_delete_one_element([0]))
print(strictly_increasing_sequence_if_delete_one_element([1, 1]))
print(strictly_increasing_sequence_if_delete_one_element([1, 2, 3]))
print(strictly_increasing_sequence_if_delete_one_element([1, 2, 1, 2]))
print(strictly_increasing_sequence_if_delete_one_element([1, 3, 2, 1]))
print(strictly_increasing_sequence_if_delete_one_element([1, 2, 3, 4, 5, 3, 5, 6]))
print(strictly_increasing_sequence_if_delete_one_element([40, 50, 60, 10, 20, 30]))
