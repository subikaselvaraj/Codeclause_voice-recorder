import pyaudio
import wave

# Settings for audio recording
FORMAT = pyaudio.paInt16  # 16-bit format
CHANNELS = 1             # Mono channel
RATE = 44100             # Sampling rate
CHUNK = 1024             # Chunk size for reading data
RECORD_SECONDS = 10      # Duration of recording
OUTPUT_FILENAME = "recorded_audio.wav"  # Output file name

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Start audio stream
print("Starting the recording...")
stream = audio.open(format=FORMAT, 
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

frames = []

# Record audio in chunks
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording finished.")

# Stop and close the stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a file
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Recording saved as {OUTPUT_FILENAME}")
