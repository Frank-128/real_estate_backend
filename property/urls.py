from django.urls import path
from .views import PropertyCategoryAPI,PropertyCategoryDetailAPI,PropertyTypeList,PropertyTypeDetail,PropertyDetail,PropertyList,AttributeDetail,AttributeList

urlpatterns =[
    path('category',PropertyCategoryAPI.as_view()),
    path('category/<int:pk>',PropertyCategoryDetailAPI.as_view()),
    path('property_type',PropertyTypeList.as_view()),
    path('property_type/<int:pk>',PropertyTypeDetail.as_view()),
    path('attribute',AttributeList.as_view()),
    path('attribute/<int:pk>',AttributeDetail.as_view()),
    path('property',PropertyList.as_view()),
    path('property/<int:pk>',PropertyDetail.as_view())
]