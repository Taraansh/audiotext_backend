from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import speech_recognition as sr
from pydub import AudioSegment
from .serializer import AudioSerializer, ProfileSerializer
from .models import Audio, Profile


@api_view(['POST'])
def conversionView(request):
    file = request.FILES.get('audio')
    # print("start")
    AudioSegment.converter = "C:\\PATH_Programs\\ffmpeg.exe"
    # Convert mp3 file to wav

    # print("start2")
    sound = AudioSegment.from_mp3(file)
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
    converted_file = Audio.objects.create(text_file)
    serializer = AudioSerializer(converted_file)
    Response(serializer.data)


@api_view(['POST'])
def signup(request):
    profile = Profile.objects.create(
        email=request.data['newEmail'],
        password=request.data['newPassword'],)
    profile.save()
    serializer = ProfileSerializer(profile)
    return Response({'success': True, 'data': serializer.data})


@api_view(["POST"])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    profile = Profile.objects.get(email=email, password=password)
    if profile:
        return Response({"status": "success", "email": email})
    else:
        return Response({"status": "failed"})
