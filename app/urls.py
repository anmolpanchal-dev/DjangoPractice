from .views import indexView, aboutView, contactView, saveDataView, deleteView, updateViewPage
from django.urls import path
urlpatterns = [
    path('',indexView, name = "index"),
    path('about/',aboutView, name = "about"),
    path('contact/',contactView, name = "contact"),
    path('save-data',saveDataView, name = "saveData"),
    path('delete-note/<int:id>',deleteView, name = "deleteView"),
    path('update-note/<int:id>',updateViewPage, name = "updateViewPage"),
]