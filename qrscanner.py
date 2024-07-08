import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
cam.set(5, 640)
cam.set(6, 480)

while True:
    # Capture the video frame by frame
    ret, frame = cam.read()
    data, bbox, straight_qrcode = detector.detectAndDecode(frame)
    if len(data) > 0:
        print(data)

        for i in decode(frame):
         print(i.type)
         print(i.data.decode('utf-8'))
         time.sleep(6)

    # Display the resulting frame
    cv2.imshow('frame', frame)
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    for i in decode(frame):
        print(i.type)
        print(i.data.decode('utf-8'))
        time.sleep(6)

cam.release()       

cv2.destroyAllWindows()
 

 
