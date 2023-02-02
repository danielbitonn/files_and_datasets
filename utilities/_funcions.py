################################################################################
################################################################################
################################################################################

def mf_quick_analysis(df, sweetviz=False):
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
  print(df.describe())
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
  if sweetviz:
    rep = sv.DataframeReport(df)
    rep.show_notebook()
    rep.show_html()
    return rep
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

class pre_process:
  def __init__(self):
    self.feat_clf = {
        'numeric': {    
        # 'dataTypes':[np.int64, np.float64],
                        'continuous'  :[],     # Floats
                        'binary'      :[],     # 0/1
                        'nominal'     :[]      # Integers
        },
        'qualitative': {
        # 'dataTypes':[object, str],
                        'categorial'  :[],     # Groups,
                        'ordinal'     :[],     # Rank, 
                        'boolean'     :[],     # Positive/Negative, True/False
                        'nominal'     :[]      # IDs,
        },
        'timeSeries': { 
        # 'dataTypes':[np.datetime64],
                        'datetime'    :[],    
                        'timedelta'   :[], 
                        'objecttime'  :[]
        },
        'other':      {
                        'other'       :[],
                        'garbage'     :[],
                        'target'      :[]
        }
    }
    
    self.feat_clas = [clas for clas, item in self.feat_clf.items()]
    self.feat_sub_clas = [[clas,typ] for clas in self.feat_clas for typ, cont in self.feat_clf[clas].items()]

    for clas, item in self.feat_clf.items():
      print(clas,':')  
      for typ, content in item.items():
        print(typ, ' >>> ' ,content)
      print()


  def _update_feat_clf(self, col_name):
    """
    class: 'numeric', 'qualitative', 'timeSeries', 'other' 
    """
    # Init
    self.col_name = col_name;
    # Functions
    self._user_input()
    self._append_column()


  def _user_input(self):
    print(f'Choose the dataType of the column\n{self.col_name}\
            \nChoose a Number from the following:\n')
    for i, x in enumerate(self.feat_sub_clas):
      print(i, x)
    
    try:
      self.input = input('\n\n >>> Press Q/q to stop.\n')
    except KeyboardInterrupt:
      self.input = self.feat_sub_clas.index(["other", "other"])

  
  def _append_column(self):
    """
    #No >>> ['class', 'sub_class']
    """
    self.feat_clf[self.feat_sub_clas[int(self.input)][0]][self.feat_sub_clas[int(self.input)][1]].append(self.col_name)

################################################################################
################################################################################
################################################################################
