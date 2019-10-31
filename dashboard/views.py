from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def listclientes(request):
    return render(request, 'listclientes.html')


from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.plotting import figure

output_file("dashboard/templates/bar_stacked.html")

indices = ['despesas', 'receitas', 'lucro']
years = ["2017", "2018", "2019"]
colors = ["#c9d9d3", "#718dbf", "#e84d60"]

data = {'indices' : indices,
        '2017'   : [23, 14, 47],
        '2018'   : [53, 36, 43],
        '2019'   : [38, 27, 44]}

p = figure(x_range=indices, plot_height=250, title="indices da Empresa",
           toolbar_location=None, tools="hover", tooltips="$name @indices: @$name")

p.vbar_stack(years, x='indices', width=0.9, color=colors, source=data,
             legend=[value(x) for x in years])

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"

from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.iris import flowers

colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
colors = [colormap[x] for x in flowers['species']]

p = figure(title = "Iris Morphology")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Petal Width'

p.circle(flowers["petal_length"], flowers["petal_width"],
         color=colors, fill_alpha=0.2, size=10)

output_file("dashboard/templates/iris.html", title="iris.py example")


import matplotlib.colors as mcolors
import numpy as np
from numpy.random import multivariate_normal

data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[2, 3], [1, 3]], size=1000)
])

gammas = [0.8, 0.5, 0.3]

fig, axes = plt.subplots(nrows=2, ncols=2)

axes[0, 0].set_title('Linear normalization')
axes[0, 0].hist2d(data[:, 0], data[:, 1], bins=100)

for ax, gamma in zip(axes.flat[1:], gammas):
    ax.set_title(r'Power law $(\gamma=%1.1f)$' % gamma)
    ax.hist2d(data[:, 0], data[:, 1],
              bins=100, norm=mcolors.PowerNorm(gamma))

fig.tight_layout()

plt.show()