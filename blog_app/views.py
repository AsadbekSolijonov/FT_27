from django.shortcuts import render, HttpResponse
import random
import datetime


# Create your views here.
def index(request):
    context = {
        "name": "Asadbek",
        "age": random.randint(1, 24),
        "time": datetime.datetime.now().strftime('%Y.%m.%d'),
        "a": random.randint(1, 1000),
        "b": random.randint(-100, 1000)
    }
    c = context['a'] + context['b']
    c1 = context['a'] * context['b']

    return HttpResponse(f"""<h1 style="color: red;">{context['name']} ning yoshi {context['age']} da.</h1>
    <p>Bugun:<code> {context['time']}</code></p>
    <p>{context['a']} + {context['b']} = {c}</p>
    <p style="color: green; border: 1px solid black; width: 200px; padding: 10px; border-radius: 10px;">{context['a']} x {context['b']} = {c1}</p>
    """)
