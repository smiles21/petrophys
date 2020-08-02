from .linear import linear

def clavier(df, gamma_ray_col):
  gr_index = linear(df, gamma_ray_col)

  return 1.7 - ((3.38 - (gr_index + 0.7) ** 2)) ** 0.5
