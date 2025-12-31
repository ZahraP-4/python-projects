#This program performs several set operations using the given sets 

#Data
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

#Processing/Output
set_a = set1 ^ set2
print('a.', set_a)
set_b = ((set1 - set2 - set3) |
         (set2 - set1 - set3) |
         (set3 - set1 - set2))
set_b = list(set_b)
set_b.sort()
set_b = set(set_b)
print('b.', set_b)
set_c = ((set1 & set2) | (set1 & set3) | (set2 & set3))
print('c.', set_c)
all_numbers = set(range(1, 26))
set_d = all_numbers - set1
print('d.', set_d)
set_e = all_numbers - (set1 | set2 | set3)
print('e.', set_e)
set_f = all_numbers - (set1 & set2 & set3)
print('f.', set_f)
