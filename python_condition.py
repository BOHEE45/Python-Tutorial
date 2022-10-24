# number = 7
# if number < 5:
#     print("숫자가 5보다 작습니다.")
# elif 5 < number < 10:
#     print("5보다 크고 10보다 작습니다.")
# else:
#     print("10보다 큽니다.")
 
# money = int(input("숫자를 입력하세요"))
# if money == 70000:
#     print("비행기를 타고 가세요")
# elif money == 50000:
#     print("기차를 타고 가세요")
# elif money == 30000:
#     print("버스를 타고 가세요")
# else:
#     print("걸어가세요")
    
# for i in range(10):
#     print("hello world")
    
# countries = ["kor","usa","china"]
# # for country in countries:
# #     print(country)
    
# for country in countries:
#     if country == "kor":
#         print("한글로 분석해주세요.")
#     elif country == "usa":
#         print("영어로 분석해주세요.")
#     elif country == "china":
#         print("중국어로 분석해주세요.") 


# 1부터 5까지 더하는 프로그램을 만드시오.
# result = 0
# for i in range(1,6):
#     result = result + i # result += i 같은코드
#     print(result)
    
# for i in range(10):
#     if 3<=i<=5:
#         continue # 반복문의 코드 처음으로 돌아간다.
#     print(i)
  
for i in range(10):
    if 3<=i<=5:
        break # 반복문을 중단한다.
    print(i)
  