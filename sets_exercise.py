s1 = input("Sentence one: ").lower()
s2 = input("Sentence two: ").lower()

split_s1 = s1.split()
split_s2 = s2.split()

count_existence = 0

for i in split_s1:
  for k in split_s2:
    if i == k:
      count_existence = count_existence + 1
  
print(count_existence)
