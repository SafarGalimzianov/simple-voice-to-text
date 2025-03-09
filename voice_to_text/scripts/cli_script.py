import argparse
from cli import CLITranscriber

DESCRIPTION = 'Transcribe audio files using ElevenLabs API.'
HELP = 'Your ElevenLabs API key.'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Transcribe MP3 files using ElevenLabs API.')
    parser.add_argument('api_key', type=str, help='Your ElevenLabs API key.')
    parser.add_argument('file_path', type=str, help='Path to the MP3 file.')
    args = parser.parse_args()
    transcription = CLITranscriber.process_data(args.file_path)
    print('Transcription:')
    print(transcription)
