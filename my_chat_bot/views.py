import environ
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .utils import initials_image
import google.generativeai as genai
from .models import ChatMessage, genaiSetting, Conversation


# Create your views here.

def index(request):
    name = "Umut ÇELİK"
    initials_image(name)
    conversation = get_active_conversation(Conversation.objects.all())


    if request.method == 'POST':
        message = request.POST['message']

        env = environ.Env(DEBUG=(bool, True), )
        environ.Env.read_env()

        GOOGLE_API_KEY = env("GOOGLE_API_KEY")
        genai.configure(api_key=GOOGLE_API_KEY)

        my_instance = genaiSetting.objects.first()  # İlk öğeyi çekmek için örnek bir sorgu
        temperature = my_instance.temperture if my_instance else None
        token = my_instance.max_length if my_instance else None
        top_p = my_instance.top_p if my_instance else None
        top_k = my_instance.top_k if my_instance else None

        print(temperature, token, top_p, top_k)

        model = genai.GenerativeModel('gemini-pro')

        response = model.generate_content(
            message,
            generation_config=genai.types.GenerationConfig(
                # Only one candidate for now.
                candidate_count=1,
                max_output_tokens=token,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
            )
        )

        all_mesages = []
        for chunk in response:
            print(chunk.text)
            all_mesages.append(chunk.text)

        string = " ".join(all_mesages)

        # Kullanıcı mesajını ekle
        chat = ChatMessage(conversation=conversation,message=message, response=string)
        chat.save()



        return redirect('index')

    else:
        conversations = Conversation.objects.all()

        # Son konuşmaları al
        chats = ChatMessage.objects.filter(conversation__in=conversations).order_by('timestamp')

        context = {'chats': chats, 'name': name}
        return render(request, 'index.html', context)



active_conversation = None  # Global değişken


def new_conversation(request):
    # Yeni bir Conversation oluştur
    conversation = Conversation.objects.create(active=True)
    # Burada conversation.id değerini kullanabilirsiniz
    conversation_id = conversation.id
    print("Aktif konuşmanın ID'si:", conversation_id)

    return redirect('index')


def get_active_conversation(conversations):
    active_conversation = conversations.filter(active=True).first()
    return active_conversation
