from django.http import HttpResponseRedirect
from Product.models import Product_main_class
from .forms import commentform
from .models import comment
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/user/login')
def comment_page(request):
    forms_comment = commentform(request.POST or None)
    Subject = request.POST.get('subject') or None
    Massege = request.POST.get('massege') or None

    if (Subject and Massege) is not None:
        prodduct = request.POST.get('product_id')
        parent = request.POST.get('parent')
        # try:
        product = Product_main_class.objects.get_by_id(product_id=prodduct)

        comment.objects.create(user=request.user, subject=Subject, massege=Massege, product_id=product,
                                   parent_id=parent)

        # except:
        #     pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
