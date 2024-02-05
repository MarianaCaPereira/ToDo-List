#from app.views import TodoListAndCreat, TodoDetailChangeAndDelete
#from app.views import todo_list, todo_detail_change_and_delete
#from django.urls import path

from app.views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls


"""
urlpatterns = [
    path('', TodoListAndCreat.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view()),
]

urlpatterns = [
    path('', todo_list),
    path('<int:pk>/', todo_detail_change_and_delete),
]
"""
