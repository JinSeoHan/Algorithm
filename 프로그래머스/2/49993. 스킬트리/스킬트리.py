def solution(skill, skill_trees):
    result = 0
    for tree in skill_trees:
        ord = 0
        flag = True
        for i in tree:
            if i in skill:
                if skill.index(i) != ord:
                    flag = False
                    break
                ord += 1
                if ord >= len(skill): break
        if flag:
            result += 1
    return result