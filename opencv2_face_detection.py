faceCascade=cv2.CascadeClassifier("files/haarcascade_frontalface_default.xml");
#personImage=cv2.imread("images/person.jpg");
personImage=cv2.imread("images/group.jpg");

grayScalePersonImg=cv2.cvtColor(personImage,cv2.COLOR_BGR2GRAY);
faces=faceCascade.detectMultiScale(grayScalePersonImg,1.3,5);
for (x,y,w,h) in faces:
  cv2.rectangle(personImage,(x-25,y-25),(x+w+25,y+h+25),(0,255,0),3);
cv2_imshow(personImage);
