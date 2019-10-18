from django.shortcuts import render, redirect
from client.forms import RecordForm
from client.models import Record


def login(request):
    return render(request, 'login.html')

def student(request):
    return render(request, "student.html")


# def Rec(request):
#     if request.method == "POST":
#         form = RecordForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect()
#             except:
#                 pass
#     else:
#         form = RecordForm()
#     return render(request, "", {'form': form})

# def home(request):
#     return render(request,'')
