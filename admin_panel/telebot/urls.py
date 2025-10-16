from django.urls import path

from admin_panel.telebot.views import save_answer

urlpatterns = [
    path('save_answer', save_answer, name='save_answer'),

]
