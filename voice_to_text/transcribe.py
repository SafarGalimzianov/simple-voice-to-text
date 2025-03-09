'''
transcribe() function sends an HTTP POST request to the
ElevenLabs API to transcribe the audio file.
this function is imported by the classes
that are responsible for different types of input, for example:
- CLI input
- GUI input
'''
import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()


def transcribe(source):
    try:
        api_key = getenv('ELEVENLABS_API_KEY')
    except:
        raise Exception('ELEVENLABS_API_KEY not \
                        found in environment variables.')
    url = 'https://api.elevenlabs.io/v1/speech-to-text/convert'
    headers = {
        'xi-api-key': api_key,
    }
    try:
        with open(source, 'rb') as f:
            files = {'file': f}
            response = requests.post(url, headers=headers, files=files)
        if response.status_code == 200:
            data = response.json()
            return data.get('text', 'No transcription found.')
        else:
            return f'Error: {response.status_code}, {response.text}'
    except FileNotFoundError:
        return 'File not found.'
    else:
        # What file type does ElevenLabs require?
        ...
if __name__ == '__main__':
    raise Exception('This function is not meant to be run directly')