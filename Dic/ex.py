import cv2
import numpy as np
import face_recognition

# Elon musk 이미지를 test와 원본을 저장.
imgElon = face_recognition.load_image_file("examples/son.jpg")
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file("examples/elon_test.jpg")
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

# 이미지에 얼굴을 찾아 인식 후 사각형 표시
facLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (facLoc[3], facLoc[0]), (facLoc[1], facLoc[2]), (255,0,255),2)

jangun = face_recognition.load_image_file("examples/jangun.JPG")
print(face_recognition.face_locations(jangun))
print(face_recognition.face_locations(imgElon))

facLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (facLocTest[3], facLocTest[0]), (facLocTest[1], facLocTest[2]), (255,0,255),2)

# test이미지와 원본 이미지를 비교 후 결과를 저장.
results = face_recognition.compare_faces([encodeElon], encodeTest)
faceDis = face_recognition.face_distance([encodeElon], encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)

cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Test', imgTest)
cv2.waitKey(0)