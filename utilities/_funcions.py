def mf_df_columns(df): # == df.info()
  for index, val in enumerate(df.columns.values.tolist()):
    print(index, val)
  return

################################################################################
################################################################################
################################################################################

def mf_quick_analysis(df):
  """
  DataTypes, Rows and Columns ,Null values, Unique values ...
  """
  print(" >>> Data info:")
  print(df.info())
  # print("-------------****----------------\n\nData Types:")
  # print(df.dtypes)
  # print("-------------****----------------\n\nColumn names:")
  # print(df.columns)
  print("\n-------------****----------------\n\n >>> Null Values:")
  print(df.isnull().sum())
  print("\n-------------****----------------\n\n >>> Precentage of Nulls Values:")
  print(df.apply(lambda x: (sum(x.isnull()) / len(df)) * 100))
  print("\n-------------****----------------\n\n >>> Unique values:")
  print(df.nunique())
  print("\n-------------****----------------\n\n >>> Describes:")
  print(df.describe().T)
  print("\n-------------****----------------\n\n >>> Rows and Columns:")
  print(df.shape)
  print("\n-------------****----------------\n\n >>> The most often appears (.mode()) in the categorical columns, and the average (.mean()) for the continuous")
  for column in df.columns:
    if df[column].dtype == 'int64' or df[column].dtype == 'float64':
      avg = df[column].mean()
      print(f'{column} :  {avg}')
    elif df[column].dtype == 'O':
      mode = df[column].mode()[0] 
      print(f'{column} :  {mode}')
      
################################################################################
################################################################################
################################################################################

def mf_html_creation_display(df, name, display=0):
  """
  HTML creation
  """
  my_report = sv.analyze(df);
  n_name = name + ".html"
  my_report.show_html();
  if n_name in os.listdir():
    os.remove(n_name);

  os.rename("SWEETVIZ_REPORT.html", n_name)
  if display==1:
    print(n_name)
    return IPython.display.HTML(filename = n_name)
  return
