import cv2
import numpy as np
from google.colab.patches import cv2_imshow


numberOfShapes=0;
shapesImage=cv2.imread("images/shapes.png");
grayScaleImg=cv2.cvtColor(shapesImage,cv2.COLOR_BGR2GRAY);

# cv2.threshold(image,lowerBound,upperBound,type);
# cv2.threshold() return a tuple of image where all the focused part of image is
# black and background is white.
ret, shapesOnlyImage=cv2.threshold(grayScaleImg,50,255,1);
# cv2.findContours() takes a image and return contour lines in that image.
contourLine,h=cv2.findContours(grayScaleImg,1,2);
# Loop through all the contourLines and find the contour points
# With the help of contour points we can determine which shape is it.
# ie, a triangle has 3 contour points while a rectangle has 4.
for contourPoint in contourLine:
  # epsilon value is the amount of error which can be negated from the calculation.
  epsilon=cv2.arcLength(contourPoint,True);
  # cv2.approxPolyDP() takes contourPoints epsilon Value and isClosedCurve values
  # and return a smaller approximate contour point which just enough to specify
  # what shape was it.
  # cv2.approxPolyDP(contourPoint,epsilonValue,isClosedCurve)
  approxPoints=cv2.approxPolyDP(contourPoint,0.01*epsilon,True);
  points=len(approxPoints);
  numberOfShapes+=1;
  # cv2.drawCountours() takes the image, contourPoints, color, thickness and
  # draw line around that shape.
  # cv2.drawContours(image,[contourPoint],0,(b,g,r),thickness);
  if points==6:
    cv2.drawContours(shapesImage,[contourPoint],0,(255,255,255),4);
  elif points==4:
        cv2.drawContours(shapesImage,[contourPoint],0,(0,0,255),4);
  elif points==3:
        cv2.drawContours(shapesImage,[contourPoint],0,(255,0,255),4);
  elif points>6:
        cv2.drawContours(shapesImage,[contourPoint],0,(0,255,0),4);
  
cv2_imshow(shapesImage);
print("Number Of Shapes: ",numberOfShapes)