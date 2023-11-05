# from deepface import DeepFace
# import cv2
# import matplotlib.pyplot as plt
#
#
# def process_frame(frame):
#     result = DeepFace.verify(frame, img2_path)
#     print(result)
#
#
# img2_path = "media/1.jpg"
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#
#     cv2.imshow("Camera", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# process_frame(frame)
# cap.release()
# cv2.destroyAllWindows()

from deepface import DeepFace
import cv2

#
# def process_frame(frame):
#     result = DeepFace.verify(frame, img2_path, enforce_detection=False)
#     print(result)
#
#
# video_path = "media/trimming/video_id.mp4"
#
# img2_path = "media/1.jpg"
# cap = cv2.VideoCapture(video_path)
#
# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
#
#     process_frame(frame)
#
#     cv2.imshow("Video", frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
