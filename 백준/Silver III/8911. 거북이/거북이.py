import sys
input = sys.stdin.readline

dir = [(0,1),(1,0),(0,-1),(-1,0)] # 북->동->남->서

def turtle(cmds):
    cx, cy, cd = 0, 0, 0

    lx,rx,uy,dy = 0,0,0,0

    for cmd in cmds:
        if cmd == 'F':
            cx, cy = cx+dir[cd][0], cy+dir[cd][1]
        elif cmd == 'B':
            cx, cy = cx-dir[cd][0], cy-dir[cd][1]
        elif cmd == 'L':
            cd = (4+cd-1)%4
        elif cmd == 'R':
            cd = (4+cd+1)%4
        rx = max(rx, cx)
        lx = min(lx, cx)
        uy = max(uy, cy)
        dy = min(dy, cy)
    return (rx-lx) * (uy-dy)

for i in range(int(input())):
    q = input()
    print(turtle(q))