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

