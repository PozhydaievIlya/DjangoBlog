# from django.core.files.storage import FileSystemStorage
# from django.shortcuts import render, redirect
#
# from .forms import PhotoForm
# from .models import Photo
#
#
# # Create your views here.
#
# def gallery(request):
#     photos = Photo.objects.all()
#     context = {"photos": photos}
#     return render(request, "gallery/gallery.html", context)
#
#
# def upload(request):
#     if request.method == "POST":
#         photoForm = PhotoForm(request.POST, request.FILES)
#         if photoForm.is_valid():
#             photoForm.save()
#             return redirect('/gallery/')
#
#     photoForm = PhotoForm()
#     context = {"photoForm": photoForm}
#     return render(request, "gallery/upload.html", context)
