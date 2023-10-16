import re
def solution(files):
    reHead = re.compile('^[^0-9]+')
    reNumber = re.compile('\d+')
    l = []
    for f in files:
        m = reHead.match(f)
        n = reNumber.findall(f)
        l.append([f, m.group(), int(n[0])])
    l.sort(key=lambda x : (x[1].lower(), x[2]))
    result = []
    for v in l:
        result.append(v[0])
        
    return result