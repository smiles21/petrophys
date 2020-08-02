from .linear import linear

def larionov_older(df, gamma_ray_col):
  gr_index = linear(df, gamma_ray_col)
  
  return 0.33 * (2**(2 * gr_index) - 1)
