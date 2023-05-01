from django.urls import path
from . import views

urlpatterns = [
    path('api/initiative/', views.InitiativeList.as_view(), name='initiative_list'),
    path('api/initiative/<int:pk>', views.InitiativeDetail.as_view(), name='initiative_detail')
]