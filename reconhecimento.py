import cv2

classifier = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")

video = cv2.VideoCapture(0)

video.set(cv2.CAP_PROP_FRAME_WIDTH,640)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

while not cv2.waitKey(20) & 0xFF == ord('q'):
    ret, color = video.read()

    gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)

    faces = classifier.detectMultiScale(gray)

    for x, y, w, h in faces:
        cv2.rectangle(color, (x,y), (x+w, y+h),(0,255,0),2)

    cv2.imshow('color',color)
    cv2.imshow('gray',gray)