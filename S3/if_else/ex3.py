#sa se afiseze Numar acceptat daca acel numar face parte din intervalul [10,50]

numar = input("n=") #citim de la tastatura
numar = int(numar)  #cast la int

#if numar >= 10 and numar <= 50:
if numar < 10 or numar >50 : 
    #True and True
    #False and False
    print ("numar acceptat")
else:
    print("numar ne-acceptat")