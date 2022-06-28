from termcolor import colored

a = input(colored('--------> ', 'green' ))

def ha(first , secend , third):
    global multiplicate , difference

    if secend - first == third - secend:
        multiplicate = int(secend - first)
        difference =  first - (multiplicate * 1) 

        if multiplicate * 1 == first and multiplicate * 2 == secend and multiplicate * 3 == third:
            return True
        else:
            if (multiplicate * 1) + difference == first and (multiplicate * 2) + difference == secend and (multiplicate * 3) + difference:
                return True
    return False

def fibonachi(first , secend , third):
    if first + secend == third:
        return True

    return False

def tavan(first , secend , third):
    global difference , multiplicate

    for i in range(2 , 11):
        if 1 ** i == first and 2 ** i == secend and 3 ** i == third:
            multiplicate = i
            return True
        else:
            if (1 ** i) - first == (2 ** i) - secend and (2 ** i) - secend == (3 ** i) - third:
                difference = first - (1 ** i)
                if (1 ** i) + difference == first and (2 ** i) + difference == secend and (3 ** i) + difference == third:
                    multiplicate = i
                    return True
    return False

def mosalas(first , secend , third):
    if first == 1 and secend == 3 and third == 6:
        return True
    return False

pattern = []
answer = []
difference = 0
multiplicate = 0
tru = False

pattern = a.split(',')

for i in range(len(pattern)):
    pattern[i] = int(pattern[i])

first = pattern[0]
secend = pattern[1]
third = pattern[2]
a , b = first , secend

if ha(first, secend , third) == True:
    for i in range(1 , 11):
        answer.append((i * multiplicate) + difference)
    
    print(answer)
    print(colored('%in + (%i)' % (multiplicate, difference), 'yellow'))

elif fibonachi(first , secend , third) == True:
    for i in range(1 , 10):
        if not a in answer:
            answer.append(a)
        elif not b in answer:
            answer.append(b)
        else:
            answer.append(a + b)

            a , b = b , a + b
    
    print(answer)
    print(colored('fibonachi', 'yellow'))

elif tavan(first, secend , third):
    for i in range(1 , 10):
        answer.append((i ** multiplicate) + difference)

    print(answer)
    print(colored('n power %i + (%i)' % (multiplicate , difference), 'yellow'))

elif mosalas(first , secend, third) == True:
    a = 2
    b = 1
    for i in range(0, 11):
        answer.append(b)
        b += a
        a += 1

    print(answer,  '\n tranger patter')

else:
    print(colored('False', 'red'))

asd = input(colored('Please enter any key to Continue...' , 'blue'))