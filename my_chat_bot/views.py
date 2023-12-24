import environ
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .utils import initials_image
import google.generativeai as genai
from .models import ChatMessage


# Create your views here.

def index(request):
    name = "Umut ÇELİK"
    initials_image(name)

    if request.method == 'POST':
        message = request.POST['message']
        print(message)

        env = environ.Env(DEBUG=(bool, True), )
        environ.Env.read_env()

        GOOGLE_API_KEY = env("GOOGLE_API_KEY")
        genai.configure(api_key=GOOGLE_API_KEY)

        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(message, stream=True)
        all_mesages = []
        for chunk in response:
            print(chunk.text)
            all_mesages.append(chunk.text)



        string = " ".join(all_mesages)

        chat = ChatMessage(message=message, response=string)
        chat.save()

        chats = ChatMessage.objects.all()


        return redirect('index')

    else:
        chats = ChatMessage.objects.all()


        return render(request, 'index.html', {'chats': chats, "name": name})
