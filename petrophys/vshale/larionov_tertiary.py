from .linear import linear

def larionov_tertiary(df, gamma_ray_col):
  gr_index = linear(df, gamma_ray_col)
  
  return 0.083 * (2**(3.7 * gr_index) - 1)
