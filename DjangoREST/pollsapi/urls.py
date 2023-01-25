from django.urls import path

from . import views
from .views import polls_detail,polls_list,index
from .apiviews import PollList,PollDetail


urlpatterns = [
    path('',index,name='index'),
    path('polls/',PollList.as_view(), name='polls_list'),
    path('polls/<int:pk>',PollDetail.as_view(),name='polls_detail'),
    # path('polls/update',PollDetail.as_view(),name='update'),
    path('polls/update/<int:pk>',PollDetail.as_view(),name='update_poll')
]