from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Referencia
from .serializers import ReferenciaSerializer


@api_view(['GET', 'POST'])
def referencia_list(request):
    """
    List all code Referencia, or create a new referencia.
    """
    if request.method == 'GET':
        referencia = Referencia.objects.all()
        serializer = ReferenciaSerializer(referencia, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReferenciaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# from rest_framework.response import Response
# from .models import Referencia
# from .serializers import ReferenciatSerializer
# from rest_framework.decorators import api_view


# @api_view(['GET'])
# def referenciaList(request):
#     referencia = Referencia.objects.all()
#     serializer = ReferenciaSerializer(referencia, many=True)

# @api_view(['GET'])
# def referenciaDetail(request,pk):
#     referencia = Referencia.objects.get(id=pk)
#     serializer = ReferenciaSerializer(referencia, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def referenciaCreate(request):
#     serializer = ReferenciaSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])

# def referenciaUpdate(request,pk):
#     referencia=Referencia.objects.get(id=pk)
#     serializer = ReferenciaSerializer(instance=referencia,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def referenciaDelete(request,pk):
#     referencia = Referencia.objects.get(id=pk)
#     referencia.delete()
#     return Response('deleted')





