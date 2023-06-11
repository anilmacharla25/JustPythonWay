import deepspeech
import soundfile as sf
import librosa
import numpy as np

# Step 3: Load the DeepSpeech model
model_path = r"C:\Users\prave\Downloads\deepspeech-0.9.3-models.pbmm"
model = deepspeech.Model(model_path)

# Step 4: Load the audio file
audio_path = r"C:\Users\prave\Downloads\en-GB-AbbiNeural.wav"

# Load the audio file using soundfile
audio_data, sample_rate = sf.read(audio_path)

# Resample audio to 16kHz if necessary using librosa
if sample_rate != 16000:
    audio_data = librosa.resample(audio_data.T, sample_rate, 16000).T
    sample_rate = 16000

# Step 5: Perform speech-to-text inference
text = model.stt(audio_data)
print("Transcription:", text)
