from django.shortcuts import render

import requests
import sys
from subprocess import run,PIPE
def button(request):
    return render(request,'home.html')
def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'home.html',{'data':data})

import os

def external(request):
    inp = request.POST.get('param')

    script_path = r'C:\Users\Tanmay Walke\Desktop\Test_Chatbot_Prajwal\Test_Chatbot\Test_Chatbot\buttonpython\test.py'
    

    
    if os.path.exists(script_path):
        try:
            out = run([sys.executable, script_path, inp], shell=False, stdout=PIPE, stderr=PIPE, text=True)
            print(out.stdout)
            return render(request, 'home.html', {'data1': out.stdout})
        except Exception as e:
            print(f"Error executing the script: {e}")
            return render(request, 'home.html', {'data1': f"Error executing the script: {e}"})
    else:
        print(f"Error: File not found at {script_path}")
        return render(request, 'home.html', {'data1': f"Error: File not found at {script_path}"})
