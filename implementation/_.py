data = input()
alpha = []
val = 0

for x in data:
  if x.isalpha():
    alpha.append(x)
  else:
    val += int(x)
    
alpha.sort()

if val!=0:
  alpha.append(str(val))
  
print(''.join(alpha))
