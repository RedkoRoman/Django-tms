from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from relations.models import Student, Teacher, Course, CourseStudent


class CourseStudentInline(admin.StackedInline):
    model = CourseStudent
    extra = 1


class StudentInline(admin.TabularInline):
    model = Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'last_name', 'first_name', 'age', 'teacher', 'display_courses', 'display_photo', 'custom_field', 'is_study'
    )
    readonly_fields = ('custom_field', 'display_photo', 'display_courses')
    list_filter = ('teacher', 'last_name', )
    search_fields = ('first_name', 'last_name', )
    ordering = ('last_name', 'first_name')
    list_editable = ('age',)

    fieldsets = (
        ('Main Information', {
            'fields': ('first_name', 'last_name', 'age', 'teacher', 'display_courses'),
        }),
        ('Additional Information', {
            'fields': ('about_me', 'photo', 'custom_field', 'display_photo'),
            'classes': ('collapse',),
        })
    )

    actions = ('change_is_study', 'change_is_not_study', 'change_age')

    raw_id_fields = ('teacher', )

    inlines = (CourseStudentInline, )

    def custom_field(self, obj):
        return 'hello world' if obj.age % 2 else '------'

    def display_photo(self, obj):
        return format_html('<img src="{}" height="50"/>', obj.photo.url) if obj.photo else ''

    def display_courses(self, obj):
        courses = obj.course.all()
        href = '<a href="{}">{}</a>'
        url = 'admin:relations_course_change'
        links = [format_html(href, reverse(url, args=[course.id]), course.name) for course in courses]
        return format_html(', '.join(links))

    def change_is_study(self, request, queryset):
        queryset.update(is_study=False)
        self.message_user(request, 'Remove students from study')

    def change_is_not_study(self, request, queryset):
        queryset.update(is_study=True)
        self.message_user(request, 'Return students to study')

    def change_age(self, request, queryset):
        queryset.update(age=30)

    display_photo.short_description = 'Photo'
    display_courses.short_description = 'Courses'
    change_is_study.short_description = 'Remove students from study'
    change_is_not_study.short_description = 'Return students to study'
    change_age.short_description = 'Change age to 30'


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'id', 'first_name', 'age')

    inlines = (StudentInline, )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


@admin.register(CourseStudent)
class CourseStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'course_id', 'date')
    date_hierarchy = 'date'