from sklearn.preprocessing import MinMaxScaler

def standardize_data(df):
    scaler = MinMaxScaler()
    df['value'] = scaler.fit_transform(df[['value']])
    df['industry_name_ANZSIC'] = df['industry_name_ANZSIC'].str.upper()
    return df
