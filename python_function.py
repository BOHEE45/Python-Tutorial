# def name(input):
#     print("제 이름은" + input + "입니다.")
# name("보희")

# def sum(a,b):
#     print(a+b)
# sum(3,4)

grade = ""
def check_grade(성적):
    if 성적 >= 90:
        greade = "A"
    elif 성적 >= 80:
        grade = "B"
    return grade
a = check_grade(80)
print(a)
#분석을 할 때는 소문자랑 대문자 서로 인식이 다르기 때문에 전처리 먼저 무조건 해줘야한다.
#Python / python