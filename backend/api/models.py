from django.db import models
from django.core.files import File
#added
from django.conf import settings
from audiofield.fields import AudioField
import os.path
#added 
# def _check_permission_clashing(custom, builtin, ctype):
#     pass
class Result(models.Model):
    pass

# class test_file(models.Model):
#     test_id=models.CharField(max_length=32)
#     pass
#     test_file=File
#     test_date=models.DateField()
    # result= result
#dd
# audio_file = AudioField(upload_to='your/upload/dir', blank=True,
#                         ext_whitelist=(".mp3", ".wav", ".ogg"),
#                         help_text=("Allowed type - .mp3, .wav, .ogg"))

# # Add this method to your model
# def audio_file_player(self):
#     """audio player tag for admin"""
#     if self.audio_file:
#         file_url = settings.MEDIA_URL + str(self.audio_file)
#         player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (file_url)
#         return player_string

# audio_file_player.allow_tags = True
# audio_file_player.short_description = ('Audio file player')
class My_Test(models.Model):
    title = models.CharField(max_length=32)
    test_id = models.AutoField(primary_key=True)
    test_owner= models.CharField(max_length=32)
    # file = models.f


# Create your models here.
# Add the audio field to your model
    audio_file = AudioField(upload_to='your/upload/dir', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg"))

# Add this method to your model
    def audio_file_player(self):
        """audio player tag for admin"""
        if self.audio_file:
            file_url = settings.MEDIA_URL + str(self.audio_file)
            player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (file_url)
            return player_string

    audio_file_player.allow_tags = True
    audio_file_player.short_description = ('Audio file player')