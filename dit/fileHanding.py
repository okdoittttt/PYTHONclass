# 파일 읽기 연습

# 파일 열기
readFile = open("ar.txt", "r")          # 읽기모드 열기
writeFile = open("ar_copy.txt", "w")    # 쓰기모드 열기

# 파일 읽기
writeFile.write(readFile.read())
print("파일 복사 완료.")

# 파일 닫기
readFile.close()
writeFile.close()