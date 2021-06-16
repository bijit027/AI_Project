import cv2

# Image file
img_file = 'cars-in-middle-of-street-road.jpg'
video = cv2.VideoCapture('video.mp4')

#Pre-trained car classifier
classifier_file = 'car_detector.xml'

#Create car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)



#Run untill car stops
while True:

    #read the current frame and
    (read_successful, frame) = video.read()

    if read_successful:
       #Must convert to grayscale
       grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else: 
       break

    #detect cars
    cars = car_tracker.detectMultiScale(grayscaled_frame)

    #Draw rectangles around the cars
    for(x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255),2)

    




    #Display  the image with the faces spotted
    cv2.imshow('Car Detector',frame)

    #Dont autoclose (Wait here in the code and listen for a key press)
    cv2.waitKey(1)



"""

#create opencv image
img = cv2.imread(img_file)



#convert to grayscale (nedded for haar cascade) conevert color to black and white
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



#Create car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

#detect cars
cars = car_tracker.detectMultiScale(black_n_white)
print(cars)


#Draw rectangles around the cars
for(x,y,w,h) in cars:


 cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)

#cv2.putText(abc, 'Car', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
#Display  the image with the faces spotted
cv2.imshow('Car Detector',img)

#Dont autoclose (Wait here in the code and listen for a key press)
cv2.waitKey()






"""

print("Code completed")