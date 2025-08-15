t = int(input())

for _ in range(t):
  r1 = input()
  r2 = input()
  r3 = input()
  r4 = input()
  r5 = input()
  r6 = input()
  r7 = input()
  r8 = input()
  r9 = input()
  r10 = input()
  
  res = 0 
  
  for i in range(len(r1)):
    if r1[i] == "X":
      res += 1 
      
  for i in range(len(r2)):
    if r2[i] == "X":
      if i in (0,9):
        res += 1 
      else:
        res += 2 
  
  for i in range(len(r3)):
    if r3[i] == "X":
      if i in (0,9):
        res += 1 
      elif i in (1,8):
        res += 2
      else:
        res += 3 
  
  for i in range(len(r4)):
    if r4[i] == "X":
      if i in (0,9):
        res += 1 
      elif i in (1,8):
        res += 2
      elif i in (2,7):
        res += 3 
      else:
        res += 4 
  
  for i in range(len(r5)):
    if r5[i] == "X":
      if i in (0,9):
        res += 1 
      elif i in (1,8):
        res += 2
      elif i in (2,7):
        res += 3 
      elif i in (3,6):
        res += 4 
      else:
        res += 5 
  
  for i in range(len(r5)):
    if r6[i] == "X":
      if i in (0,9):
        res += 1 
      elif i in (1,8):
        res += 2
      elif i in (2,7):
        res += 3 
      elif i in (3,6):
        res += 4 
      else:
        res += 5 
  
  for i in range(len(r4)):
    if r7[i] == "X":
      if i in (0,9):
        res += 1 
      elif i in (1,8):
        res += 2
      elif i in (2,7):
        res += 3 
      else:
        res += 4 
  
  for i in range(len(r3)):
    if r8[i] == "X":
      if i in (0,9):
        res += 1 
      elif i in (1,8):
        res += 2
      else:
        res += 3 
  
  for i in range(len(r2)):
    if r9[i] == "X":
      if i in (0,9):
        res += 1 
      else:
        res += 2 
  
  for i in range(len(r1)):
    if r10[i] == "X":
      res += 1 
  
  print(res)

  
  
  
  
 
  
  