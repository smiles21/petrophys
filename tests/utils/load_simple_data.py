import pandas as pd

def load_simple_data():
  return pd.DataFrame(
    data={
      'GR': [60, 70, 80]
    },
    index=pd.Index(data=[400, 400.5, 401], name="MD")
  )
