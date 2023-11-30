import math
def solution(w,h):
    
    gcd = math.gcd(w, h)
    
    rateW, rateH = w // gcd, h // gcd
    
    cnt = rateW + rateH - 1
    
    return w* h - w // rateW * cnt