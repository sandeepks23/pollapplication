from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,DetailView
# Create your views here.

from pollapp.models import Polls
from pollapp.forms import PollForm

class HomePageView(TemplateView):
    template_name = "homepage.html"
    context={}
    def get(self, request, *args, **kwargs):
        polls=Polls.objects.all()
        self.context['polls']=polls
        return render(request,self.template_name,self.context)

class CreatePoll(CreateView):
    template_name = "createpoll.html"
    model = Polls
    form_class = PollForm
    success_url = reverse_lazy("home")


# class ViewPoll(DetailView):
#     template_name = "viewpoll.html"
#     model = Polls
#     context_object_name = "poll"

class ViewPoll(TemplateView):
    template_name = "viewpoll.html"
    context={}
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        poll=Polls.objects.get(id=id)
        self.context['poll']=poll
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        poll = Polls.objects.get(id=id)
        selected_option=request.POST.get('options',False)
        if selected_option:
            if selected_option=='option_a':
                poll.a_count+=1
            elif selected_option=='option_b':
                poll.b_count += 1
            elif selected_option=='option_c':
                poll.c_count += 1
        else:
            return redirect("view",poll.id)
            # return render(request,self.template_name)
        poll.save()
        return redirect("result",poll.id)

class PollResultView(DetailView):
    template_name = "results.html"
    model=Polls
    context_object_name = "poll"
# class OptionA(TemplateView):
#     template_name = "results.html"
#     context={}
#     def get(self, request, *args, **kwargs):
#         id=kwargs.get("pk")
#         poll=Polls.objects.get(id=id)
#         poll.a_count+=1
#         poll.save()
#         self.context['poll']=poll
#         return render(request,self.template_name,self.context)

# class CastVoteView(TemplateView):
#     template_name = "results.html"
#     context={}
#     def post(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         poll=Polls.objects.get(id=id)
#         print(request.POST['option'])

