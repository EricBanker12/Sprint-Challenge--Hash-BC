#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # O(n)
    for i in range(length):
        hash_table_insert(ht, weights[i], i)

    # O(n)
    for i in range(length):
        other_weight = limit - weights[i]
        other_index = hash_table_retrieve(ht, other_weight)
        if other_index != None:
            if i > other_index:
                return [i, other_index]
            else:
                return [other_index, i]
    
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
