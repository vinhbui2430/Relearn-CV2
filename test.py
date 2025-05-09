import numpy as np
import cv2 as cv

events = [i for i in dir(cv) if 'EVENT' in i]
print(events)

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
 
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
 
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
 
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                return
                # cv.rectangle(img,(ix,iy),(x,y),(0,255,0),0)
            else:
                cv.circle(img,(x,y),5,(0,0,255),-1)
 
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),2)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)

img = cv.imread('longcat.jpg')
clone = img.copy()

cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
 
while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    if k == ord('r'):
        img = clone.copy()
    if k == ord('s'):
        cv.imwrite('annotatedimg.jpg', img)
    elif k == 27:
        break
 
cv.destroyAllWindows()