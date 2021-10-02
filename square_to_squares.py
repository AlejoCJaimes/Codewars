def is_square(n):
    res = 0
    while n > 0 and res**2 < n:
        res += 1
    return True if n >= 0 and res**2 == n else False


if __name__ == '__main__':
    print(is_square(26))


# Task

# Given an integral number, determine if it's a square number:

# In mathematics, a square number or perfect square is an integer
#  that is the square of an integer; in other words, it is the product 
# of some integer with itself.