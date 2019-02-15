from django.shortcuts import render
#from django.contrib.auth.models import User
from .filters import LandlineFilter
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
        ListView, 
        DetailView, 
        CreateView,
        UpdateView,
        DeleteView
    )
from .models import Landline, Broadband


# Create your views here.
def home(request):
    context = {
        'landline' : Landline.objects.all()
    }
    return render(request, 'plans/home.html', context)


class LandlineListView(ListView):
    model = Landline
    template_name = 'plans/home.html'
    context_object_name = 'landline'
    ordeing = ['-date_posted']


class LandlineDetailView(DetailView):
    model = Landline


class LandlineCreateView(LoginRequiredMixin, CreateView):
    model = Landline
    fields = ['planname', 'applicability', 'fmc', 'talkvalue', 'callcharges', 'remark']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class LandlineUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Landline
    fields = ['planname', 'applicability', 'fmc', 'talkvalue', 'callcharges', 'remark']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        landline = self.get_object()
        if self.request.user == landline.author:
            return True
        return False


class LandlineDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Landline
    success_url = '/'

    def test_func(self):
        landline = self.get_object()
        if self.request.user == landline.author:
            return True
        return False


def about(request):
    return render(request, 'plans/about.html', {'title': 'About'})

# def search(request):
#     user_list = User.objects.all()
#     user_filter = UserFilter(request.GET, queryset=user_list)
#     return render(request, 'plans/user_list.html', {'filter': user_filter})

class BroadbandListView(ListView):
    model = Broadband
    template_name = 'plans/bbhome.html'
    context_object_name = 'broadband'
    ordeing = ['-date_posted']

class BroadbandDetailView(DetailView):
    model = Broadband


class BroadbandCreateView(LoginRequiredMixin, CreateView):
    model = Broadband
    fields = ['planname', 'speed', 'fmc', 'freedata', 'freeCalls', 'callcharges', 'securitydeosit', 'addfac', 'remark']
    success_url = '/broadband'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BroadbandUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Broadband
    fields = ['planname', 'speed', 'fmc', 'freedata', 'freeCalls', 'callcharges', 'securitydeosit', 'addfac', 'remark']
    success_url = '/broadband'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        broadband = self.get_object()
        if self.request.user == broadband.author:
            return True
        return False


class BroadbandDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Broadband
    success_url = '/broadband'

    def test_func(self):
        broadband = self.get_object()
        if self.request.user == broadband.author:
            return True
        return False
