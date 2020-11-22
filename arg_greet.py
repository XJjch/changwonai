def arg_greet(*N):
    for X in N:
        print("안녕하세용", X,"님")

arg_greet("엄준식", "이재석", "김찬호", "정상길", "손인욱")
arg_greet("랄로","파카","괴물쥐")

# 가변인자(arg)를 쓰기 위해서는 반드시 "*" 가 들어가야한다~~~