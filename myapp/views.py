from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import course
from .serializers import CourseSerializer
from .permissions import IsInstructor
from rest_framework.pagination import PageNumberPagination
from myapp.models import course
#
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import course


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set the current user as the instructor when creating a new course
        serializer.save(instructor=self.request.user)

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

class CourseListCreateView(generics.ListCreateAPIView):
    # ...
    permission_classes = [IsAuthenticated, IsInstructor]

class CourseListCreateView(generics.ListCreateAPIView):
    # ...
    
    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return course.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    
class CoursePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CourseListCreateView(generics.ListCreateAPIView):
    # ...
    pagination_class = CoursePagination

#
class CourseListView(ListView):
    model = course
    template_name = 'main/index.html'
    context_object_name = 'course'

class CourseDetailView(DetailView):
    model = course
    template_name = 'main/detail.html'
    context_object_name = 'course'

def index(request):
    course1=course.objects.all()
    return render(request,'main/index.html', {'course1': course1})

def detail(request, pk):
    c = get_object_or_404(course, pk=pk)

    return render(request,'main/detail.html', {'c': c})