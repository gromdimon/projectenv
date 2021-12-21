from django.urls import path
from .views import main, item

urlpatterns = [
    path ('', main),
    path('item_id/', item),
]