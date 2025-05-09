from django.urls import path
from . import views

urlpatterns = [
    path("home/page/", views.teacher_home_page, name='teacher_home_page'),
    path("profile/", views.teacher_profile, name='teacher_profile'),
    path('add/question/<int:subject_id>',views.add_question,name='add_question'),
    path('manage/question/',views.manage_question,name='manage_question'),
    path('view/questions/<int:subject_id>',views.view_question,name='view_questions'),
    path('add/notes/<int:subject_id>',views.add_notes,name='add_notes'),
    path('manage/notes',views.manage_notes,name='manage_notes'),
    path('view/notes/<int:subject_id>',views.view_notes,name='view_notes'),
    path('viewa/notesa',views.view_aa,name='view_aa'),
    path('edit/question/<int:question_id>/', views.edit_question, name='edit_question'),
    path('delete/question/<int:question_id>/', views.delete_question, name='delete_question'),
    path("apply/leave/", views.apply_leave,name='apply_leave'),
    path('bookmarked/books/',views.bookmarked_book,name='bookmark_book'),
    path('create/bookmark/<int:book_id>/',views.create_bookmark, name='create_bookmark'),
    path('delete/bookmark/<int:bookmark_id>/', views.delete_bookmark, name='delete_bookmark'),
    
    
]