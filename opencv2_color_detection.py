shapesImage=cv2.imread("images/shapes.png");
hsvShapesImage=cv2.cvtColor(shapesImage,cv2.COLOR_BGR2HSV);

# Defining the bounds of blue color.
# lower bound : 65, upper bound : 110
# background bound : 0,0 to 255,255 (ignore)
lowerBlue=np.array([65,0,0]);
upperBlue=np.array([110,255,255]);

lowerRed=np.array([0,0,0]);
upperRed=np.array([20,255,255]);

lowerGreen=np.array([46,0,0]);
upperGreen=np.array([91,255,255]);

lowerYellow=np.array([21,0,0]);
upperYellow=np.array([45,255,255]);

# cv2.inRange(image,lowerBound,upperBound) return the are where the 
# given range is present
blueColorMask=cv2.inRange(hsvShapesImage,lowerBlue,upperBlue);
redColorMask=cv2.inRange(hsvShapesImage,lowerRed,upperRed);
greenColorMask=cv2.inRange(hsvShapesImage,lowerGreen,upperGreen);
yellowColorMask=cv2.inRange(hsvShapesImage,lowerYellow,upperYellow);


# cv2.bitwise_and(image,image,mask=mask) return a image where only
# the masked area is visible.
blueColorResult=cv2.bitwise_and(shapesImage,shapesImage,mask=blueColorMask);
redColorResult=cv2.bitwise_and(shapesImage,shapesImage,mask=redColorMask);
greenColorResult=cv2.bitwise_and(shapesImage,shapesImage,mask=greenColorMask);
yellowColorResult=cv2.bitwise_and(shapesImage,shapesImage,mask=yellowColorMask);

display=np.hstack((shapesImage,blueColorResult,greenColorResult,redColorResult,yellowColorResult));
cv2_imshow(display);