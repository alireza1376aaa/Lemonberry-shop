from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from Send_and_Factor.models import Send_Factor
from shopping_cart.models import Final_cart, finally_order
from shopping_cart.number_to_words import convert


class Show_list_factor(ListView):
    model = Final_cart
    template_name = 'list_factoe.html'

    def get_queryset(self):
        data = super(Show_list_factor, self).get_queryset()
        data = data.filter(is_pay=True)
        return data

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Show_list_factor, self).get_context_data()
        context['count'] = self.get_queryset().count()
        return context


def show_factor_admin(request, code_factor):
    if request.user.is_superuser:
        order = Final_cart.objects.filter(is_pay=True, Order_number=code_factor).first()
        if order is not None:
            send = Send_Factor.objects.filter(basket=order).first()
            addres = finally_order.objects.filter(user=request.user).first()
            takhfif = int(order.total_price_without_discount() - order.total_price())
            work_number = convert(str(order.total_price()))
            context = {'data': order, 'send': send, 'addres': addres, 'takhfif': takhfif, 'work_number': work_number}
            return render(request, 'factor/Factor.html', context)
    else:
        raise Http404()
