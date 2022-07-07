from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.
import joblib

reloadModel = joblib.load('./models/Lineal Regression.pkl')

def index(request):
    context = {'a': 'HelloWorld!'}
    return render(request, 'index.html', context)
    #return HttpResponse({'a':1})

def predict(request):
    print(request)
    if request.method == 'POST':
        temp= []
        temp.append(float(request.POST.get('temp9Val')))
        temp.append(float(request.POST.get('presion3Val')))
        temp.append(float(request.POST.get('humedad3Val')))
        temp.append(float(request.POST.get('presion9Val')))
    print(temp)
    scoreval = reloadModel.predict([temp])
    #testDta = pd.DataFrame({'x':temp}).transpose()
    #scoreval = reloadModel.predict(testDta)[0]
    context={'scoreval':round(scoreval[0],1)}
    return render(request, 'index.html',context)