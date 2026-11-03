def is_prime(x:int) ->int:
    if x < 2:
        return False
    else :
        for i in range(x,x-1):
            if x % i == 0:
                return False
        return True