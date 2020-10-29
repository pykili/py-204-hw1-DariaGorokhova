# your code here
n = 0
sum = 0
for smth in 'a'*100:
  n = n + 1
  sum = sum + 2 * n - 1
if n ** 2 == sum:
  print('True')
else:
  print('False')  
