# 파일을 한줄씩 읽어 출력하기 연습
# 2022.4.27
import os

# ===========================================================
# 사전 d에 처리할 단어 w를 전달하여 신규 등록 하거나 단어 횟수를 증가 시킨다
def findAdd(d, w):  # (단어 찾아서 개수 +1 해주는 함수)
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

# ===========================================================
def wordsCount():
    # 1.파일 열기
    sourceFile = input("작업할 원본파일명:")
    midFile = "중간파일"+sourceFile
    reportFile = "report_"+sourceFile

    finput = open(sourceFile, "r")
    foutput = open(midFile, "w")
    # 2.한 줄씩 읽어서 처리하기.

    for aline in finput:
        aline = aline.lower()  # 한 줄 읽은 내용을 모두 소문자로 변환.
        # aline의 문자들을 조사하여 알파벳만 화면에 출력한다.
        for ch in aline:
            if ch.isalnum() or ch.isspace() or ch == "-":  # 알파벳이거나 숫자이면 출력
                foutput.write(ch)

    # 파일 닫기
    finput.close()
    foutput.close()

    # ==========================================================
    dictionary = dict()  # 빈 dictionary 생성
    finput = open(midFile, "r")

    for aline in finput:
        words = aline.split(" ")  # 읽은 한 줄을 단어 단위로 분리한 리스트 생성

        for w in words:  # 리스트에서 단어 하나씩 가져오기
            w = w.strip()
            if len(w) > 0:
                findAdd(dictionary, w)  # 단어 사전에 차례로 신규 등록 또는 카운트 업

    # ==========================================================
    # dictionary d를 알파벳 순으로 정렬한다.
    # 1. d의 key만 뽑아서 list를 만든다.
    k = list(dictionary.keys())

    # 2. key list를 정렬한다.
    k.sort()
    # 3. 정렬된 key list에서 key를 차례로 꺼내어 새 dictionary에 추가한다.
    #   (이 때 value는 d에서 읽어 온다.)
    abc = dict()
    for item in k:
        abc[item] = dictionary[item]

    # 결과를 새 파일에 출력
    output = open(reportFile, "w")
    output.write("입력파일:{}\n".format(sourceFile))

    for key in abc:  # 사전 dictionary내용을 파일에 출력한다.
        output.write("%20s: %d\n" % (key, dictionary[key]))

    output.close()  # 파일 닫기
    # midFile은 삭제하도록 한다.
    os.remove(midFile)
    print("통계작업 완료.[결과파일 : %s]"%(reportFile))

    # 1)등장한 단어들을 알파벳 순으로 표시한다.
    # dictionary =>sortedDictionary로 새로 생성하기.
