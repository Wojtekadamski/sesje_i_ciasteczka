from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View


class Index(View):

    def get(self, request):
        session = request.session.get('session')
        return render(request, 'Index.html',{'session': session})

    def post(self, request):
        pass


class ShowSessionView(View):
    def get(self, request):
        session = request.session.get('sroka')
        return render(request, 'session.html', {'session': session})


class SetSessionView(View):
    def get(self, request):
        session = request.POST.get('sikorka')
        return render(request, 'set_session.html', {'session': session})

    def post(self, request):
        session = request.POST.get('sikorka')
        request.session['sroka'] = session

        return redirect('/')
