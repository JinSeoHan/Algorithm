l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for e in l:
    for j in range(s.count(e)):#해당 문자 요소 개수만큼 삭제
        s = s[:s.find(e)] + '_' +s[s.find(e) + len(e):]        
print(len(s))