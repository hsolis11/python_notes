def solution(s):
    right = 0
    salutes_total = 0
    right_inside = False


    for i in s:
        if i == '<' and not(right_inside):
            pass

        if i == '<' and right_inside:
            salutes_total += right * 2
        
        if i == '>':
            right_inside = True
            right += 1
    
    return salutes_total