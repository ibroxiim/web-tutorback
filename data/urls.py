from django.urls import path
from .views import (
    # Category views
    CategoryCreateView,
    CategoryListView,
    CategoryDetailView,
    CategoryUpdateView,
    CategoryDeleteView,

    # Lesson views
    LessonCreateView,
    LessonListView,
    LessonDetailView,
    LessonUpdateView,
    LessonDeleteView,
)

urlpatterns = [
    # ---- CATEGORY URLS ----
    path('categories_list/', CategoryListView.as_view()),
    path('categories/create/', CategoryCreateView.as_view()),
    path('categories/<uuid:uid>/', CategoryDetailView.as_view()),
    path('categories/<uuid:uid>/update/', CategoryUpdateView.as_view()),
    path('categories/<uuid:uid>/delete/', CategoryDeleteView.as_view()),

    # ---- LESSON URLS ----
    path('lessonlist/', LessonListView.as_view()),
    path('lessons/create/', LessonCreateView.as_view()),
    path('lessons/<uuid:uid>/', LessonDetailView.as_view()),
    path('lessons/<uuid:uid>/update/', LessonUpdateView.as_view()),
    path('lessons/<uuid:uid>/delete/', LessonDeleteView.as_view()),
]
