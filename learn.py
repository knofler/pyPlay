number = range(51)

comprehension = [i for i in number if i%2==0] 
slicing 	  = number[1:len(number):2]

print comprehension
print slicing

def is_prime(x):
    char = range(x)[2:]

    if x < 2:
        return False 

    elif x == 2:
        print True
        return True

    else:   
        for n in char:
            if (x % n == 0):
                print n
                return False
        else: 
            print True
            return True 
# note the else statement is still inside the other else statement though

is_prime(11)