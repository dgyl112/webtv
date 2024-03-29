from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('upload', views.upload_file, name='upload'),
    path('upload_success', views.upload_success, name='upload_success'),
    path('csv', views.csv_view, name='csv_view'),
    path('csv_big', views.csv_streaming_view, name='csv_streaming_view'),
    path('pdf_simple', views.pdf_simple_view, name='pdf_simple_view'),
    path('pdf_complex', views.pdf_complex_view, name='pdf_complex_view'),

]
