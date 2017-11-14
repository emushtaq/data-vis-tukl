from datetime import datetime
from bokeh.plotting import figure, output_file, show
from bokeh.models import NumeralTickFormatter

# prepare some data
x = [
datetime(10,8,13),
datetime(10,8,20),
datetime(10,8,27),
datetime(10,9,3),
datetime(10,9,10),
datetime(10,9,17),
datetime(10,9,24),
datetime(10,10,1),
datetime(10,10,8),
datetime(10,10,15)
]

y = [48389085, 24123161, 13055524, 9674843, 4404622, 1858731, 779092, 325543, 180594, 277329]

rank = [1,1,3,6,6,13,15,22,32,31]

# output to static HTML file
output_file("filmgross.html")

# create a new plot with a title and axis labels
p = figure( title="The Expendables - Gross earning line example.", plot_width=800, x_axis_label='Time in days', y_axis_label='Gross in Million $', 
            x_axis_type="datetime")

# add a line renderer with legend and line thickness
p.line( x, y, legend="Weekly Gross", line_width=2 )

# use a formatter to display y-axis tick labels in million dollars
p.yaxis[0].formatter = NumeralTickFormatter(format="($ 0.00 a)")

# show the results
show(p)