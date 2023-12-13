import pyaudio
import wave  # Import the wave module
import numpy as np
import matplotlib.pyplot as plt  # Add this import statement

# Parameters for audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # Sample rate (samples per second)
CHUNK = 1024  # Size of each audio chunk (number of frames per buffer)
RECORD_SECONDS = 5  # Duration of recording in seconds
WAVE_OUTPUT_FILENAME = "file_output.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()



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
