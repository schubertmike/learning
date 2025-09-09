#the challenge here was to pick one of the indices in the list, and loop through the list to find it. Once found, set item_found variable to true and print item found

#list
dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

#pick which item I want to find, and initialize item_found to False
item_to_find = 'CAT'
item_found = False

#loop i times through the list
for i in dna_sequence:
#if i is equal to our item_to_find variable, then set item_found to true and stop looping
  if i == item_to_find:
    item_found = True
    break
#outside of the loop, if item found is true, print item found and what that item is
if item_found == True:
  print('Item Found:', i)
#otherwise, print item not found
else:
  print('Item not found.')
