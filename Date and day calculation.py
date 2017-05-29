days = ["일", "월", "화", "수", "목", "금", "토"]
monthsList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
maxOfMonths = 13
yearOfLeapMonths = 29


def isLeap(x):
    return (not (x % 4)) and (x % 100) or (not (x % 400))


def getOldToCur(x):
    return ((x - 1) * 365) + (x - 1) // 4 - (x - 1) // 100 + (x - 1) // 400


#함수 크기를 쪼갤 필요가 있음 -> 날짜 연산 , x일 뒤 계산 부분
#y,m,d를 클래스로 처리하면 더 깔끔

def totalDay(year, months, date, x):
    # 1년 1월 1일부터 지금까지 흐른 시간 년도 계산
    total = getOldToCur(year)
    if isLeap(year):
        monthsList[1] = yearOfLeapMonths
    # 달수 계산
    for i in range(months - 1):
        total += monthsList[i]
    # 날짜 추가
    total += date

    print(year, months, date, days[int(total % 7)])
    while 1 <= x:
        # 말일이라면 1일로 바꾸고 다음달로 넘겨줌
        if monthsList[months - 1] == date:
            date = 1
            months += 1
        else:
            date += 1
        x -= 1
        total += 1
        # 말월이라면 1월로 바꾸고 내년으로 넘겨줌
        if months == maxOfMonths:
            months = 1
            year += 1
            # 만약 바뀐 연도가 윤년이라면 2월 날짜를 조정해줌
            if isLeap(year):
                monthsList[1] = yearOfLeapMonths
            else:
                monthsList[1] = 28

    print(year, months, date, days[int(total % 7)])

'''
years = (input('년도를 입력해주세요:'))
months = (input('월를 입력해주세요:'))
dates = (input('일를 입력해주세요:'))
print(totalDay(int(years), int(months), int(dates), int(x)))
'''
x = (input('x일 후 입력해주세요:'))
print(totalDay(2005,5,1,int(x)))