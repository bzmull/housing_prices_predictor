
def cat_var_to_num(df):
    '''
    Function to convert columns containing categorical data to numerical data in a dataframe
    input: dataframe
    output: dataframe
    '''
    new_df = df.copy()
    #selects columns which don't have numerical data
    string_df = new_df.select_dtypes(exclude=np.number)
    #iterating through each column in df containing categorical data
    for col in string_df.columns:
        # replace NaN with string "NA"
        new_df[col].fillna('NA',inplace = True)
        # identify unique categories used in specific column
        unique_vals = new_df[col].unique()
        for idx,unique_val in enumerate(unique_vals):
            # replace categorical values in column with numerical values 
            new_df[col].loc[new_df[col]==unique_val] = idx
    return new_df