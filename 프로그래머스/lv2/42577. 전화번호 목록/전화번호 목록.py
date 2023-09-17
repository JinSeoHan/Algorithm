def solution(phone_book):
    setPhone_book = set()
    for i in phone_book:
        setPhone_book.add(i)
        
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in setPhone_book: return False
    return True