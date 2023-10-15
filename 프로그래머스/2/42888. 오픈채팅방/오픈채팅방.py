from collections import defaultdict
def solution(record):
    cmdList = []
    changeL = []
    idName = defaultdict(int)
    for cmd in record:
        cmd = cmd.split()
        if cmd[0] != 'Change':
            cmdList.append(cmd)
            if cmd[0] == 'Enter':
                idName[cmd[1]] = cmd[2]
        else:
            changeL.append(cmd)
            idName[cmd[1]] = cmd[2]
            
    result = []
    for cmd in cmdList:
        if cmd[0] == 'Enter':
            result.append(f'{idName[cmd[1]]}님이 들어왔습니다.')
        elif cmd[0] == 'Leave':
            result.append(f'{idName[cmd[1]]}님이 나갔습니다.')
    return result
            
