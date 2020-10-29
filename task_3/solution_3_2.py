# your code here
alphabet = ''
for smth in 'a'*10:
    user_input = input()
    for i in user_input:
        if i not in alphabet:
            alphabet = alphabet + i
print(alphabet)
