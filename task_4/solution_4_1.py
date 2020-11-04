# your code here
for smth in 'a'*10:
  user_input = input()
  numoftab = 0
  form = ''
  lemma = ''
  if user_input == '' or user_input[0] == '#':
    break
  else:
    for i in user_input:
      if i == '\t':
        numoftab += 1
      if numoftab == 1:
        form = form + i
      if numoftab == 2:
        lemma = lemma + i
  if form != lemma:
    print (form, lemma)
