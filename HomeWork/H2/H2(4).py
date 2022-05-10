# 4. Scrieti un program care citeste de la tastatura un nr natural "n", 
# si afiseaza n! (factorial). 6! = 1 * 2 * 3 * 4 * 5 * 6

n = input("n = ")
n = int(n)

f = 1
  
for i in range(1,n+1):
    f = f * i
      
print (f)
