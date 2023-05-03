# def solution(phoneBook):
#     # 1. 전화번호 sorting
#     phoneBook.sort()

#     # 2. 인접한 전화번호 두 개씩 비교
#     for i in range(len(phoneBook) - 1):
#         if phoneBook[i+1].startswith(phoneBook[i]):
#             return False
#     return True
#startswith는 문자열이 특정문자로 시작하는지 여부를 알려줌 (true, false 반환)

def solution(phoneBook):
    phoneBook.sort()

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


# zip 함수는 여러 개의 iterable자료형의 크기가 동일할 때 사용한다. 
# ( 크기가 다를경우 순서대로 생성후 None값 삽입) -for문과 사용을 많이 한다

# iterable 자료형의 각각의 요소를 나눈 후 순서대로 묶어서 요소 개수만큼 새로운 iterable 자료형을 생성


phone_book = [123,415]
for nums in phone_book: 
    nums = 1
print(phone_book)