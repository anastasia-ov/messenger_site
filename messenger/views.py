from django.shortcuts import render
from .forms import LoginForm, MessageForm, ChangePasswordForm
from .models import Message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, Http404

# Create your views here.

def ivan_only(user):
    return user.username == 'ivan'


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].strip()
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                form.add_error('username', 'Неправильный логин или пароль.')
            else:
                login(request, user)
                goto = request.GET.get('next', '/')
                return HttpResponseRedirect(goto)
    else:
        form = LoginForm()

    return render(request, 'login.html', context={'form': form})


@login_required
def messages_view(request, folder='inbox'):
    messages =[]
    inbox = False
    if folder == 'inbox':
        messages = Message.objects.filter(addressee=request.user).order_by('-date_sent')
        inbox = True
    elif folder == 'outbox':
        messages = Message.objects.filter(sender=request.user).order_by('-date_sent')
    
    return render(request, 'messages.html', context={'messages': messages, 'inbox': inbox})


@login_required
# @user_passes_test(ivan_only)
def new_message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            addressee_name = form.cleaned_data['addressee']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            try:
                addressee = User.objects.get(username=addressee_name)
            except User.DoesNotExist:
                form.add_error('addressee', 'Пользователь не существует.')
            else:
                m = Message(addressee=addressee, sender=request.user, subject=subject, body=body)
                m.save()
                return HttpResponseRedirect('/outbox/')
    else:
        form = MessageForm()

    return render(request, 'new_message.html', context={'form': form})


def message_sent_view(request):
    pass


@login_required
def full_message_view(request, id):
    try:
        message = Message.objects.get(id=id)
    except Message.DoesNotExist:
        raise Http404
    if message.addressee == request.user or message.sender == request.user:
        return render(request, 'full_message.html', context={'message': message})
    else:
        raise Http404


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/login/')

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            old_pass = form.cleaned_data['old_password']
            new_pass = form.cleaned_data['new_password']
            rep_pass = form.cleaned_data['repeat_password']
            if new_pass != rep_pass:
                form.add_error('new_password', 'Пароли не совпадают')
            else:
                user = authenticate(username=request.user.username, password=old_pass)
                if user is None:
                    form.add_error('old_password', 'Пароль не совпадает')
                else:
                    user.set_password(new_pass)
                    user.save()
                    return render(request, 'password_changed.html')
    else:
        form = ChangePasswordForm()

    return render(request, 'change_password.html', context={'form': form})