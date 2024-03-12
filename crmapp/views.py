from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
def dashboard(request):
    item_idf = request.GET.get('item_idf',' ').split(',')
    return render(request, 'dashboard.html',{'item_idf':item_idf})
def archive(request):
    item_ids = request.GET.get('item_ids',' ').split(',')
    return render(request, 'archive.html', {'item_ids': item_ids}) 

def page1(request):
    item_idf = request.GET.get('item_idf',' ').split(',')
    return render(request, 'page1.html',{'item_idf':item_idf})

def page2(request):
    item_ids = request.GET.get('item_ids',' ').split(',')
    return render(request, 'page2.html', {'item_ids': item_ids}) 