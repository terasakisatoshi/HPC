def f(x):
  return 4 / ( 1.0 + x**2 )

n = 10000000
sum = 0
step = 1.0 / n

for i in range(0, n):
  x = ( i + 0.5 ) * step
  sum += f(x)

pi = sum * step

print(pi)