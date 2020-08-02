from .clavier import clavier
from .larionov_older import larionov_older
from .larionov_tertiary import larionov_tertiary
from .linear import linear
from .steiber import steiber

method_function_map = {
  'clavier': clavier,
  'linear': linear,
  'larionov_older': larionov_older,
  'larionov_tertiary': larionov_tertiary,
  'steiber': steiber,
}

def calc_vshale(df, method='linear', gamma_ray_col='GR'):
  if method not in method_function_map:
    raise KeyError(f'Method {method} does not exist')

  return method_function_map[method](df, gamma_ray_col)

