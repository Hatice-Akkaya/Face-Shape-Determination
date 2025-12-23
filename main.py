import cv2
import mediapipe as mp
import math
import matplotlib.pyplot as plt

# MediaPipe Kurulumu
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

class FaceAnalyzer:
    def __init__(self):
        self.face_mesh = mp_face_mesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def calculate_distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def get_landmarks(self, image):
        height, width, _ = image.shape
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(image_rgb)
        
        landmarks = []
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                for lm in face_landmarks.landmark:
                    x = int(lm.x * width)
                    y = int(lm.y * height)
                    landmarks.append((x, y))
            return landmarks, results.multi_face_landmarks
        return None, None

    def analyze_face_shape(self, landmarks):
        if not landmarks:
            return "No Face Found", {}

        # Kritik Noktalar
        chin_bottom = landmarks[152]
        forehead_top = landmarks[10]
        cheek_left = landmarks[234]
        cheek_right = landmarks[454]
        jaw_left = landmarks[58]
        jaw_right = landmarks[288]
        temple_left = landmarks[103]
        temple_right = landmarks[332]

        # Mesafeler
        face_length = self.calculate_distance(forehead_top, chin_bottom)
        cheek_width = self.calculate_distance(cheek_left, cheek_right)
        jaw_width = self.calculate_distance(jaw_left, jaw_right)
        forehead_width = self.calculate_distance(temple_left, temple_right)

        # Oranlar
        ratio_len_cheek = face_length / cheek_width
        
        shape = "Unknown"
        
        if ratio_len_cheek > 1.45:
            if forehead_width > cheek_width and jaw_width > cheek_width:
                 shape = "Oblong"
            else:
                 shape = "Oval"
        elif ratio_len_cheek < 1.25:
            if abs(cheek_width - face_length) < face_length * 0.1:
                shape = "Round"
            else:
                shape = "Square"
        else:
            if jaw_width < forehead_width and jaw_width < cheek_width:
                shape = "Heart"
            elif jaw_width > cheek_width:
                shape = "Triangle"
            else:
                shape = "Diamond"

        return shape, {
            "Uzunluk": face_length,
            "Elmacik": cheek_width,
            "Cene": jaw_width,
            "Alin": forehead_width
        }

def analyze_webcam():
    analyzer = FaceAnalyzer()
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Kamera açılamadı!")
        return

    print("Çıkmak için 'q' tuşuna basın.")

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Kamera akışı alınamıyor.")
            break

        landmarks, multi_face_landmarks = analyzer.get_landmarks(image)
        
        result_text = "Searching..."
        color = (0, 0, 255)

        if landmarks:
            shape, _ = analyzer.analyze_face_shape(landmarks)
            result_text = f"Shape: {shape}"
            color = (0, 255, 0)

            for face_landmarks in multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())

        cv2.putText(image, result_text, (30, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        cv2.imshow('Yuz Sekli Analizi (Cikis: q)', image)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    analyze_webcam()
