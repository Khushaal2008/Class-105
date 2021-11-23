import csv

with open('class1.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
n = len(file_data)
total = 0
for x in file_data:
    total += float(x[1])

mean = total / n
print("Mean / Average is: " + str(mean))

import pandas as pd
import plotly.express as px

df = pd.read_csv("class1.csv")

fig = px.scatter(df,    x="Student Number",
                        y="Marks"
            )
fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= mean, y1= mean,
      x0= 0, x1= n
    )
])

fig.update_yaxes(rangemode="tozero")

fig.show()