from django.http import HttpResponse ,JsonResponse

def home_page (request):
    print("home page requested ")
    friends=['ankit',
             'takshil',
             'sam'
             ]
    return JsonResponse(friends,safe=False)