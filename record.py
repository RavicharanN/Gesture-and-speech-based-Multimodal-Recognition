import pyaudio
import wave
import audioop
 
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "file"
 
audio = pyaudio.PyAudio()
 
# start Recording

iter = 1

while True:
    ip = raw_input()
    if ip == "e":
        break
    if ip == "r":
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
        print ("recording...")
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            mx = audioop.max(data, 2)
            print (mx)
            frames.append(data)
        print ("finished recording")
        waveFile = wave.open(WAVE_OUTPUT_FILENAME + str(iter) + ".wav", 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        iter += 1

        # stop Recording
        stream.stop_stream()
        stream.close()
        
audio.terminate()
print("Total files generated : " + str(iter-1))
