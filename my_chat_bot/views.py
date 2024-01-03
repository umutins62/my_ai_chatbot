import environ
from django.http import JsonResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from .utils import initials_image
import google.generativeai as genai
from .models import ChatMessage, genaiSetting, Conversation
from .forms import ModelParametersForm


def index(request):
    name = "Umut ÇELİK"
    initials_image(name)

    model_set = genaiSetting.objects.all()
    conversation = get_active_conversation(Conversation.objects.all())

    if not conversation:
        conversation = Conversation.objects.create(active=True)
        conversation_id = conversation.id
        print("Aktif konuşmanın ID'si:", conversation_id)

    message_count = conversation.get_message_count()

    # Aktif sohbetin mesajlarını al
    chats = ChatMessage.objects.filter(conversation=conversation).order_by('timestamp') if conversation else []

    sohbetler = Conversation.objects.all()

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


        form1 = ModelParametersForm()
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
            all_mesages.append(chunk.text)

        string = " ".join(all_mesages)

        # Kullanıcı mesajını ekle
        chat = ChatMessage(conversation=conversation, message=message, response=string)
        chat.save()

        return redirect('index')

    else:
        form1 = ModelParametersForm(request.POST)
        context = {'chats': chats, 'name': name, 'sohbetler': sohbetler, 'message_count': message_count,
                   'model_set': model_set, 'form1': form1, }

        return render(request, 'index.html', context)


active_conversation = None  # Global değişken


def new_conversation(request):
    # Aktif olan Conversation'ı bul
    active_conversation = Conversation.objects.get(
        active=True)  # Varsayılan olarak ilk aktif Conversation'ı alır, gerekirse sıralamayı belirtin

    # Eğer aktif bir Conversation varsa, deaktive et
    if active_conversation:
        active_conversation.active = False
        active_conversation.save()

    # Yeni bir Conversation oluştur
    conversation = Conversation.objects.create(active=True).ç.ççç
    conversation_id = conversation.id
    print("Aktif konuşmanın ID'si:", conversation_id)

    return redirect('index')


def get_active_conversation(conversations):
    active_conversation = conversations.filter(active=True).first()
    return active_conversation


def activate_conversation(request, conversation_id):
    try:
        # Seçilen Conversation'ı bul
        selected_conversation = Conversation.objects.get(id=conversation_id)

        # Diğer tüm Conversation'ları deaktive et
        Conversation.objects.exclude(id=conversation_id).update(active=False)

        # Seçilen Conversation'ı aktive et
        selected_conversation.active = True
        selected_conversation.save()

    except Conversation.DoesNotExist:
        # Eğer seçilen Conversation bulunamazsa, hata işleme yapabilirsiniz
        pass

    return redirect('index')


def delete_conversation(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)

    # Diğer kontrolleri ve yetkilendirmeleri buraya ekleyebilirsin.

    # Konuşmayı sil
    conversation.delete()

    return redirect('index')  # Silindikten sonra ana sayfaya yönlendir


def update_model(request):
    if request.method == 'POST':

        form = ModelParametersForm(request.POST)
        if form.is_valid():
            model_instance = genaiSetting.objects.get(pk=1)
            model_instance.temperture = form.cleaned_data['temperture']
            model_instance.max_length = form.cleaned_data['max_length']
            model_instance.top_p = form.cleaned_data['top_p']
            model_instance.top_k = form.cleaned_data['top_k']
            model_instance.save()
            return redirect('index')
        else:

            model_instance = genaiSetting.objects.get(pk=1)
            form = ModelParametersForm(instance=model_instance)
            return render(request, 'index.html', {'form ': form})
