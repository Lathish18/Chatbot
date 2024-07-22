from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Chat

def custom_logic(message, user_name):
    message = message.lower()
    if "hi" in message or "hii" in message:
        return  f"Hey, {user_name}! How can I assist you today?"
    elif "news" in message:
        return "I can provide the latest news. What topic are you interested in?"
    elif "time" in message:
        return "I can tell you the current time. Where are you located?"
    elif "joke" in message:
        return "I can tell you a joke. Want to hear one?"
    elif "quote" in message:
        return "I can share an inspiring quote with you. Would you like one?"
    elif "define" in message:
        return "I can define words for you. What word would you like defined?"
    elif "reminder" in message:
        return "I can set reminders for you. What would you like to be reminded about?"
    elif "recipe" in message:
        return "I can provide recipes. What kind of dish are you looking for?"
    elif "sports" in message:
        return "I can provide sports updates. Which sport are you interested in?"
    elif "music" in message:
        return "I can recommend music. What genre or artist do you like?"
    else:
        return "Sorry, I don't understand that."


@login_required
def chatbot(request):
    chats = Chat.objects.filter(user=request.user).order_by('created_at')

    if request.method == 'POST':
        message = request.POST.get('message')
        user_name = request.user.username
        response = custom_logic(message, user_name)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    else:
        chats = []
    return render(request, 'chatbot.html', {'chats': chats})

@login_required
def chat_history(request):
    chats = Chat.objects.filter(user=request.user)
    return render(request, 'chathistory.html', {'chats': chats})

@login_required
def delete_history(request):
    if request.method == 'POST':
        Chat.objects.filter(user=request.user).delete()
        return redirect('chat_history')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except Exception as e:
                error_message = f"Error creating account: {str(e)}"
            return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = "Passwords don't match"
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')
