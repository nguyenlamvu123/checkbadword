from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from checkbadword import foo


@csrf_exempt
def some_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        ret = foo(text, django=True)
    else:
        raise
    return HttpResponse(ret)

