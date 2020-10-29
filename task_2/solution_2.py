# your code here
user_input = input()
most_frequent_character = ''
max = 0
for a in user_input:
    count = 0
    for b in user_input:
        if b == a:
            count += 1
    if count > max:
        max = count
        most_frequent_character = a
print(most_frequent_character)
