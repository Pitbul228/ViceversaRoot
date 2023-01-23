from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    len_of_text = len(user_text.split())
    reverse_user_text = user_text[::-1]
    return render(request, 'reverse.html', {'user_text': user_text,
                                            'reverse_user_text': reverse_user_text,
                                            'len_of_text': len_of_text})
