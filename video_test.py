import cv2

capt = cv2.VideoCapture(0)

while(True):
    ret, frame = capt.read()
    
    gr = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gr)
    
    if cv2.waitKey(1) & 0xFF == ord('p'):
        break 

capt.release()
cv2.destroyAllWindows()