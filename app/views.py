from django.shortcuts import render

def home(request):

    return render(request, 'home.html')

def prediction(request):

    return render(request, 'prediction.html')

def prediction_result(request):

    return render(request, 'prediction.html')