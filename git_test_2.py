def auto_classification(df = None):
    if df != None:
        try:
            df.info()
        except:
            print('Error')
    return df