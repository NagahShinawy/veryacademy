from django.http import HttpResponse


def index(request):
    # http://127.0.0.1:8082/tryeveything/?name=john&age=34&skills=html&skills=python&skills=django

    # <QueryDict: {'name': ['john'], 'age': ['34'], 'skills': ['html', 'python', 'django']}>
    print(request.GET)
    request.GET.getlist("skills")  # ['html', 'python', 'django']
    print(request.GET["skills"])  # return last value: django
    name = request.GET.get("name")
    skills = request.GET.getlist("skills")
    content = "Try everything"
    if name:
        content = f"Try everything, {name.title()}"

    if skills:
        content += f"Your skills : {','.join(skills[:-1])} and {skills[-1]}"

    print(
        request.GET.get("price", 100)
    )  # if 'price' passed but no value ==> '' empty return because price is still exist in the url but no value.
    # so, it considered 'price' as empty because it passed
    print(
        request.GET.get("price") or 100
    )  # if 'price' passed but no value ==> 100 return
    # check value ('') (empty) returned or 100
    return HttpResponse(content)
