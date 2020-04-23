from django.shortcuts import render
from rest_framework import viewsets

from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST
import pydub
from rest_framework.decorators import api_view, permission_classes, authentication_classes
import os 
# import librosa    
import soundfile as sf
import time
import wave

@api_view(['POST'])
# @api_view(['GET'])

@permission_classes((AllowAny,))


def api_convert(request):
    def change_file(file):
        method='bbalnk'
        # mp3=glob.glob('*.mp3')
        dest='dest'+'.wav'
        print('here ')
        mp3_file=file
        sound=pydub.AudioSegment.from_mp3(mp3_file)
        sound=sound.set_frame_rate(8000)
        sound.export(dest, format="wav")
        time.sleep(5)
        # os.system(f"""ffmpeg -i {file} -acodec pcm_u8 -ar 22050 {file[:-4]}.wav""")          # wave.open('fff.wav')
        # data, samplerate = sf.read('fff.wav') 
        # print(samplerate)
        # audio = wave.open('fff.wav', 'wb')
        # audio.setnchannels(1)
        try:
            wavefile =open('fff.wav', 'wb')
        
        except:
            print('error')
        return wavefile
   
    #  return HttpResponse("<h1>MyClub Event Calendar</h1>")
    try:
      
        post_quary=request.POST
        # print(request.data)
        print(post_quary)
        file=request.FILES['myfile']
        file =change_file(file)

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)
        return HttpResponse({'error tt   '+'method' +message: 'Please provide correct file'},
                         status=HTTP_400_BAD_REQUEST)
    # return HttpResponse("<h1>MyClub Event Calendar"+method+"</h1>")
    # file = open("/path/to/your/song.mp3", "rb").read() 

    try:    
        wav='fff'+'.wav'
        print('here ')
     
        # mp3_file=file
        # print('line before sound ')
        # sound=pydub.AudioSegment.from_mp3(mp3_file)
        # sound.export(wav, format="wav")
        # print('after sound')
        # response = HttpResponse(wav, content_type='audio/wav')
        file=change_file(file)
        response = HttpResponse(file, content_type='audio/wav')
        response['Content-Disposition'] = 'attachment; filename="foo.xls"'
        print('finishes ')
    except IOError:
        # handle file not exist case here
        response = HttpResponse('<h1>File not exist</h1>')

    return response


# Create your views here.
