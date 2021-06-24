def compare(a, b):
    a = a.split(".")
    b = b.split(".")

    decision = False
    swap = False

    counter = 0
    while not(decision):
        
        try:
            if int(a[counter]) > int(b[counter]):
                decision = True
                swap = True
            elif int(a[counter]) == int(b[counter]):
                counter += 1
            else:
                decision = True
        except:
            if len(a) > len(b):
                decision = True
                swap = True
            decision = True
    
    return swap

    
def solution(s):
    sorted = False
    
    if not(sorted):
        swapped = True
        maxElement = len(s)-1

        for i in range(maxElement):
            if swapped:
                swapped = False
                for j in range(maxElement):
                    if compare(s[j], s[j+1]):
                        s[j], s[j+1] = s[j+1], s[j]
                        swapped = True
                        
        sorted = True

    return s

