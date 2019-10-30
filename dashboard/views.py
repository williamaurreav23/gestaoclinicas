from bokeh.plotting import figure, output_file, show
from django.shortcuts import render, render_to_response
import matplotlib.pyplot as plt
import numpy as np
from bokeh.embed import components
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def listclientes(request):
    return render(request, 'listclientes.html')


import base64
from io import BytesIO
from matplotlib.figure import Figure

def hello():
   # Generate the figure **without using pyplot**.
   fig = Figure()
   ax = fig.subplots()
   ax.plot([1, 2])
   # Save it to a temporary buffer.
   buf = BytesIO()
   fig.savefig(buf, format="png")
   # Embed the result in the html output.
   data = base64.b64encode(buf.getbuffer()).decode("ascii")
   return f"<img src='data:image/png;base64,{data}'/>"