from app.models import Todo #class
from app.serializers import TodoSerializer
from rest_framework import viewsets


from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

"""
Forma 3:
class TodoListAndCreat(generics.ListCreateAPIView): #implementa os métodos get port automaticamente
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailChangeAndDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

Forma 2:
class TodoListAndCreat(APIView):
    def get(self, request):
        todo = Todo.objects.all() #Pegar todos os objetos do BD "SELECT * FROM todo"
        serializer = TodoSerializer(todo, many=True) #Informar que são vários objs na variável
        return Response(serializer.data)

    def post(self, request):
        serializer =  TodoSerializer(data=request.data) #Verificar se a requisição que foi feita está correta
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #Obj criado
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Obj inválido

class TodoDetailChangeAndDelete(APIView):
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data) #retornar o obj

    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data) #Verificar a requisição que chegou no servidor
        if serializer.is_valid():
            serializer.save() #Salva se válida
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Erro

    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

Forma 1:
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
    def todo_detail_change_and_delete(request, pk):
        try:
            todo = Todo.objects.get(pk)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
"""
