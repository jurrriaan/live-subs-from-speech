import plotly
import pandas as pd
import numpy as np
import cufflinks as cf

from plotly.graph_objs import *
from datetime import datetime, timedelta
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

cf.go_offline()

# import plotly_express as px
plotly.offline.init_notebook_mode()


glew_colors = ['#2196F3', '#7168F2', '#00B8CC', '#55E0AA', '#FFB300', '#FF525E', '#8EA2AC', 'rgb(255, 152, 150)', 'rgb(148, 103, 189)', 'rgb(197, 176, 213)', 'rgb(140, 86, 75)', 'rgb(196, 156, 148)', 'rgb(227, 119, 194)', 'rgb(250, 175, 250)', 'rgb(255, 238, 0)', 'rgb(252, 163, 45)', 'rgb(15, 22, 219)', 'rgb(15, 219, 196)']

#  def joke():
    #  return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
            #  u'Beiherhund das Oder die Flipperwaldt gersput.')

def plotly_heatmap(z, x, y, layout):
  if layout is None:
    layout = Layout()

  # redata = json.loads(json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder))
  # relayout = json.loads(json.dumps(layout, cls=plotly.utils.PlotlyJSONEncoder))
  trace = Heatmap(
    z=z,
    x=x,
    y=y,
    colorscale='Jet'
  )

  fig = Figure(data=[trace], layout=layout)
  iplot(fig)
