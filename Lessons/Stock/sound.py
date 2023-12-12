import pyaudio
import matplotlib.pyplot as plt
import numpy as np

# Parameters for audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Size of each audio chunk (number of frames per buffer)
RECORD_SECONDS = 5  # Duration of recording in seconds
WAVE_OUTPUT_FILENAME = "output.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open a new audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []

# Record audio in chunks
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

# Close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save recorded audio to a file
with open(WAVE_OUTPUT_FILENAME, "wb") as wf:
    wf.write(b''.join(frames))

# Read the recorded audio file
audio_data = np.fromfile(WAVE_OUTPUT_FILENAME, dtype=np.int16)

# Create a time axis for the waveform
time = np.linspace(0, len(audio_data) / RATE, num=len(audio_data))

# Plot the waveform
plt.figure(figsize=(10, 4))
plt.plot(time, audio_data, lw=0.5)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Waveform")
plt.grid()
plt.show()
