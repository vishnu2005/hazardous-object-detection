📁 Folder Structure

hazardous-object-detection/
│
├── best.pt                   # YOLOv8 trained model (custom for hazard detection)
├── detect_and_caption.py     # Main detection + translation + TTS script
├── requirements.txt
│
├── test_images/
│   └── img2.jpg              # Sample input images
│
└── outputs/
    └── audio_clips/          # Saved audio (MP3) clips
⚙️ Installation
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/<your-username>/hazardous-object-detection.git
cd hazardous-object-detection
2. Set up Python environment
bash
Copy
Edit
pip install -r requirements.txt
3. Run Detection
bash
Copy
Edit
python detect_and_caption.py
📦 Dependencies
ultralytics

opencv-python

Pillow

deep-translator

gTTS

playsound

All included in requirements.txt.

📌 Notes
best.pt is the trained YOLOv8 model (~6 MB).

Uses Google Translate + gTTS, so internet connection is required for translation and speech generation.

Assamese TTS is not currently supported by gTTS (will be skipped with a warning).
