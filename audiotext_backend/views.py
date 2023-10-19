from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import speech_recognition as sr
from pydub import AudioSegment
from serializer import AudioSerializer

@api_view(['POST'])
def conversionView(request):
    file = request.FILES.get('audio')
    # print("start")
    AudioSegment.converter = "C:\\PATH_Programs\\ffmpeg.exe"
    # Convert mp3 file to wav

    # print("start2")
    sound = AudioSegment.from_mp3("Recordingmp3.mp3")
    sound.export("transcript.wav", format="wav")
    # print("start3")
    # Transcribe audio file
    AUDIO_FILE = "transcript.wav"

    # Use the audio file as the audio source
    r = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # Read the entire audio file

    # Transcribe the audio
    transcription = r.recognize_google(audio)

    # Print the transcription
    print("Transcription: " + transcription)

    # Save the transcription to a text file
    with open("transcript.txt", "w") as text_file:
        text_file.write(transcription)
    
    serializer = AudioSerializer()
    Response()
    