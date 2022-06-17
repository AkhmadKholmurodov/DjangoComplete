from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  """
  페이지 Home 화면 출력
  """
  return render(request, 'detection/home.html')

def dataset(request):
  return render(request, 'detection/dataset.html')