from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import *
from .serialzers import *
from  rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from  .models import *
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_orders(request):
    orders=Order.objects.all()
    serializer= OrderSerializers(orders,many=True)
    return Response({"orders":serializer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order(request,pk):
    order=get_object_or_404(Order,id=pk)
    serializer= OrderSerializers(order,many=False)
    return Response({"order":serializer.data})



@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_order(request,pk):
    order=get_object_or_404(Order,id=pk)
    order.status=request.data['status']
    order.save()
    serializer= OrderSerializers(order,many=False)
    return Response({"order":serializer.data})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_order(request,pk):
    order=get_object_or_404(Order,id=pk)
    order.delete()    
    return Response({"detials":"order is deleted"})




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_order(request):
    user=request.user
    data=request.data
    order_items=data['order_items']
    if order_items and len(order_items)==0:
        return Response({'error':'No order recieved'},status=status.HTTP_400_BAD_REQUEST)
    totoal_amount=sum(item['price']*item['quantity'] for item in order_items)
    order=Order.objects.create( 
    user=user,
    city=data['city'],
    zipcode=data['zipcode'],
    street=data['street'],
    country=data['country'],
    phone_number=data['phone_number'],
    total_amount=totoal_amount,
        )
    for i in order_items:
        product=Product.objects.get(id=i['product'])
        item=OrderItem.objects.create(
            product=product,
            order=order,
            name=product.name,
            quantity=i['quantity'],
            price=i['price']
        )
        product.stock-=item.quantity
        product.save()
    serializers=OrderSerializers(order,many=False)
    return Response(serializers.data)
    
        
        