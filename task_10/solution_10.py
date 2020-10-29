# your code here
string = input()
is_palindrom = 'Not a palindrome'
palindrom = ''
for i in string:
  palindrom = i + palindrom
if string == palindrom:
  is_palindrom = 'Palindrome'
print(is_palindrom)
