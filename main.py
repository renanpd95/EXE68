import os,random,time

cont = 0
soma = 0
for n in range(1500):
  n = (random.randint (0,1000))
  cont = cont + 1
  #caso queira ver os número retire o -> # do time.sleep abaixo
  time.sleep(0.1) 
  print(n)
  
  soma = soma + n
  media = soma /cont
else:
  os.system('clear')
  
  print(f"Média:{media:.2f}")
  
  
  
