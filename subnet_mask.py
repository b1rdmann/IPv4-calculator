import sys
def doubl(ipadd, octet):
    for i in range(1, len(octet) + 1):
        if ipadd % 2 == 0:
            octet[-i] = 0
        else:
            octet[-i] = 1
        ipadd = ipadd // 2

def mask_doubl(mask, maskDouble):
    for i in range(0, len(maskDouble)):
        if i < mask:
            maskDouble[i] = 1
        else:
            maskDouble[i] = 0

def mask_apply(octet, maskDouble):
    for i in range(0,8):
        if octet[i] == maskDouble[i]:
            continue
        else:
            octet[i] = 0
def broadcast(octet, maskDouble):
    for i in range(0,8):
        if maskDouble[i] == 1:
            continue
        else:
            octet[i] = 1
def undouble(octet):
    add = 0
    for i in range (1,9):
        add += (2 ** (i - 1)) * octet[-i]
    return (add)


while True:
    print('Enter IP Address')
    try:
        a, b, c, d = map(int, input().split('.'))
        if a > 255 or b > 255 or c > 255 or d > 255:
            print ('Wrong value, octets cannot be igher than 255')
            continue
    except ValueError:
        print ('Wrong value, please enter IP address in format: x.x.x.x')
        continue
    octet1 = [0] * 8
    octet2 = [0] * 8
    octet3 = [0] * 8
    octet4 = [0] * 8
    doubl(a, octet1)
    doubl(b, octet2)
    doubl(c, octet3)
    doubl(d, octet4)
    print('Subnet mask in format /x')
    while True:
        try:
            mask = int(input())
        except ValueError:
            print ('Wrong value')
            continue
        if mask < 32:
            maskDouble = [0] * 32
            maskDouble1 = [0] * 8
            maskDouble2 = [0] * 8
            maskDouble3 = [0] * 8
            maskDouble4 = [0] * 8
            mask_doubl(mask, maskDouble)
            for i in range(0, 32):
                if i <= 7:
                    maskDouble1 [i] = maskDouble [i]
                elif i <= 15:
                    maskDouble2 [i - 8] = maskDouble [i]
                elif i <= 23:
                    maskDouble3 [i - 16] = maskDouble [i]
                elif i <= 32:
                    maskDouble4 [i - 24] = maskDouble [i]
            mask_apply(octet1, maskDouble1)
            mask_apply(octet2, maskDouble2)
            mask_apply(octet3, maskDouble3)
            mask_apply(octet4, maskDouble4)
            a = undouble(octet1)
            b = undouble(octet2)
            c = undouble(octet3)
            d = undouble(octet4)
            print('Subnet: ')
            print(a, b, c, d, sep = '.')
            print('Hostmin: ')
            print(a, b, c, d + 1, sep ='.')
            print('Hostmax: ')
            broadcast(octet1, maskDouble1)
            broadcast(octet2, maskDouble2)
            broadcast(octet3, maskDouble3)
            broadcast(octet4, maskDouble4)
            a2 = undouble(octet1)
            b2 = undouble(octet2)
            c2 = undouble(octet3)
            d2 = undouble(octet4)
            print(a2, b2, c2, d2 - 1, sep ='.')
            print('Broadcast: ')
            print(a2, b2, c2, d2, sep ='.')
            print('Number of nodes: ')
            if mask == 31:
                print(2)
            else:
                numberOfHosts = ((2 ** (32 - mask)) - 2)
                print(numberOfHosts)
        elif mask == 32:
            print('Subnet: ')
            print(a, b, c, d, sep = '.')
            print('Hostmin: ')
            print(a, b, c, d, sep ='.')
            print('Hostmax: ')
            print(a, b, c, d, sep ='.')
            print('Broadcast: ')
            print(a, b, c, d, sep ='.')
            print('Number of nodes: ')
            print(1)
        else:
            print('Wrong mask value')
            continue
        break
    while True:
        print('Wish to continue? (y/n)')
        answer = str(input())
        if answer == 'y':
            break
        elif answer == 'n':
            sys.exit()
        else:
            continue
