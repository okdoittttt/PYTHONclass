# 파일 한 줄씩 읽기 연습

# 파일 열기
readFile = open("ar.txt", "r")          # 읽기모드 열기
writeFile = open("ar_copy.txt", "w")    # 쓰기모드 열기

# 파일 읽기
for aline in readFile:
    aline = aline.lower()
    for c in aline:
        if c.isalnum() or c.isspace():
            writeFile.write(c)


print("출력 완료.")

s = "messiah hwv 561n 1 is an englishlanguage oratorio composed in 1741 by george frideric handel with a scriptural text compiled by charles jennens from the king james bible and from the coverdale psalter the version of the psalms included with the book of common prayer it was first performed in dublin on 13 april 1742 and received its london premiere nearly a year later after an initially modest public reception the oratorio gained in popularity eventually becoming one of the bestknown and most frequently performed choral works in western music"

w = s.split(" ")
print(w)

words = {}

def findAdd(d, w, s):
    if d in s:
        w[d] += 1
    else:
        w[d] = 1


# 단어 출력하기
for key in words:
    print("%20s: %d"%(key, words[key]))

# list로 만들기
wl = list(words.keys())
# 정렬하기
wl.sort()

# 파일 닫기
readFile.close()
writeFile.close()