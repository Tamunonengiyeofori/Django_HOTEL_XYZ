from django.shortcuts import redirect, render
from .forms import HotelRecordForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def create_record_view(request):
    form = HotelRecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(home)
    context = {"form": form}
    # context["form"] = HotelRecordForm()
    return render(request, "create_record.html", context)