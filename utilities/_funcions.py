################################################################################
################################################################################
################################################################################

def mf_quick_analysis(df):
  """
  DataTypes, Rows and Columns ,Null values, Unique values ...
  """
  print(" >>> Data info:")
  print(df.info())
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
  
  rep = sv.DataframeReport(df)
  rep.show_notebook()
  return sv.analyze(df), df.columns.tolist()
################################################################################
################################################################################
################################################################################

def mf_get_files_from_git(_fileName, _fileLink):
  """
  *including extension
  with open({_fileName}, 'w') as f:
    f.write(requests.get({_fileLink}).text)
  """
  with open(f'{_fileName}', 'w') as f:
    f.write(requests.get(f'{_fileLink}').text)
  print(f'\n{_fileName} has been created!')

################################################################################
################################################################################
################################################################################

def mf_html_creation_display(df, display=0):
  """
  HTML creation
  """
  my_report = sv.analyze(df);
  my_report.show_html();
  
################################################################################

def mf_html_renaming(name):
  n_name = name + ".html"
  if n_name in os.listdir():
    os.remove(n_name);
  os.rename("SWEETVIZ_REPORT.html", n_name)
  
  

  
