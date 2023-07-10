import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key.json"

from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="We live in a god darn society!")

# Build the voice request, select the language code ("en-US") 
# ****** the NAME
# and the ssml voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code='en-US',
    name='en-US-Neural2-D',
    ssml_gender=texttospeech.SsmlVoiceGender.MALE)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, 
    voice=voice, 
    audio_config=audio_config
)

# The response's audio_content is binary.
with open('neural.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "neural.mp3"')