from django.shortcuts import render, get_object_or_404
from .models import item_model
from .forms import ItemForm


def main(request):
    if request.method == "POST":
        form = ItemForm(request.POST or None)
        if form.is_valid():
            form.save()

        items = item_model.objects.all()
        item_form = ItemForm

        return render(request, 'main/main.html', {'items':items, 'form': item_form})

    else:
        items = item_model.objects.all()
        item_form = ItemForm
        return render(request, 'main/main.html', {'items': items, 'form': item_form})


def item(request, id):
    items = item_model.objects.order_by("?")[:3]
    item_id = get_object_or_404(item_model, id=id)
    return render(request, 'main/item.html', {'item_id': item_id, 'items': items})
