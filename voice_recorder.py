import pyaudio
import wave

# Set parameters for recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open audio stream for recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

# Print a message to indicate that recording has started
print("Recording...")

# Create empty list to store frames of recorded audio
frames = []

# Record audio in chunks
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

# Print a message to indicate that recording has finished
print("Done recording.")

# Stop recording and close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save recorded audio to a WAV file
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

# Print a message to indicate that the file has been saved
print("Audio saved to", WAVE_OUTPUT_FILENAME)
