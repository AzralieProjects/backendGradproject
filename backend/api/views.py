from django.shortcuts import render
from rest_framework import viewsets

from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST
import pydub
from rest_framework.decorators import api_view, permission_classes, authentication_classes
import os 
# import librosa    



@api_view(['POST'])
# @api_view(['GET'])

@permission_classes((AllowAny,))


def api_convert(request):
    def change_file(file):
        # mp3=glob.glob('*.mp3')
        wav='fff'+'.wav'
        print('here ')
     
        mp3_file=file

        sound=pydub.AudioSegment.from_mp3(mp3_file)
        sound.export(wav, format="wav")
        # y, sr = librosa.load(wav, sr=8000) # Downsample to 8kHz
        # librosa.output.write_wav(wav, y, sr)
    # sound.export(wav,format="wav")
        return     'c'
   
   

    #  return HttpResponse("<h1>MyClub Event Calendar</h1>")
    try:
        method='ll'
      
        post_quary=request.POST
        # print(request.data)
        print(post_quary)
        file=request.FILES['myfile']
        

    except:
        return HttpResponse({'error tt   '+method: 'Please provide correct file'},
                         status=HTTP_400_BAD_REQUEST)
    # return HttpResponse("<h1>MyClub Event Calendar"+method+"</h1>")
    # file = open("/path/to/your/song.mp3", "rb").read() 

    try:    
        wav='fff'+'.wav'
        print('here ')
        file=change_file(file)
        response = HttpResponse(file, content_type='audio/wav')
        response['Content-Disposition'] = 'attachment; filename="foo.xls"'
        print('finishes ')
    except IOError:
        # handle file not exist case here
        response = HttpResponse('<h1>File not exist</h1>')

    return response


# Create your views here.
