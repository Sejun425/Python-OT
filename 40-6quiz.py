def prime_number_generator(start,stop):
    for n in range(start,stop):
        is_prime=True
        for i in range(2,n-1):
            if n%i==0:
                is_prime=False
        if is_prime==True:
            yield n