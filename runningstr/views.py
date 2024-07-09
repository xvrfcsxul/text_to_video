from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .models import Video
from .utils import create_video

def video_view(request):
    if request.method == 'POST':
        text = request.POST.get('input_text')
        create_video(text)
        video = open('video.mp4', 'rb')
        video_model = Video(text=text)
        video_model.save()
        return FileResponse(video, content_type='video/mp4', as_attachment=True)
    return render(request, 'home.html')
