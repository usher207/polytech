def unique_words(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    unique_in_list1 = set1 - set2
    unique_in_list2 = set2 - set1
    
    unique_words_list = unique_in_list1.union(unique_in_list2)
    
    return list(unique_words_list)

list_a = ["apple", "banana", "cherry", "date"]
list_b = ["banana", "date", "fig", "grape"]

result = unique_words(list_a, list_b)

print("Слова, які є тільки в одному з списків:")
print(result)
