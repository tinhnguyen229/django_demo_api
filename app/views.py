from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer


@api_view(['GET'])
def get_course_list(request):
    courses = Course.objects.all()
    datas = CourseSerializer(courses, many=True)
    return Response(data=datas.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def post_course(request):
    req_data = request.data
    new_course = CourseSerializer(data=req_data)
    if not new_course.is_valid():
        return Response(data='Wrong input', status=status.HTTP_400_BAD_REQUEST)
    new_course.save()
    return Response(data=new_course.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def get_course_detail(request, id):
    try:
        course = Course.objects.get(id=id)
    except:
        return Response(data='This course does not exist', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        datas = CourseSerializer(course)
        return Response(data=datas.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        # updated_course = CourseSerializer(course, data=request.data)
        # if not updated_course.is_valid():
        #     return Response(data='Wrong input', status=status.HTTP_400_BAD_REQUEST)

        for key in ('title', 'price', 'content'):
            value = request.data.get(key, False)
            if value:
                setattr(course, key, value)
        course.save()
        return Response(data=CourseSerializer(course).data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        course.delete()
        return Response(data='Delete successfully', status=status.HTTP_200_OK)



