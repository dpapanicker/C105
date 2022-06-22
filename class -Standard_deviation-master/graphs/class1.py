import csv

with open('class1.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove headers from CSV
file_data.pop(0)

total_marks = 0
total_entries = len(file_data)

for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks / total_entries
print("Mean (Average) is -> "+str(mean))

import pandas as pd
import plotly.express as px

df = pd.read_csv("class1.csv")

fig = px.scatter(df,    x="Student Number",
                        y="Marks"
            )
# In this code, we are saying that we want to update our figure, 
# which is a scatter plot, and we want to add a shape to it.

# For the shapes, we have to define the attributes of that shape.

# Here, we are saying that we want the shape to be of type=”line”

# since we have marks in the Y Axis,  we say that the average 
# also lies in the Y Axis
fig.update_layout(shapes=[
    dict(
      type= 'line',   
      y0= mean, y1= mean,
      x0= 0, x1= total_entries
    )
])
# the X0 is the point from where the line will start in the
#  X Coordinate, and X1 is the point where the line will end in the
# X Coordinate. We set the X0 as 0 and X1 as the total  
# number of entries.
# Y0 is the point from where the line is starting in the Y axis, 
# and Y1 is the point where the line will end. Since our mean lies
#  in the Y axis, we will keep the Y0 and Y1 the same.


fig.update_yaxes(rangemode="tozero")

fig.show()

# After doing the same thing for class 2, if we look closely, we can 
# see that this second graph’s Y Axis does not start with 0, since 
# there are no values below 60.

# To make both the graphs consistent with each other, 
# we  add the line fig.update_yaxes(rangemode="tozero") 
# before fig.show() . This line will update the figure’s Y Axis,
# and we are asking the code to start the range of the Y Axis to 0.
