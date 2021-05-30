ballCoor=[];
# cv2.VideoCapture take a file path and return the video
# cv2.VideoCapture("path");
inputVideo=cv2.VideoCapture("videos/video.mp4");# 0 for webcam
outputVideo=cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'),10,(1920,1080));
# video.isOpened() return True if the video has any frames.
while video.isOpened():
  # video.read() read the video by frame and return a tuble with the frame as
  # an image and a True or False value, True if there is a frame.
  isFrame, frame = inputVideo.read();
  if isFrame is False:
    break;
  hsvBallFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV);
  # The ball is yellow colored
  lowerYellow=np.array([21,0,0]);
  upperYellow=np.array([45,255,255]);
  frameMask=cv2.inRange(hsvBallFrame,lowerYellow,upperYellow);
  contourLine,h=cv2.findContours(frameMask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE);
  centerContourPoint=None;
  if len(contourLine)>0:
    area=max(contourLine,key=cv2.contourArea);
    # cv2.minEnclosingCircle() take the focused area and return x,y coordinates
    # and it's radius.
    ((x,y),radius)=cv2.minEnclosingCircle(area);
    M=cv2.moments(area);
    try:
      centerContourPoint=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]));
      cv2.circle(frame,centerContourPoint,10,(255.255,255),-1);
      ballCoor.append(centerContourPoint);
    except:
      pass;
    if len(ballCoor)>2:
      for i in range(1,len(ballCoor)):
        cv2.line(frame,ballCoor[i-1],ballCoor[i],(0,0,255),3);
  outputVideo.write(frame);
outputVideo.release();