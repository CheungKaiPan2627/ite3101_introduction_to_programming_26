def is_prime(x:int) ->int:
    if x < 2:
        return False
    else:
        for n in range(x,x-1):
            if x % n == 0:
                return False
        return True