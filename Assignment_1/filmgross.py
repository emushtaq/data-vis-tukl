from datetime import datetime
from bokeh.plotting import figure, output_file, show
from bokeh.models import NumeralTickFormatter

# prepare some data
x = [
datetime(11,6,3),
datetime(11,6,10),
datetime(11,6,17),
datetime(11,6,24),
datetime(11,7,1),
datetime(11,7,8),
datetime(11,7,15),
datetime(11,7,22),
datetime(11,7,29),
datetime(11,8,5),
datetime(11,8,12),
datetime(11,8,19),
datetime(11,8,26),
datetime(11,9,2),
datetime(11,9,9),
datetime(11,9,16),
datetime(11,9,23)
]

y = [73894349, 34530213, 17790366, 9496799, 4905010, 2203534, 1042047, 574015, 486450,
     577954 ,307397, 202011, 159843, 147932, 54941, 23943, 11501
]

# output to static HTML file
output_file("filmgross.html")

# create a new plot with a title and axis labels
p = figure( title="simple line example", plot_width=800, x_axis_label='x', y_axis_label='y', 
            x_axis_type="datetime")

# add a line renderer with legend and line thickness
p.line( x, y, legend="Weekly Gross", line_width=2 )

# use a formatter to display y-axis tick labels in million dollars
p.yaxis[0].formatter = NumeralTickFormatter(format="($ 0.00 a)")

# show the results
show(p)