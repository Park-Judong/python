#==================== Data type ====================
# numbers
# print(5)
# print(-10)
# print(3.14)
# print(3.14 + 1210)
# print(3.14 - 3.14)

#strings
# print('풍선')

#boolen
# print(5>10)
# print(True)
# print(False)
# print(not False)

# variables
# animal = "고양이" # string
# name = "연탄이" # string
# age = 4 #integer
# is_adult = age >= 3 #boolen
# hobby = "공놀이"


# print("우리집 " + animal + "의 이름은 " + name + "에요")
# #print(name + "는 " + str(age) +"살이며, "+ hobby +"을 아주 좋아해요.")
# print(name, "는 ", str(age), "살이며, ", hobby, "을 아주 좋아해요.") #,: include 1 space automatically
# print(name + "는 어른일까요? " + str(is_adult))

# blocking commands
# ''' ~~ '''

#Quiz
# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")

#operations
# print(5//3) #1 quotient

# print((3>0) and (3<5)) #True
# print((3>0) & (3<5)) #True, AND

# print((3>0) or (3>5)) #True, OR
# print((3>0) | (3>5)) #True, OR

# print(5 > 4 > 3) #True
# print(5 > 7 > 3) #False

# number = 2 + 3*4 #14
# print(number)
# number = number + 2 # 16
# print(number)
# number += 2 # 18
# print(number)
# number *= 2 # 36
# print(number)
# number /= 2 # 18.0
# print(number)
# number -= 2 # 16.0
# print(number)

# number %= 5 #1
# print(int(number))

#
# print(abs(-5)) #5
# print(pow(4,2)) #4^2 = 16
# print(max(5,12)) #12
# print(min(5,12)) #5
# print(round(3.14)) #3 Rounding
# print(round(4.99)) #5 Rounding

#math library
# from math import *
# print(floor(4.99)) #4, rounding down
# print(ceil(4.99)) #5, rounding up
# print(sqrt(16)) #4

#random library
# from random import *
# print(random()) #0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10) #0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10)+1) #1 ~ 10 이하의 임의의 값 생성

# print(int(random() * 45)+1) #1 ~ 45 이하의 임의의 값 생성

# print(randrange(1,46)) #1 ~ 46 미만의 임의의 값 생성

# print(randint(1,45)) #1 ~ 45 이하의 임의의 값 생성
#==================================================================
#Quiz
# from random import *
# offline_date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(offline_date) +" 일로 선정되었습니다.")
#==================================================================
#strings
# sentence = '나는 소년입니다.'
# print(sentence)
# sentence2 = "파이썬은 쉬워요."
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)
#==================================================================
#slicing
# jumin = "990120-1234567"
# # index: 0 1 2 3 4 ...
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0 ~ 1
# print("월 : " + jumin[2:4]) # 2 ~ 3
# print("일 : " + jumin[4:6]) # 4 ~ 5
# print("생년월일 : " + jumin[:6]) # 0 ~ 5
# print("뒤 7자리 : " + jumin[7:]) # 7 ~ 13
# print("뒤 7자리(뒤에서부터) : " + jumin[-7:]) # -7 ~ -1
# #index: 7: -1, 6: -2 ...
#==================================================================
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper()) #check if index 0 is UPPER character
# print(len(python)) 
# print(python.replace("Python", "Java"))

# index = python.index("n") #seeking the position of 'n'
# print(index)
# index = python.index("n", index+1) #seeking the position of the next 'n'
# print(index)
# print(python.find("Java")) #without Java, find outputs -1
# #print(python.index("Java")) #without Jave, index outputs error
# print(python.count("n")) #counting a number of 'n'
#==================================================================
# #방법1
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple은 %c로 시작해요." % "A")
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# #방법2
# print("나는 {}살입니다." .format(20))
# print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))
# #format = {파란, 빨간}

# #방법3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 99))

# #방법4 (from 3.6 version)
# age = 16
# color = '빨간'
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# #escape 
# print("백문이 불여일견 \n 백견이 불여일타")
# print("저는 '박주동'입니다.") #we can use '' in "". easier to make a mistake
# print("저는 \"박주동\"입니다.")

# #//: 문장 내에서
# print("C:\\judong\\Python")

# # \r: 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# # \b: back space: delete 1 character
# print("Redd\bApple")

# # \t: tab
# print("Red\tApple")

