import os
import cv2

output_directory = "media/trimming"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

video_capture = cv2.VideoCapture('media/video31.mp4')

x = 410
y = 60
width = 500
height = 400
output_file_path = os.path.join(output_directory, "video_face.mp4")

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter(output_file_path, fourcc, 30.0, (width, height))

while True:
    ret, frame = video_capture.read()

    if not ret:
        break

    cropped_frame = frame[y:y + height, x:x + width]

    out.write(cropped_frame)

    cv2.imshow('Cropped Video', cropped_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
out.release()
cv2.destroyAllWindows()
