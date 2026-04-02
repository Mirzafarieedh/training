def f(x):
  return x**2
x = 2
#print for different h values
for h in [0.1,0.01,0.001]:
  slope = (f(x+h) - f(x)) / h
  print("h =", h, "slope=", slope)
