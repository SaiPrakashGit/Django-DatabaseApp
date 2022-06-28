from django.urls import path

from .views import RecordList, RecordDetail, RecordCreate, RecordUpdate, RecordDelete, AppLoginView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', AppLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name = 'logout'),
    
    path('', RecordList.as_view(), name = 'records'),
    path('record/<int:pk>', RecordDetail.as_view(), name = 'record'),
    path('record-create/', RecordCreate.as_view(), name = 'record-create'),
    path('record-update/<int:pk>', RecordUpdate.as_view(), name = 'record-update'),
    path('record-delete/<int:pk>', RecordDelete.as_view(), name = 'record-delete'),
]