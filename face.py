import cv2

imagePath = "666.jpg"
cascPath = "C:\python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
	gray,
	scaleFactor = 1.05,
	minNeighbors = 2,
	minSize = (2, 2)
)
print("Found {0} faces!".format(len(faces)))
# draw a rectzngle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)#myproject
