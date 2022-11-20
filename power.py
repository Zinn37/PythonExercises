def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp-1)

print(power(2, 0))
print(power(2, 2)) 
print(power(2, 4))
print(power(3, 10))
