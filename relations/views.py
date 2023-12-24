import datetime

from django.urls import reverse
from django.views import generic
from django.utils.translation import gettext_lazy as _

from relations.form import StudentForm
from relations.models import Student, CourseStudent


class StudentsListView(generic.ListView):
    template_name = 'relations/relations_list.html'
    context_object_name = 'students'
    queryset = Student.objects.all()

    # select_related - O2O, O2M
    # prefetch_related - M2O, M2M

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_text'] = _('Hello world')
        return context


class StudentsCreateView(generic.CreateView):
    template_name = 'relations/relations_create.html'
    form_class = StudentForm

    def form_valid(self, form):
        response = super().form_valid(form)

        selected_courses = form.cleaned_data.get('courses')

        course_students_objects = [
            CourseStudent(student=self.object, course=course, date=datetime.date.today())
            for course in selected_courses
        ]

        CourseStudent.objects.bulk_create(course_students_objects)

        return response

    # def form_invalid(self, form):
    #     response = super().form_valid(form)
    #     return response

    def get_success_url(self):
        return reverse('students')