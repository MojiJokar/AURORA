import time
import cv2
import numpy as np

from gz.transport13 import Node
from gz.msgs10.image_pb2 import Image

TOPIC = "/world/iris_runway/model/iris_with_gimbal/link/pitch_link/sensor/camera/image"

node = Node()
latest_frame = None
frame_count = 0


def camera_callback(msg):
    global latest_frame, frame_count

    image = np.frombuffer(msg.data, dtype=np.uint8)

    image = image.reshape(
        msg.height,
        msg.width,
        3
    )

    latest_frame = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2BGR
    )

    frame_count += 1


if not node.subscribe(Image, TOPIC, camera_callback):
    raise RuntimeError("Could not subscribe to Gazebo camera")


print("AURORA LIVE CAMERA STARTED")
print("Waiting for Gazebo images...")
print("Press Q to exit.")

try:
    while True:

        if latest_frame is not None:

            cv2.imshow(
                "AURORA - Live Gazebo Camera",
                latest_frame
            )

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        time.sleep(0.01)

finally:
    cv2.destroyAllWindows()
    print("Camera stopped.")
