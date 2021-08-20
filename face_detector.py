# import libraries
import cv2 as cv
import face_recognition

# def face_det():
# Get a reference to webcam
video_capture = cv.VideoCapture(0)
if not video_capture.isOpened():
    print("Cannot open camera")
    exit()

# Initialize variables
face_locations = []

while True:

    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)

    # Display the results
    for top, right, bottom, left in face_locations:
        cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

    # Display the resulting image
    cv.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv.destroyAllWindows()

# if __name__ == '__main__':
#     face_det()
