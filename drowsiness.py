import cv2
eye_cascPath = 'path_to_haarcascade/haarcascade_eye_tree_eyeglasses.xml' #default cascades provided by opencv
face_cascPath = 'path_to_haarcascade/haarcascade_frontalface_alt.xml' #default cascades provided by opencv
faceCascade = cv2.CascadeClassifier(face_cascPath)
eyeCascade = cv2.CascadeClassifier(eye_cascPath)

cap = cv2.VideoCapture(0)

duration_ptr = 0
lentt = []
zero_var = 0
one_var = 0


while 1:
    duration_ptr = duration_ptr + 1
    ret, img = cap.read()
    if ret:
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
      
            eyes = eyeCascade.detectMultiScale(
                frame,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
            )
            if len(eyes) == 0:
                print("can't see eyes")
                lentt.append(-1)
            else:
                for (x, y, w, h) in eyes:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                print('eyes')
                lentt.append(1)


            cv2.imshow('Face Recognition', frame)

        if duration_ptr == 100:

            duration_ptr = 0

            zero_var = 0
            one_var = 0

            for i in lentt:
                if i == -1:
                    zero_var = zero_var + 1

                elif i == 1:
                    one_var = one_var + 1


            if zero_var > one_var:
                print("person is sleeping!")
                exit(0)

            elif one_var > zero_var:
                print("person is awake")

        waitkey = cv2.waitKey(1)
        if waitkey == ord('q') or waitkey == ord('Q'):
            cv2.destroyAllWindows()
            break