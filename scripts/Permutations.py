from itertools import permutations

my_list = [1, 2, 3, 4]

list_of_permutations = permutations(my_list)
for permutation in list_of_permutations:
    print(permutation)
