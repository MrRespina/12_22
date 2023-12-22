class Calculator:
    def __init__(self,f,s):   # 멤버 필드를 초기화하기 위한 생성자격 메소드 __init__ (_2개씩)
        self.f = f
        self.s = s
    def addNum(self):
        self.res = self.f + self.s
        return self.res
    def subNum(self):
        self.res = self.f - self.s
        return self.res
    def mulNum(self):
        self.res = self.f * self.s
        return self.res
    def divNum(self):
        self.res = self.f / self.s
        return self.res

class FourCal(Calculator):    # 파이썬의 상속. 
    def subNum(self):
        self.res = self.f - self.s
        return self.res
    def mulNum(self):
        self.res = self.f * self.s
        return self.res
    def divNum(self):   # 오버 라이드 : 재 정의
        if self.s == 0 or self.f == 0:
            self.res = 0
        else:
            self.res = self.f / self.s
        return self.res

fCalc2 = FourCal(10,0)

def gugu(startDan,endDan,startGop,endGop):
    for dan in range(startDan,endDan + 1):
        for gop in range(startGop,endGop + 1):
            print(f'{dan} * {gop} = {dan*gop}')

def randint(x1,x2): 
    return x1 + x2

i = 10
PI = 3.141492
