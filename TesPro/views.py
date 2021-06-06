from django.shortcuts import render
from django.http import JsonResponse

# define the definition/function to return our template page
def zinggrid(request):
    title = 'sMque paso!'
    return render(request, 'zinggrid.html', {'title': title})
def verjson(request):
    data={
    
      'first_name': 'Airi',
      'last_name': 'Satou',
      'position': 'Accountant',
      'office': 'Tokyo',
      'start_date': '28th Nov 08',
      'salary': '$162,700'
    }
  
    return JsonResponse(data)
