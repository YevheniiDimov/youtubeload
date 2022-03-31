from django.shortcuts import render
from pytube import YouTube

def index(request):
    context = {"message": ""}
    if request.method == 'POST':
        link = request.POST.get('link')
        quality = request.POST.get('quality')
        
        yt = YouTube(link)
        
        file = yt.streams.filter(file_extension='mp4').get_by_resolution(quality)
        
        if file == None:
            context['message'] = "Video doesn't support this quality"
            return render(request, 'index.html', context)
        
        context = {"file": file, "message": "There is your video"}
    
    return render(request, 'index.html', context)