import lasio

def load_las(path='tests/utils/south-barrow-18.las'):
  las = lasio.read(path)
  return las.df()