# #Quiz
# website = "http://naver.com"
# website_without_http = website.replace("http://", "").replace("https://", "")
# website_main = website_without_http.split(".")[0]
# another code: website_main = website_without_http[:website_without_http.index(".")]
# #split => {'naver', 'com'}
# #website_main = website[7:12]
# website_main_len = len(website_main)

# key_1st = website_main[0:3]
# key_2nd = website_main_len
# key_3rd = website.count('e')
# key_4th = '!'

# print(f"생성된 비밀번호 : {key_1st}{key_2nd}{key_3rd}{key_4th}")

# ============== list ===================
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# #where is 조세호?
# print(subway.index("조세호"))

# #In the next station, 하하 takes the train
# subway.append("하하")
# print(subway)

# #At the same time, 정형돈 took the section which is between "유재석" and "조세호"
# subway.insert(1, "정형돈")
# print(subway)

#Let's pop All
# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# #a number of name of "유재석"
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

#=================== change the order =======================
# #we can arrange this
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# #reverse the order of the list
# num_list.reverse()
# print(num_list)

# ## erase all
# #num_list.clear()
# #print(num_list)

# #we can mix it with various data types
# mix_list = ["조세호", 20, True]
# #print(mix_list)

# # extend lists
# num_list.extend(mix_list)
# print(num_list)

#================= dictionary =======================
# # key & value
# cabinet = {3:"유재석", 100: "김태호"}
# print(cabinet[3])
# print(cabinet.get(3))
# print(cabinet[100])
# # print(cabinet[5]) #error STOP without key 5
# # print(cabinet.get(5)) #error None without key 5
# print(cabinet.get(5, "사용 가능")) #error 사용 가능 without key 5

# print(3 in cabinet) #True
# print(5 in cabinet) #False 

# cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# #새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# #간 손님
# del cabinet["A-3"]
# print(cabinet)

# #key들만 출력
# print(cabinet.keys())

# #value들만 출력
# print(cabinet.values())

# #key, value 쌍으로 출력
# print(cabinet.items())

# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)

#======================== tuple ==========================
# cannot change order, add contents
# faster than list.

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# # name = "김종구"
# # age = 20
# # hobby = "코딩"
# # print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

#========================= set ============================
#no order, no code element redundancy
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# #교집합
# print(java & python)
# print(java.intersection(python))

# #합집합
# print(java.union(python))
# print(java | python)

# #차집합 (java 할 수 있지만, python할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))
# print(python.difference(java))

# #python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# #java를 잊었어요
# java.remove("김태호")
# print(java)

#==================== switch data structures
#커피숍
# menu = {"커피", "우유", "주스"} # set type
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

#Quiz 4
# from random import *
# #set 20 IDs
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# # lst = range(1,21) #from 1 to 20 numbers
# #print(type(users)): range
# #pick 1 for chicken
# chicken_one = sample(lst,1)
# #remove them picked already
# lst_without_chicken = set(lst) - set(chicken_one)
# #pick 3 for coffee
# coffee_three = sample(list(lst_without_chicken),3)        #lst[1:4]
# # OR we can pick 4 once. And seperate them into 1 and 3.
# print("-- 당첨자 발표 --")
# print(f"치킨 당첨자 : {chicken_one}")
# print(f"커피 당첨자 : {coffee_three}")
# print("-- 축하합니다 --")
# #===================== what we can use above ========================
# #shuffle(lst)    #change index randomly
# #print(sample(lst,1)) #pick #number elements in the list randomly

# # if
# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else: 
#     print("준비물 필요 없어요")

# temp = int(input("오늘 기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요.")

# for
# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4")

# for waiting_no in range(1, 6): #1~6 # [0,1,2,3,4]:
#     print("대기번호: {0}".format(waiting_no))

# startbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in startbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

#while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

#infinite loop
# # ctrl + c => you can exit it
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

#continue, break
# absent = [2,5] #결석
# no_book = [7] #without a book
# for student in range(1,11): # 1 ~ 10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

#one line for loop
#출석번호 1,2,3,4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students] # type: list.
# print(students)
# print(type(students))

# #convert length from names
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# #convert upppers from lowers
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

