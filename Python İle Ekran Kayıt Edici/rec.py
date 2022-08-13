import pyautogui
import numpy as np
import cv2


resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename ="output.avi"
fps = 60.0
out = cv2.VideoWriter(filename, codec, fps, resolution)
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    
    img = pyautogui.screenshot()
    frame = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGRA)
    out.write(frame)
    cv2.imshow("Live",frame)
    # q tusu ile kapatabilirsiniz.
    if cv2.waitKey(1) == ord("q"):
        break
out.release()
cv2.destroyAllWindows()