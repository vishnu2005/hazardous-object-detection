# from ultralytics import YOLO
# import cv2
# from PIL import Image
# from deep_translator import GoogleTranslator
# from gtts import gTTS
# import os
# import time
# from playsound import playsound
#
# # Paths
# model_path = "best.pt"
# image_path = "test_images/img2.jpg"
# audio_output_dir = "outputs/audio_clips"
# os.makedirs(audio_output_dir, exist_ok=True)
#
# # Load YOLO model
# model = YOLO(model_path)
#
# # Read image
# frame = cv2.imread(image_path)
# captions = []
#
# if frame is not None:
#     results = model(frame)
#     for r in results:
#         for box in r.boxes:
#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#             conf = float(box.conf[0])
#             cls = int(box.cls[0])
#             class_name = model.names[cls].capitalize()
#
#             if conf > 0.4:
#                 area = (x2 - x1) * (y2 - y1)
#                 if area > 100000:
#                     distance = "very close"
#                 elif area > 50000:
#                     distance = "close"
#                 elif area > 20000:
#                     distance = "medium distance"
#                 else:
#                     distance = "far"
#
#                 center_x = (x1 + x2) // 2
#                 width = frame.shape[1]
#                 if center_x < width * 0.33:
#                     position = "left"
#                 elif center_x < width * 0.66:
#                     position = "center"
#                 else:
#                     position = "right"
#
#                 sentence = f"{class_name} detected on the {position}, and it is {distance}."
#                 captions.append(sentence)
#
# else:
#     print("❌ Image not loaded. Check path.")
#
# # Print English Captions
# print("\n[English Captions]:\n")
# for c in captions:
#     print(c)
#
# # Define Indian languages
# languages = {
#     "Hindi": "hi",
#     "Tamil": "ta",
#     "Assamese": "as",
#     "Bengali": "bn",
#     "Telugu": "te",
#     "Malayalam": "ml"
# }
#
# print("\n[Translated Captions + TTS]:\n")
#
# # Translate + TTS
# for lang_name, lang_code in languages.items():
#     print(f"\n[{lang_name}]")
#     for idx, caption in enumerate(captions):
#         translated = GoogleTranslator(source='auto', target=lang_code).translate(caption)
#         print(translated)
#         try:
#             tts = gTTS(text=translated, lang=lang_code)
#             audio_path = os.path.join(audio_output_dir, f"{lang_name}_{idx}.mp3")
#             tts.save(audio_path)
#             playsound(audio_path)
#             time.sleep(1)  # Give time for audio to play
#         except Exception as e:
#             print(f"[ERROR] TTS failed for {lang_name}: {e}")
from ultralytics import YOLO
import cv2
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os
import time

# === PATH SETUP ===
model_path = "best.pt"
image_path = "test_images/img2.jpg"
audio_output_dir = "outputs/audio_clips"
os.makedirs(audio_output_dir, exist_ok=True)

# === LOAD YOLO MODEL ===
model = YOLO(model_path)
frame = cv2.imread(image_path)

captions = []

# === DETECTION & CAPTION GENERATION ===
if frame is not None:
    results = model(frame)
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            class_name = model.names[cls].capitalize()

            if conf > 0.4:
                area = (x2 - x1) * (y2 - y1)
                if area > 100000:
                    distance = "very close"
                elif area > 50000:
                    distance = "close"
                elif area > 20000:
                    distance = "medium distance"
                else:
                    distance = "far"

                center_x = (x1 + x2) // 2
                width = frame.shape[1]
                if center_x < width * 0.33:
                    position = "left"
                elif center_x < width * 0.66:
                    position = "center"
                else:
                    position = "right"

                sentence = f"{class_name} detected on the {position}, and it is {distance}."
                captions.append(sentence)
else:
    print("❌ Image not loaded. Check path.")

# === ENGLISH OUTPUT ===
print("\n[English Captions]:\n")
for idx, cap in enumerate(captions):
    print(cap)
    try:
        tts_en = gTTS(text=cap, lang='en')
        audio_en_path = os.path.join(audio_output_dir, f"english_{idx}.mp3")
        tts_en.save(audio_en_path)
        playsound(audio_en_path)
        time.sleep(1)
    except Exception as e:
        print(f"[ERROR] English TTS failed: {e}")

# === TRANSLATED OUTPUTS ===
languages = {
    "Hindi": "hi",
    "Tamil": "ta",
    "Assamese": "as",
    "Bengali": "bn",
    "Telugu": "te",
    "Malayalam": "ml"
}

print("\n[Translated Captions + TTS]:\n")

for lang_name, lang_code in languages.items():
    print(f"\n[{lang_name}]")
    for idx, caption in enumerate(captions):
        try:
            translated = GoogleTranslator(source='auto', target=lang_code).translate(caption)
            print(translated)
            tts = gTTS(text=translated, lang=lang_code)
            audio_path = os.path.join(audio_output_dir, f"{lang_name}_{idx}.mp3")
            tts.save(audio_path)
            playsound(audio_path)
            time.sleep(1)
        except Exception as e:
            print(f"[ERROR] TTS failed for {lang_name}: {e}")
