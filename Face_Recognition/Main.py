import timeit
import cv2

# 가중치 데이터
cascade_filename = 'sample.xml'
# 모델 불러오기
cascade = cv2.CascadeClassifier(cascade_filename)

# 영상, 사진파일 불러오기
cam = cv2.VideoCapture('sample.mp4')
img = cv2.imread('sample.jpg')

# 영상 재생
def videoDetector(cam, img):
    while True:
        start_t = timeit.default_timer()

        ret, img = cam.read()
        img = cv2.resize(img, dsize=None, fx=0.75, fy=0.75)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 얼굴 탐지 알고리즘 (입력 이미지, 이미지 피라미드 스케일 factor, 인접 객체 최소 거리 픽셀, 탐지 객체 최소 크기
        result = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))

        for box in result:
            x, y, w, h = box
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 255, 255), thickness=2)

        # 알고리즘 연산
        terminate_t = timeit.default_timer()
        FPS = 'fps' + str(int(1./(terminate_t - start_t)))
        cv2.putText(img, FPS, (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

        cv2.imshow('facenet', img)

        if cv2.waitKey(1) > 0:
            break

# 사진 출력
def imgDetector(img, cascade):
    img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5, minSize=(20, 20))

    for box in result:
        x, y, w, h = box
        cv2.retangle(img, (x, y), (x + w, y + h), (255, 255, 255), thickness=2)

    cv2.imshow('facenet', img)
    cv2.waitKey(10000)

# 영상탐지
videoDetector(cam, cascade)

# 사진탐지
# imgDetector(cam, cascade)