#Quiz 5
# from random import * 
# count = 0
# for guest in range(1,51): # 1 ~ 50 
#     journy_time = randint(5,50) # randrange(5, 51)
#     if 5 <= journy_time <= 15:
#         print("[O] {0}번째 손님 (소요시간: {1}분)".format(guest, journy_time))
#         count += 1
#     else : 
#         print("[ ] {0}번째 손님 (소요시간: {1}분)".format(guest, journy_time))  
#     guest += 1
#     if guest == 51:
#         print("총 탑승 승객 : {0} 분".format(count))
#===============================================================================================
# function, return, 
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if money > balance: 
#         print("잔액이 부족합니다.")
#         return balance
#     else:
#         print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
#         return balance - money

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission #type: tuple

# open_account()

# balance = 0
# balance = deposit(balance, 2000)
# print(balance)
# balance = withdraw(balance,1000)
# commission, balance = withdraw_night(balance, 400)
# print("수수료 {0} 원이며, 잔액은 {1}원입니다.".format(commission, balance))

#func default
# def profile(name, age=17, main_lang = "파이썬"): #default: age, lang
#     print("이름 : {0}\t나이 : {1}\t 주 사용 언어: {2}".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호")

#같은 학교 같은 학년 같은 반 같은 수업

#func keyword
# def profile(name, age, main_lang): #default: age, lang
#     print("이름 : {0}\t나이 : {1}\t 주 사용 언어: {2}".format(name, age, main_lang))

# profile(name = "유재석", main_lang= "Ruby", age = 90)

# func 
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") #end: instead of new line
#     print(lang1, lang2, lang3, lang4, lang5)
# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end = " ") #end: instead of new line
#     for lang in language:
#         print(lang, end=" ")
#     print() # new line

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
# profile("김태호", 25, "Kotlin", "Swift")

# global & local variable
# gun = 10

# # NOT RECOMMENDED
# def checkpoint(soldiers): #경계근무
#     global gun # I will use the gun out of the func. not recommended
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# RECOMMENDED!!!!!!!!!!!!!!!
# we can deal with the global gun as a parameter of this func. better for managing your code
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun 

# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun,2) # 2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))

# height = float(input("키가 몇입니까?(m) : "))
# gender = input("성별이 무엇입니까?(ex. 남성, 여성) : ")

# def std_weight(height, gender):
#     if gender == '남성':
#         std_kg = height * height * 22
#     elif gender == '여성':
#         std_kg = height * height * 21
#     return std_kg

# std_kg = std_weight(height, gender)

# print(f"키 {str(int(100*height))}cm {gender}의 표준 치중은 {std_kg:.2f}kg 입니다.")

#standard input/output
# print("Python", "Java", "JavaScript", sep=",", end="?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): #key: subject, value: score
#     print(subject.ljust(8), str(score).rjust(4), sep=':')

#은행 대기순번표
#001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3))

# answer = input("아무값이나 입력하세요: ")
# print(type(answer))

# various output format
# # 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))
# # 양수일땐 +로 표시, 음수일땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500))
# # 3자리마다 콤마를 찍어주기
# print("{0:,}".format(100000000000000))
# # 3자리마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(100000000000000))
# print("{0:+,}".format(-100000000000000))
# # 3자리마다 콤마를 찍어주기, +- 부호도 붙이기, 자리수 확보하기
# print("{0:^<+30,}".format(100000000000000))
# # 소수점 출력 2번째자리까지
# print("{0:.2f}".format(5/3))

#file input/output
# score_file = open("score.txt", "w", encoding="utf8") #utf8: 한글정보
# print("수학: 0", file=score_file)
# print("영어: 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "w", encoding="utf8") #utf8: 한글정보
# score_file.write("과학 : 80")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") #utf8: 한글정보
# #print(score_file.read()) #read all lines at once
# #print(score_file.readline()) #read line by line
# #print(score_file.readline()) #read line by line
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") #utf8: 한글정보
# lines = score_file.readlines() #list 형태로 저장
# for line in lines:
#     print(line,end="")
# score_file.close()

#pickle
# import pickle
# profile_file = open("profile.pickle", "wb") #write
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()

# import pickle

# profile_file = open("profile.pickle", "rb") #read
# profile = pickle.load(profile_file) #file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

#with
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

# for i in range(1,3): #1~2
#     with open(f"{i}주차.txt", "w", encoding="utf8") as report_file:
#         dep = input("부서명: ")
#         name = input("이름: ")
#         work = input("업무 요약: ")
#         report_file.write(f"부서 : {dep}\n")
#         report_file.write(f"이름 : {name}\n")
#         report_file.write(f"업무 요약 : {work}\n")
