import soundfile as sf
import clipaudiomodule as ca
import bingspeechmodule as bs
import bingttsmodule as bt
import luismodule as luis
import requests


class BotHelper():

    def convert_audio(self):
        myfile = sf.SoundFile('/home/trungbd1/input.wav', mode='r', format='RAW',
                              samplerate=16000, channels=1, subtype='PCM_16')
        sf.write('converted.wav', myfile.read(),
                 16000, subtype='PCM_16', format='WAV')

    def trim_audio(self):
        trimmer = ca.AudioTrimmer()
        # Saves trimmed audio to trimmed.wav
        trimmer.trim_audio('converted.wav')

    def recognize_speech(self):
        spr = bs.BingSpeech('YOUR_BING_SPEECH_KEY')
        # Take from trimmed data
        res = spr.transcribe('trimmed.wav')
        print res
        return res

    def get_response(self):
        # # speech to text
        # translator = bt.Translator('YOUR_BING_SPEECH_KEY')
        # text = self.recognize_speech()
        # # get bot response
        # reply = luis.get_luis_response(text)
        # print reply
        # # text to speech
        # output = translator.speak(
        #     reply, "en-US", "Female", "riff-16khz-16bit-mono-pcm")
        data = self.ss()
        with open("botresponse.wav", "w") as f:
            f.write(data)

    def ss(self):
        url_request = "http://10.208.209.81:5040/api/v1/tts/results/wav/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDA5MTkxNDMsImlhdCI6MTYwMDkxNTU0MywiaXNzIjoic3MiLCJjdG4iOiIxM2I4YTBlYTliZTNlMTQzMDQ5ZTAxNTFmZGI5NGVkZGQ4Mzc3M2ZlMzkyZDEwMjhjNjdiODBmMTllMTdhZTQ0IiwibW9kIjoibWFsZV9ub3J0aCIsImN0eCI6ImdlbmVyYWwifQ.XohK66baKHbbPKceBxAhELrGcBl7YcZoXUNyhInCltQ"
        response = requests.get(url_request)
        data = response.content
        return data

    def generate_response(self):
        self.convert_audio()
        # self.trim_audio()
        self.get_response()
