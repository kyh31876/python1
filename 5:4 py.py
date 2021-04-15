#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:28:39 2021

@author: tetsuyaariake
"""

#성인 판별 

age = int(input("나이 입력 :"))
if age >= 19:
    print("성인")

print("미성년자입니다")


# if else # 참이면 if 다음에 있는 문장을 수행하고 거짓이면 else 다음 문장을 수행

#수를 입력 받아 홀수 짝수 판별하기
number = int(input("숫자를 입력하세요:"))
if number % 2 == 0:
    print("짝수")
else:
    print("홀수")
    
    
    
#가격 할인 행사에 다른 상품 구입 가격 구하기
#상품 구입 가격이 10 만원 이상이면 20%, 그렇지 않으면 10% 를 할인함
price = float(input("상품 가격을 입력 (만원):"))
if price >= 10: 
    discount = price * 0.2
else:
    discount = price * 0.1
final_price = price - discount
print(" 최종 가격 : %.2f 만원 " %final_price)


## 근무시간에 따른 시간당 임금 구하기
## 단 근무시간이 7 시간을 넘을 경우 넘은 시간에 대해서는 시간당 임금의 50% 를 추가로 지급함
            
hours = float(input("근무 시간 입력 :"))
pay = 8000
if hours > 7:
    salary = pay * hours
    salary = salary + (pay * (hours)) * 0.5
else:
    salary = pay * hours
print("임금 : %.2f 원 " %salary)


#여자 축구단을 모집하는 프로그램
#단 나이는 10~12 살 사이의 여성이어야 함 , 성별은 m 과 f 로 받아들임
gender = input(("성별을 입력 남 :m, 여 :f) :"))
if gender == 'f':
    age = int(input("나이 입력 :"))
    if 10 <= age <= 12:
        print("입단이 가능합니다")
    else:
        print("나이가 조건에 안맞습니다")
else: 
    print("여자만 모집합니다.")
    
    
# 점수를 입력 받아 학점을 출력하는 프로그램
score = int(input("점수를 입력 :"))
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:      
    print("B")
elif 70 <= score < 80:
    print("C")
else:
    print("F")
if score >= 90:
    print("수")
elif score >= 80:
    print("우")
elif score >= 70:
    print("미")
elif score >= 60:
    print("양")
else:
    print("가")


#달의 일수를 구하기
month = int(input("달을 입력 :"))
if month == 2: 
    print("28일")
elif month == 4 or month == 6 or month == 10: 
    print("30일")
else: 
    print("31일")
    
#학생 10 명의 점수로 합격 불합격자수 구하기
passes = 0; failure = 0
count = 1
while count <= 10:
    score = int(input("학생 점수를 입력 :"))
    if score >= 80:
        passes += 1
    else:
        failure += 1
    count += 1
print("합격 : %d, 불합격 : %d" %(passes,failure))


#두 수의 중간 값 구하기
minNumber = int(input("작은 수 입력 :"))
maxNumber= int(input( "큰 수 입력 :"))  
while True: 
    if minNumber >= maxNumber:
        break 
    minNumber+= 1
    maxNumber -= 1

print("중간값 :", minNumber)


#while 문에서 else 문 사용이 가능함
#모든 반복을 다 수행하였을 경우 else 문을 수행
# 반복을 다 수행하지 못하고 빠져나올 경우 else 문은 수행하지 않음
count = 1
while count <= 5:
    if count == 3:
        break
    print("python", count)
    count += 1
else:
    print("감사합니다")

count = 1
while count <= 5:
    print("python", count)
    count += 1
else:print("감사합니다")



#in 다음의 리스트 순차 자료 개수 만큼 반복하여 “python” 문자열 출력
for number in [1, 2, 3, 4, 5]:
    print("python")
    
    
#리스트의 개수만큼 차례로 반복하면서 score 변수에 하나씩 저장
for score in [100, 98, 85, 70]:
    print(score)
#in 다음의 문자열 길이 만큼 반복하면서 각 문자를 letter 변수에 저장
for letter in "hello":
    print(letter)

#in 다음의 리스트의 문자열 수만큼 반복하여 문자열을 변수에 저장
for animal in ["dog", "cat", "pig", "lion"]: 
    print("동물 :",animal)


#5 개 성적의 합과 평균 구하기
    
total = 0
for score in [100, 98, 85, 97, 74]:
    total += score
    average = total / 5
    
print("합 : %d" %total)
print("평균 : %.2f" %average)


#for 문에 else 문 사용할 수 경우
#모든 반복을 다 수행했을 경우 else 문을 수행
#반복 수행 중 중간에 중지되는 경우 else 문을 수행하지 않음

# 중첩된 반복문을 이용한 구구단 작성
dan = 2
while dan <= 9:
    su = 1
    while su <= 9:
        print("%d X %d = %d" %(dan, su, dan*su)) # %d 는 정수형 들고옴 
        su += 1
    dan += 1

for dan in range(2, 10): #마지막 숫자 포함안됨, 숫자가 포함된경우
    for su in range(1, 10):
        print("%d X %d = %d" %(dan, su, dan*su))

# 주사위 두 개를 던졌을 때 합이 6이 되는 경우 출력하기
for dice1 in range(1, 7):
    for dice2 in range(1, 7):
        if (dice1 + dice2) == 6:
            print("주사위1 : %d, 주사위2 : %d" %(dice1, dice2))
for dice1 in range(1,7):
    for dice2 in range(1,7): 
        if (dice1 + dice2) == 6:
            print("dice1 : %d, dice2 :%d" %(dice1,dice2))

# 라인과 별의 수를 입력하여 별 블록 생성하기
line = int(input("라인 개수 : "))
star = int(input("별의 개수 : "))
for lcount in range(line):
    for scount in range(star):
        print("*", end="")
    print()

for line in range(1, 6):
    for star in range(line):
        print("*", end="")
    print()

for line in range(1, 5):
    for star in range(line, 5):
        print("*", end="")
    print()


     
#continue   
for letter in "python":
    if letter == "t":
        continue
    print(letter, end="")
else:
    print("출력완료")
    
for letter in "python":
    if letter == "t":
        print(letter, end="")
else:
    print("출력완료")
    
    
#1에서 20까지의 수중에서 2의 배수와 3의 배수를 제외한 수 구하기
for number in range(1, 21):
    if number % 2 == 0 or number % 3 == 0:
        continue
print(number, end="")


#숫자 건너뛰기
for count in range (1,6):
     if count == 3:
         continue
     print("count=", count)

# '\'연산은 현재라인과 다음라인을연결 , '*'연산은 문자 반복을 의미 
# in keyword 데이터 내부에 element 의 존재를 확인 
massage= "hello world"
print("h" in massage)

# str(object) number object 를 str로 변환 
#문자형 formatting  
# %d 정수형 , $f 실수형, %s  문자형, %.nf  소수 n자리까지 실수출력 

#입력된 문자열 거꾸로 
<<<<<<< HEAD
s = input("Enter a string: ")
print(s[::-1])
=======
a= input("문자를 입력하시오:")
print(a[::-1])


>>>>>>> 2f71aaf2ba9bdd442b08d7eca0952470fbd8507b

#입력한 주민번호 에서 생년월일 추출하여 출력 
import sys 
idnumber= input("주민번호를 '-'없이 입력:")
if '1' == idnumber[6] or idnumber[6]=='2':
    year = '19' + idnumber[:2]
else:
    year= '20' +idnumber[2:4]

month=idnumber[2:4]
day=idnumber[4:6]
print("%d년 %d월 %d일 " %(year,month,day))

def stdInfo(rrn):
    while len(rrn) !=7:
        print('7자리가 아닙니다. 다시 입력해주세요.')
        rrn = input('주민등록번호 7자리를 입력하세요 : ')
        if len(rrn) == 7:
            break

    #앞 2자리 이용하여 나이 계산
    if int(rrn[:2]) < 21 and int(rrn[6]) in (3, 4) :
        biryear = 2000 + int(rrn[:2])
    else:
        biryear = 1900 + int(rrn[:2])
    #월
    birmonth = int(rrn[2:4])
    #일
    birday = int(rrn[4:6])

#문자열.count(찾을 문자열 위치, 찾을 위치)
#문자열.replace(찾을 문자열,바꿀문자열 )  

#문자열.split() *important 
#문자열.splitless()  

#구분문자.join 인수에서 지정한 문자열이나 리스트의 각항목들에 구분문자를 중간에 삽입 하여 하나의 문자열을 만들어 변환 

a= [1,2,[3,4]]
a[[2][0]]


#range 
list(range(0,3))

#서로다른 리스트 요소를 반복문으로 출력
person = ["홍길동" , 25 , "박지성" , 35 , "박찬호" ,32]
for count in range(len(person)):
    if count % 2 ==0:
        print("이름 : %s" %person[count], end=",")
    else: 
        print("나이: %d" %int(person[count]))
        
#0부터 15까지 피보나치 수열 만들기 
fibo = list(range(10))
fibo[0]=1
fibo[1]=1
for count in range(2,10):
    fibo[count] = fibo[count-2] + fibo[count-1]
    
    
print("피보나치 :", fibo)

#리스트의 분리 
number1, *number2 = [10,20,30,40,50]


#max(): 리스트 내의 가장 큰요소를찾아 변환  min(): 리스트내의 가장작은요소를 변환 

#index method  변수명.함수명(옵션) ; 변수명.index(찾을위치)
#count method 변수명.count()

# list.append(data): 리스트마지막요소로 새로운요소 추가 
# list.insert(index, data) : 리스트에 삽입할 위치를 지정해 새로운 요소를 추가

# list.extend( 확장할 리스트 )마지막에 다른 리스트의 요소를 추가하여 확장. 

#학생 5명의 점수를 입력받아 리스트에 저장하고 평균구하기 시험문제(문자를 숫자로)

student =[]
total =0 
for count in range(5):
    score =int(input("점수를 입력 :"))
    student.append(score)
    total += score
    
average = total/ len(student)
print("학생들 점수:", student)
print("평균 : %.1f" %average)


#삭제 pop삭제할자료를 보여준후 삭제 
# remove 값삭제 del 변수삭제

#변수명.pop() 마지막자료를 보여준뒤 삭제 
#변수명.remove(삭제자료) 

a=[1,2,3]
a.remove(2)

#정렬 sort() sorted() reverse 
a= [1,3,2]
sorted(a)

print(a.sort(a)) #정렬해서 저장까지 할떄 


#5명의 이름 차례로 입력 하고 list 보여주기 삭제할 이름을 입력한후 삭제 

names =[] 
name_str = input("다섯명 이름 입력 :") 
name_str.split(',')
rmv=input("삭제할 이름입력 :")
if rmv in names:
        names.remove(rmv)
        print(names)  
    while TURE: 
        rmv=input("삭제:") #리스트에 없는 이름
        if rmv == 'exit':
            break
        elif rmv in names:  
            name.remove(rmv)
            print(rmv)#삭제할 이름 입력요구 
            break
        else:
            print("다시입력:") #다시입력 

#국가를 입력받아 리스트로 구성하기 (시험문제,알파벳순서변환 )
nation =[]

while TRUE:
    name=input("국가를 입력 (종료:exit):")
    if name == "exit":
        break
    if name in nation:
        print("중복된 국가가 존재합니다")
        print("다시입력 하세요 ")
        continue
    nation.append(name)
print("국가 :", nation)
        
