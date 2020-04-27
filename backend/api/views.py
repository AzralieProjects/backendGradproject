from django.shortcuts import render
from rest_framework import viewsets

from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST
import pydub
from rest_framework.decorators import api_view, permission_classes, authentication_classes
import os 
from .models import My_Test
from .serializers import My_TestSerializer
# import librosa    
import soundfile as sf
import time
import wave
import os, tempfile, zipfile
from django.http import HttpResponse
# from django.core.servers.basehttp import FileWrapper

from wsgiref.util import FileWrapper

def send_file(request):
    """                                                                         
    Send a file through Django without loading the whole file into              
    memory at once. The FileWrapper will turn the file object into an           
    iterator for chunks of 8KB.                                                 
    """
    fname='./mediafiles/des.wav'
    filename = fname # Select your file here.                                
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(filename)
    return response
class My_TestViewSet(viewsets.ModelViewSet):

    pass
@api_view(['POST'])

@permission_classes((AllowAny,))
    # queryset = Movie.objects.all()
# def render(self, name, value, attrs=None, renderer=None):
#     pass

def api_convert(request):
    # queryset = My_Test.objects.all()
    # My_Test=
    # serializer_class = My_TestSerializer('555','musahassuna')

    def change_file(file,name):
        method='bbalnk'
        # mp3=glob.glob('*.mp3')
        dest='./mediafiles/'+name+'.wav'
        print('here ')
        mp3_file=file
        
        sound=pydub.AudioSegment.from_mp3(mp3_file)
        sound=sound.set_frame_rate(8000)
        sound.export(dest, format="wav")
        print('after export')
        # time.sleep(5)
        # os.system(f"""ffmpeg -i {file} -acodec pcm_u8 -ar 22050 {file[:-4]}.wav""")          # wave.open('fff.wav')
        # data, samplerate = sf.read('fff.wav') 
        # print(samplerate)
        # audio = wave.open('fff.wav', 'wb')
        # audio.setnchannels(1)
        # try:
        #     wavefile =open('fff.wav', 'wb')
        
        # except:
        #     print('error')
        return 'wavefile'
    def sendfile(name):
        base='./mediafiles/'
        fname=base+name+'.wav'
        print(fname)
        f = open(fname,"rb") 
        response = HttpResponse()
        response.write(f.read())
        response['Content-Type'] ='audio/mp3'
        response['Content-Length'] =os.path.getsize(fname )
        return response

   
    #  returnfname HttpResponse("<h1>MyClub Event Calendar</h1>")
    try:
      
        post_quary=request.POST
        # print(request.data)
        print(post_quary)
        file=request.FILES['myfile']
        name=request.data['filename']
        print(name)
        path =change_file(file,name)
        print('finish')
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)
        return HttpResponse({'error tt   '+'method' +message: 'Please provide correct file'},
                         status=HTTP_400_BAD_REQUEST)
    

    try:
        name=request.data['filename']

        # sendfile(name)
    
        # response = HttpResponse(wav, content_type='audio/wav')
        # temp=change_file(file)
        # fname='./mediafiles/dest.wav'
        base='./mediafiles/'
        fname=base+name+'.wav'
        print(fname)
        f = open(fname,"rb") 
        response = HttpResponse()
        response.write(f.read())
        response['Content-Type'] ='audio/mp3'
        response['Content-Length'] =os.path.getsize(fname )
        return response
        # f = open(fname,"rb")     fname='./mediafiles/des.wav'
        # filename = fname # Select your file here.                                
        # wrapper = FileWrapper(file(filename), "rb")
        # response = HttpResponse(wrapper, content_type='text/plain')
        # response['Content-Length'] = os.path.getsize(filename)
        # return response
        print('uplading file')

        '''response = HttpResponse(file, content_type='audio/wav')
        
        
        response.write(f.read())
        response['Content-Disposition'] = 'attachment; filename="foo.xls"'''
        print('finishes ')
    except IOError:
        # handle file not exist case here
        response = HttpResponse('<h1>File not exist</h1>')

    return response


# Create your views here.
