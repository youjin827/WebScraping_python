#정규식(정해진 형식을 의미하는 식.)
# ex. 주민번호

import re


p = re.compile("ca.e") 
# . : 하나의 문자를 의미 > care,cafe,case .. | caffe (x)
# (^de) : 문자열의 시작 > desk, destiny, .. | fade(x)
#$ (se$) : 문자열의 끝 > case,base (0) | face (x)



def print_match(m):
    if m:
        print("m.group():",m.group())  # 일치하는 문자열 반환
        print("m.string()",m.string)   # 입력받은 문자열 
        print("m.start():",m.start())  # 일치하는 문자열의 시작 index
        print("m.end():",m.end())      # 일치하는 문자열의 끝 index
        print("m.span():",m.span())    # 일치하는 문자열의 시작/끝
    else :
        print("매칭되지 않음.")

''' case 1
m = p.match("careless")  # match : 주어진 문자열의 처음부터 일치하는지 확인.
print_match(m)        
'''


lst= p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 변환.
print(lst)



'''
정규식 쓸 때 
1. re.compile("원하는 형태")
2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
3. m = p.search("비교할 문자열") :            중에 일치하는게 있는지 확인
4. lst = p.findall("비교할 문자열"): 일치하는 모든 것을 "리스트" 형태로 변환

원하는 형태 : 정규식
# . : 하나의 문자를 의미 > care,cafe,case .. | caffe (x)
# (^de) : 문자열의 시작 > desk, destiny, .. | fade(x)
#$ (se$) : 문자열의 끝 > case,base (0) | face (x)
'''
