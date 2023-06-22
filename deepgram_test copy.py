# Example filename: deepgram_test.py

import json
import requests
# Location of the file you want to transcribe. Should include filename and extension.
# Example of a local file: ../../Audio/life-moves-pretty-fast.wav
# Example of a remote file: https://static.deepgram.com/examples/interview_speech-analytics.wav
FILE = 'audio/ec.m4a'

# Mimetype for the file you want to transcribe
# Include this line only if transcribing a local file
# Example: audio/wav
MIMETYPE = 'audio/mp4'

zhurl = "https://api.deepgram.com/v1/listen?language=zh-CN&punctuate=true&utterances=true"

enurl = "https://api.deepgram.com/v1/listen?language=en-US&punctuate=true&utterances=true"

with open(FILE, 'rb') as file:
    raw_binary_data = file.read()

payload = raw_binary_data
headers = {
    "accept": "application/json",
    "content-type": MIMETYPE,
    "Authorization": "Token " + DEEPGRAM_API_KEY,

}

zhresponse = requests.post(zhurl, data=payload, headers=headers)

print(json.dumps(zhresponse.json(), indent=4))

enresponse = requests.post(enurl, data=payload, headers=headers)

print(json.dumps(enresponse.json(), indent=4))