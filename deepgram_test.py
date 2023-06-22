# Example filename: deepgram_test.py

from deepgram import Deepgram
import asyncio
import json
import copy
#from config import *

# Location of the file you want to transcribe. Should include filename and extension.
# Example of a local file: ../../Audio/life-moves-pretty-fast.wav
# Example of a remote file: https://static.deepgram.com/examples/interview_speech-analytics.wav
FILE = 'audio/ec.m4a'

# Mimetype for the file you want to transcribe
# Include this line only if transcribing a local file
# Example: audio/wav
MIMETYPE = 'audio/mp4'

FIRST_API_KEY = '426ede75de63902dcec1758f2825fdecf4144b73'
SECOND_API_KEY = 'c76cd20140827b65299eace0dc4fb9ffa17dcce1'
async def main():

    # Initialize the Deepgram SDK
    deepgram = Deepgram(FIRST_API_KEY)
    deepgram2 = Deepgram(SECOND_API_KEY)
    # Check whether requested file is local or remote, and prepare source
    if FILE.startswith('http'):
        # file is remote
        # Set the source
        source = {
            'url': FILE
        }

    else:
        # file is local
        # Open the audio file
        audio = open(FILE, 'rb')

        # Set the source
        source = {
            'buffer': audio,
            'mimetype': MIMETYPE
        }

    # Send the audio to Deepgram and get the response
    response = await asyncio.create_task(
        deepgram.transcription.prerecorded(
            source,
            {
                'punctuate': True,
                'model': 'base',
                'language': 'zh'
            }
        )
    )

    # Write the response to the console
    print(json.dumps(response, indent=4))
    
    audio = open(FILE, 'rb')
    source = {
            'buffer': audio,
            'mimetype': MIMETYPE
    }
    response2 = await asyncio.create_task(
        deepgram.transcription.prerecorded(
            source,
            {
                'punctuate': True,
                'model': 'base',
                'language': 'en'
            }
        )
    )

    # Write the response to the console
    print(json.dumps(response2, indent=4))
    # Write only the transcript to the console
    # print(response["results"]["channels"][0]["alternatives"][0]["transcript"])

try:
    # If running in a Jupyter notebook, Jupyter is already running an event loop, so run main with this line instead:
    # await main()
    asyncio.run(main())
except Exception as e:
    exception_type, exception_object, exception_traceback = sys.exc_info()
    line_number = exception_traceback.tb_lineno
    print(f'line {line_number}: {exception_type} - {e}')
