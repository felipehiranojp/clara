from django.urls import path 
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("checkout_session",views.checkout_session,name='checkout_session'),
    path("create_checkout_session",views.create_checkout_session,name='create_checkout_session'),
    path('stripe_webhook',views.stripe_webhook, name='stripe_webhook'),
    path("success/",views.success,name='success'),
    path("cancel",views.cancel,name='cancel'),
    path("estilo",views.estilo,name='estilo'),
    path("portifolio",views.portifolio,name='portifolio'),
    path("logout",views.logout,name='logout'),
    path("redes",views.redes,name='redes'),
    path("quiz1",views.quiz1,name='quiz1'),
    path("quiz2",views.quiz2,name='quiz2'),
    path("quiz3",views.quiz3,name='quiz3'),
    path("quiz4",views.quiz4,name='quiz4'),
    path("quiz5",views.quiz5,name='quiz5'),
    path("quiz6",views.quiz6,name='quiz6'),
    path("quiz7",views.quiz7,name='quiz7'),
    path("quiz8",views.quiz8,name='quiz8'),
    path("quiz9",views.quiz9,name='quiz9'),




] 