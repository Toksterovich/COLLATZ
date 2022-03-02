from time import time
n = int(input())
first_num = n
steps = 0
start_time = time()
while n != 1:
  if n % 2 != 0:
    n = (n * 3) + 1
  elif n % 2 == 0:
    n = n // 2
  else:
    print ("ERROR")
  steps += 1
print (f"Число:", {first_num}, {n}, "Длина цепи:", {steps + 1})
print(time() - start_time)