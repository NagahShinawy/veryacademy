from django.http import HttpResponse


def index(request):
    # http://127.0.0.1:8082/tryeveything/?name=john&age=34&skills=html&skills=python&skills=django

    # <QueryDict: {'name': ['john'], 'age': ['34'], 'skills': ['html', 'python', 'django']}>
    print(request.GET)
    request.GET.getlist("skills")  # ['html', 'python', 'django']
    return HttpResponse("Try everything")
