from django.shortcuts import render

# define the definition/function to return our template page
def zinggrid(request):
    title = "Mque paso!"
    return render(request, 'zinggrid.html', {'title': title})