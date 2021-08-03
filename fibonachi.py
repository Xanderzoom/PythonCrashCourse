def generate_next_fib(a, b, c):
  a = b
  b = c
  c = a + b
  return a, b, c

a=0
b=1
c=1

while c < 1000000:
    a,b,c = generate_next_fib(a,b,c)
    print(b,c,c/b,round(c/b,11))

