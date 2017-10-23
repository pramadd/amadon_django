# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    
    return render(request,'amadon/index.html')

def checkout(request):
    
    return render(request,'amadon/checkout.html')

def payment(request):
    quantity = float(request.POST['quantity'])
    if not 'price' in request.session:
        request.session['price'] = 0
    if not 'total' in request.session:
        request.session['total'] = 0
    if not 'count' in request.session:
        request.session['count'] = 0

    if request.POST['product_id'] == '1':
        request.session['price'] = 19.99 * quantity
    elif request.POST['product_id'] == '2':
        request.session['price'] = 74.99 * quantity
    elif request.POST['product_id'] == '3':
        request.session['price'] = 7.99 * quantity
    elif request.POST['product_id'] == '4':
        request.session['price'] = 3.99 * quantity
    
    quantity = int(quantity)
    print quantity

    request.session['count'] += quantity
    request.session['total'] += request.session['price']

    return redirect('/checkout')
