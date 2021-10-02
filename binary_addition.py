def binary(decimal):
    binary_num = []
    swape = -1
    while swape!=0:
        binary_num.append(decimal%2)
        swape = decimal //2
        decimal = decimal //2
    binary_num = binary_num[::-1]     
    return ''.join(map(str, binary_num))

        

def add_binary(a,b):
    return binary(a+b)

if __name__ == '__main__':
    print(add_binary(5,9))