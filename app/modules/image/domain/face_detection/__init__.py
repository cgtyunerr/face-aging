"""Face detection package."""
from .face_detection import FaceDetection
from .mtcnn_face_detection import MtcnnFaceDetection

__all__ = ["FaceDetection", "MtcnnFaceDetection"]