#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length) # Create the hashtable based on size of the list given

    for i in range(0,length):
        hash_table_insert(ht,weights[i],i)
        #print(hash_table_retrieve(ht,weights[i]))
    
    for i in range(0,length):
        current_item_index = i #hash_table_retrieve(ht,weights[i])
        current_item = weights[hash_table_retrieve(ht,weights[current_item_index])]
        match_item_index = hash_table_retrieve(ht,limit-current_item)
        
        print(f"Current item is {current_item} at index {current_item_index}")
        if match_item_index:
            match_item = weights[match_item_index]
            print(f"{current_item} and {match_item} match")
            if current_item_index >= match_item_index:
                return (current_item_index, match_item_index)
            else:
                return (match_item_index, current_item_index)
        
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)

print(answer_2)