import cv2


img=cv2.imread("C:\\Users\\berza\\OneDrive\\Documenten\\cv\\drawing on images\\pikachu.jpg")
font=cv2.FONT_HERSHEY_SIMPLEX

org=(50,50)
FontScale=1
color= (255,0,0)

thickness= 2

image=cv2.putText(img,'OpenCV',org, font, FontScale, color,thickness,cv2.LINE_AA)

cv2.imshow("normal",img)
cv2.waitKey(0)
cv2.destroyAllWindows()