from django.urls import path
from pollapp.views import HomePageView,CreatePoll,ViewPoll,PollResultView
urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('createpoll',CreatePoll.as_view(),name='create'),
    path('view/<int:pk>',ViewPoll.as_view(),name='view'),
    # path('vote/<int:pk>',CastVoteView.as_view(),name='vote'),
    path('result/<int:pk>',PollResultView.as_view(),name='result')
]