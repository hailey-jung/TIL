import calculator as calc
import datetime
print(calc.add(2,5))

#datatime 해부하기

today = datetime.datetime.now()
print(today)
print(today.year)
print(today.strftime("%A, %B %dth %Y"))

name = input("이름을 알려주세요:")
print(name)

#input은 항상 문자열