from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import *
from .serialzers import *
from .filters import *
from  rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.db.models import Avg
# Create your views here.

@api_view(['GET'])
def get_all_products(request):
    products=Product.objects.all().order_by('id')
    filterset=ProductsFilter(request.GET,queryset=products)
    respage=2
    countpage=filterset.qs.count()
    paginator=PageNumberPagination()
    paginator.page_size=respage
    queryset=paginator.paginate_queryset(filterset.qs,request)
    serializer=ProductSerializers(queryset,many=True)
    return Response({"product":serializer.data,"count":countpage})



@api_view(['GET'])
def get_product(request,pk):
    product=get_object_or_404(Product,pk=pk)
    serializer=ProductSerializers(product,many=False)
    return Response({"product":serializer.data})



@api_view(['POST'])
@permission_classes([IsAuthenticated,IsAdminUser])
def new_product(request):
    data=request.data
    serializer=ProductSerializers(data=data)
    
    if serializer.is_valid():
        product=Product.objects.create(**data,user=request.user)
        result=ProductSerializers(product,many=False)
        return Response({"product":result.data})
    else:
        return Response(serializer.errors)
        


@api_view(['PUT'])
@permission_classes([IsAuthenticated,IsAdminUser])
def update_product(request,pk):
    product=get_object_or_404(Product,pk=pk)
    
    if product.user != request.user:
         return Response({"error":"you can't update this product"},status=status.HTTP_403_FORBIDDEN)
    product.name=request.data['name']
    product.price=request.data['price']
    product.brand=request.data['brand']
    product.category=request.data['category']
    product.rating=request.data['rating']
    product.stock=request.data['stock']
    product.description=request.data['description']
    product.save()
    result=ProductSerializers(product,many=False)
    return Response({"product":result.data})
       
    
        
@api_view(['DELETE'])
@permission_classes([IsAuthenticated,IsAdminUser])
def delete_product(request,pk):
    product=get_object_or_404(Product,pk=pk)
    
    if product.user != request.user:
         return Response({"error":"you can't update this product"},status=status.HTTP_403_FORBIDDEN)
    product.delete()
   
    return Response({"details":"Delelte is done "})
       
    
        
        
        

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_review(request,pk):
    data=request.data
    product=get_object_or_404(Product,pk=pk)
    user=request.user
    review=product.reviews.filter(user=user)
    
    if data['rating'] >5 or data['rating'] <0:
        return Response({"error":" the rate between 0 -> 5"},status=status.HTTP_400_BAD_REQUEST)
    elif review.exists():
        new_review={'rating':data['rating'],'comment':data['comment']}
        review.update(**new_review)
        rating=product.reviews.aggregate(avg_ratings=Avg('rating'))
        product.rating=rating['avg_ratings']
        product.save()
        return Response({"details":" product review updated"})
    else:
        Review.objects.create(
            user=user,
            product=product,
            rating=data['rating'],
            comment=data['comment']
        )
        rating=product.reviews.aggregate(avg_ratings=Avg('rating'))
        product.rating=rating['avg_ratings']
        product.save()
        return Response({"details":" product review created"})


        

@api_view(['DELETE'])
@permission_classes ([IsAuthenticated]) 
def delete_review(request, pk):
    user = request.user
    product = get_object_or_404(Product,id=pk)
    review = product.reviews.filter(user=user)
    if review.exists():
        review.delete() 
        rating=product.reviews.aggregate(avg_ratings = Avg('rating'))
        if rating['avg_ratings'] is None:
            rating ['avg_ratings'] = 0
            product.ratings = rating['avg_ratings'] 
            product.save()
            return Response({'details':'Product review deleted'})
    return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)