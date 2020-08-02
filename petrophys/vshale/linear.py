def linear(df, gamma_ray_col):
  gr = df[gamma_ray_col]
  max_gr = gr.max()
  min_gr = gr.min()
  
  return (gr - min_gr) / (max_gr - min_gr)
