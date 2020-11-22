a = int(input("숫자를 입력하시오."))
b = int(input("숫자를 입력하시오."))

if a % 2 == 0 and b % 2 == 0:
    print("모두 짝수입니다.")
elif a % 2 == 0 or b % 2 == 0:  # "else if" 를 파이썬에서는 "elif" 라고 씀
    print("둘 중 하나는 짝수입니다.")
else:
    print("모두 홀수입니다.")