
from pixellib.instance import instance_segmentation
import cv2


# OpenCv captures video stream
capture = cv2.VideoCapture(0)

# Create instance of instance segmentation class

segment_video = instance_segmentation()

# Load RCNN model

segment_video.load_model("mask_rcnn_coco.h5")

segment_video.process_camera(capture,show_bboxes = True, frames_per_second= 15, output_video_name="output_video.mp4", show_frames= True,
frame_name= "frame")



# Extract feature overlays and bbox classifications to be used in evaluation algorithm


