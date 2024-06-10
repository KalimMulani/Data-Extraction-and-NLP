from Pyfiles.data_extraction import data_extraction
from Pyfiles.utility import Output
import pandas as pd
if __name__ == "__main__":
    obj  = data_extraction()
    out  = Output()
    obj1 = obj.primary()
    df,remain_data = obj.secondary()
    update_df = obj.handle_blank_link(remain_data)
    final = obj.merged(df,update_df)
    df7= pd.read_csv("C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\CSVfiles\\Final.csv")
    df3 = out.output_primary(df7)
   