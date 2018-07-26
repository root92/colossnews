from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobsView.as_view(), name='jobs_list'),
    path('<int:pk>/', views.JobsDetailView.as_view(), name='jobs_details'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]