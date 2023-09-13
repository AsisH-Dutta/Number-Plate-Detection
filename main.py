from easyocr import Reader
import cv2
import matplotlib.pyplot as plt
import pytesseract as pt
import Info_api



haarcascade = "model/haarcascade_russian_plate_number.xml"
cap=cv2.VideoCapture(0)
cap.set(3,640) # width 
cap.set(4,480) # height


min_area=500
count =0


while (count<1):
    success,img = cap.read()

    plate_cascade =cv2.CascadeClassifier(haarcascade)
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(img_gray,1.1,4)

    for(x,y,w,h) in plates:
        area = w*h

        if area > min_area:
            cv2.rectangle(img, (x,y),(x+w, y+h), (0,255,0), 2)
            cv2.putText(img, 'Number Plate', (x, y-3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
            
            img_plate = img[y:y+h, x:x+w]
            cv2.imshow("Number Plate", img_plate)
            

    cv2.imshow("Number Plate Detected", img)
    
    # save the image
    if cv2.waitKey(1) & 0xFF == ord('s'):
    #    file = cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_plate)
       file = cv2.imwrite("scaned_img_" + str(count) + ".jpg", img_plate)
       cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
       cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
       # print("image saved")
       cv2.imshow("plate Detected",img)
       count += 1
       Info_api.dbs()
       # cv2.waitKey(500)
       
       
    
        







