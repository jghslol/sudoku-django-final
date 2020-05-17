from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'sudokuapp/index.html')

def easypuzzle(request):
    return render(request,'sudokuapp/easypuzzle.html')

def hardpuzzle(request):
    return render(request,'sudokuapp/hardpuzzle.html')
