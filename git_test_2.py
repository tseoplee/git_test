def auto_classification(df = None):
    if df != None:
        try:
            df.info()
        except:
            print('Error_1')
    return df

def plus(a, b):
  return a+b