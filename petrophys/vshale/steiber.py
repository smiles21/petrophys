from .linear import linear

def steiber(df, gamma_ray_col):
  gr_index = linear(df, gamma_ray_col)

  return gr_index / (3 - 2 * gr_index)
