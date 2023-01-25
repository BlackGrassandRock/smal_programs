import random
import re
expt = []
x = []
rt = False

def rund_answ(st, fn, expt, rt):
      answ = str(random.randint(st, fn))
      for i in expt:  
          if i in answ:
                rund_answ(st, fn, expt, rt)
                rt = True
      if rt == False:
            x.append(answ)


st = int(input("Range start: "))
fn = int(input("End of range: "))
num_rand = int(input("How many numbers?: "))
num_expt = int(input("How many exceptions?; "))

for i in range(num_expt):
      a = input("Exceptions ")
      expt.append(a)
expt = list(map(str, expt))

for i in range(num_rand):
      answ = rund_answ(st, fn, expt, rt)
print(x)
