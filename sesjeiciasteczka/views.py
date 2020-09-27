from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


class Index(View):

    def get(self, request):
        session = request.session.get('session')
        cookies = request.COOKIES.get('cos')
        return render(request, 'Index.html', {'session': session, 'cookies': cookies})

    def post(self, request):
        pass


class ShowSessionView(View):
    def get(self, request):
        session = request.session.get('session')
        cookies = request.COOKIES['cos']
        return render(request, 'Index.html', {'session': session, 'cookies': cookies})


class ShowCookieView(View):
    def get(self, request):
        session = request.session.get('session')
        cookie = request.COOKIES['cos']
        return render(request, 'Index.html', {'session': session, 'cookie': cookie})


class SetSessionView(View):
    def get(self, request):
        session = request.session.get('session')
        cookies = request.COOKIES['cos']
        return render(request, 'Index.html', {'session': session, 'cookies': cookies})

    def post(self, request):
        session = request.POST.get('sikorka')
        request.session['sroka'] = session

        return redirect('/')


class SetCookieView(View):
    def get(self, request):
        return render(request, 'set_session.html')

    def post(self, request):
        http_response = redirect("/")
        value = request.POST.get('sikorka')
        http_response.set_cookie(key='cos', value=value)
        return http_response


class DelSessionView(View):

    def get(self, request):
        del request.session['sroka']
        return redirect("/")


class SetSessionKeyValue(View):
    def get(self, request):
        return render(request, 'sessionKeyValue.html')

    def post(self, request):
        key = request.POST.get('key')
        value = request.POST.get('value')
        session = request.session[f'{key}'] = f'{value}'
        return redirect('/')


class ShowSessionKeyValue(View):
    def get(self, request):
        session = request.session.items()

        return render(request, 'showSessionKeyValue.html', {'session': session})


class DelSessionKeyValue(View):
    def get(self, request):
        session = request.session.items()
        return render(request, 'del_sessionkeyvalue.html', {'session': session})

    def post(self, request):
        choice = request.POST.getlist('choice')

        for elem in choice:
            del request.session[f'{elem}']

        return redirect("/")