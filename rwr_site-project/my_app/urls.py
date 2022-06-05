from django.urls import path
from my_app import views

urlpatterns=[
    # This is the standard method
    # path('',views.simple_view),
    # path('sports/',views.sports_view), # /my_app/sports
    # path('finance/',views.finance_view),  # /my_app/finance
    # This uses topic to read dictionary
    path('<int:num_page>',views.num_page_view),
    path('<str:topic>/',views.news_view,name='topic-page'),
    path('<int:num1>/<int:num2>',views.add_view)

]
