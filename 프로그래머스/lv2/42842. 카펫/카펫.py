def solution(brown, yellow):
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0:
            width = yellow // i
            height = i
            if (width+2)*(height+2)-(width)*(height) == brown:
                return list([width+2, height+2])