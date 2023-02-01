def func_df_columns(df): ### == df.info()
  for index, val in enumerate(df.columns.values.tolist()):
    print(index, val)
  return
