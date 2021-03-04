import cv2

image_path_ramm = "resources/static/img/facecontrol/ramm.jpg"
image_path_roxette = "resources/static/img/facecontrol/roxette.jpg"
image_path_cam = 'resources/static/img/facecontrol/webcam.png'
face_cascade = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier('venv/Lib/site-packages/cv2/data/haarcascade_eye.xml')


def view_image(img, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def print_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    faces_detected = "Faces detected: " + format(len(faces))
    print(faces_detected)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=1.046, minNeighbors=5, minSize=(25, 25))
        i = 0
        for (ex, ey, ew, eh) in eyes:
            if i < 2:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                i = i + 1

        view_image(img, faces_detected)


'''
cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
for i in range(10):
    cap.read()
ret, frame = cap.read()
frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imwrite(image_path_cam, frame)
cap.release()
'''
# Here instead of image_path_ramm and others we would use image_path_cam but Kaspersky still blocks camera
print_faces(cv2.imread(image_path_ramm))
print_faces(cv2.imread(image_path_roxette))
