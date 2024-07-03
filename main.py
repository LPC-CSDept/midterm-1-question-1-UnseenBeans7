

def main():
    number = []
    evencnt = 0

    for i in range(10):
        number.append(int(input('Enter a number: ')))

    """
    ########################################
    Code Your Program here
    ########################################
    """
    consecutive = 0
    for num in number:
        if num % 2 == 0:
            consecutive += 1
        else:
            if consecutive >= 2:
                evencnt += 1
            consecutive = 0
                
    if consecutive >= 2:
        evencnt += 1
        
    print(evencnt)

    ########################################
    # Do not delete the return statement
    ########################################
    return evencnt


if __name__ == '__main__':
    main()

