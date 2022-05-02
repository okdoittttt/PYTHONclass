# 문자열 출력하기 연습 1
# ss = 'Python!'
#
# sslen = len(ss)
#
# for i in range(0, sslen):
#     print(ss[i], end='$')
#

# 문자열 출력하기 연습 2
# a = 'happy python'
#
# print(a.count('p'))
# print(a.find('a'))
# print(a.rfind('h'))
# print(a.find('h', 5))
# print(a.startswith('p'))
# print(a.endswith('n'))

# 문자열 공백 제거하기
# s = ' 파 이 썬 '
#
# # 왼쪽, 오른쪽 한글자 제거
# print(s.strip())
# # 오른쪽 한글자 제거
# print(s.rstrip())
# # 왼쪽 한글자 제거
# print(s.lstrip())
# # 특정 문자 제거
# ss = '--파-이-썬--'
# print(ss.strip('-'))
# rr = '<<파 << 이 >> 썬>>'
# print(rr.strip('<>'))

# 특정 문자 변경하기
# ss = input("문자를 입력하세요.")
#
# for i in range(0, len(ss)):
#     if ss[i] != 'o':
#         print(ss[i], end='')
#     else:
#         print('$', end='')

# 문자열 결합, 분리

a = '파이썬을 열심히 공부 중'
print(a.split())
b = '하나:둘:셋'
print(b.split(':'))
c = '하나\n둘\n셋'
print(c.splitlines())
d = '%'
print(d.join('파이썬'))