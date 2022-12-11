import math
import cv2

src = cv2.imread("C:\Users\82103\Desktop\opencv\melling.png")
dst = src.copy()


gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, 
                           param1=350, param2=40, minRadius=30, maxRadius=102)
canny = cv2.Canny(gray, 5000, 1500, apertureSize=5, L2gradient=True)
lines = cv2.HoughLinesP(canny, 0.8, math.pi / 180, 90, minLineLength=10, maxLineGap=100)

print('Number of detected lines =', len(lines))

for circle in circles[0]:
    x, y, r = int(circle[0]), int(circle[1]), int(circle[2])
    cv2.circle(dst, (x, y), r, (255, 255, 255), 2)
for i in lines:
    cv2.line(dst, (int(i[0][0]), int(i[0][1])), (int(i[0][2]), int(i[0][3])), (0, 0, 255), 2)

cv2.imshow("Detect lines and circles", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()