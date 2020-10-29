# your code here
string = input()
is_palindrom = False
palindrom = ''
for i in string:
  palindrom = i + palindrom
if string == palindrom:
  is_palindrom = True
print(is_palindrom)
