def Fibonacci(n):
   if n <= 1:
       return n
   else:
       return(Fibonacci(n-1) + Fibonacci(n-2))

nterms = 34
sum=0
#print("Fibonacci sequence:")
for i in range(nterms):
  #print(i, Fibonacci(i))
  if (Fibonacci(i)%2==0):
    sum = sum + Fibonacci(i)
print(sum)
