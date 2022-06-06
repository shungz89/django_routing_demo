from django.urls import path
from . import views

#domain.com/first_app/


urlpatterns = [
    path('<int:num_page>/',views.num_page_view),
    path('<str:topic>/',views.news_view, name='topic-page'),

]