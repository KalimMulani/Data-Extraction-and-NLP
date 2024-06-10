import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import requests
import urllib
import re
import os

class data_extraction:

    def primary(self):
        try:
            data = pd.read_csv(os.path.join("Providedfiles\\Input.xlsx - Sheet1.csv"))
            return data
        except Exception as e:
            print("Error", e)

    def secondary(self):
        data = pd.read_csv("Providedfiles\\Input.xlsx - Sheet1.csv")
        df = data.copy()
        updated_list = []
        no_match_data = []
        blank_links = {}
            
        for i, row in df.iterrows():
            url = row['URL']
            try:
                response = requests.get(url)
                response.raise_for_status()
                soup = bs(response.text, "html.parser")
                article_title = soup.find("title").text
                all_text = soup.find("div", class_="td-post-content tagdiv-type")
                
                if all_text is not None:
                    all_text = all_text.get_text(strip=True, separator="\n")
                    first_data = all_text.splitlines()
                else:
                    print(f"No matching element found in HTML of URL: {url}")
                    first_data = []
                    blank_links[f"blackassign00{i+1}"] = url

                    Blank = {
                        'URL_ID': df["URL_ID"][i],
                        "URL": url,
                    }
                    no_match_data.append(Blank)
            except requests.RequestException as e:
                print(f"Error fetching {url}: {e}")
                first_data = []
                blank_links[f"blackassign00{i+1}"] = url

                Blank = {
                    'URL_ID': df["URL_ID"][i],
                    "URL": url,
                }
                no_match_data.append(Blank)
            
            new_df = {
                'URL_ID': df["URL_ID"][i],
                'URL': url,
                'Article_data': f"{article_title}-{first_data}"
            }
            
            updated_list.append(new_df)
            
            filename = urllib.parse.quote_plus(str(df["URL_ID"][i]))
            file_path = "C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\Extracted_Data"
            os.makedirs(file_path, exist_ok=True)

            with open(f"{file_path}\\{filename}.txt", "w+", encoding="utf-8") as file1:
                file1.write(article_title + "\n")
                file1.write("\n".join(first_data) if first_data else "No data found.")

        return pd.DataFrame(updated_list), no_match_data

            
    def handle_blank_link(self,blank_data):
        updated_list = []
        for item in blank_data:
            i = item["URL_ID"]
            j = item["URL"]
            response = requests.get(j)
            soup = bs(response.text,"html.parser")
            article_title = soup.find("title").text
            all_div =soup.find("td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type")
            
            if all_div is not None:
                first_data = all_div.get_text(strip=True,separator="\n")
                updated_dict = {
                    'URL_ID': i,
                    'URL': j,
                    'Article_data': f"{article_title}-{first_data}"
                }
                    
                updated_list.append(updated_dict)
                
                filename = urllib.parse.quote_plus(i)
                file_path ="C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\Extracted_Data"
                space=" "
                with open(f"{file_path}\{filename}.txt","w+",encoding="utf-8") as file1:
                    file1.writelines(article_title)
                    file1.writelines(space)
                    file1.writelines(first_data)
                    
                
            else:
                print(f"No data available from url {j}")
        df = pd.DataFrame(updated_list)
        return df    
        
    def merged(self,df1,df2):
        try:
            merged_df = pd.merge(df1,df2,on=['URL_ID','URL'],how="left")
            merged_df = merged_df.dropna()
            merged_df.reset_index(drop=True,inplace=True)
        except KeyError:
            final_df = pd.DataFrame(df1)
            final_df.to_csv("C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\CSVfiles\\Final.csv",index=False)
        return final_df
    
# if __name__ == "__main__":
#     obj  = data_extraction()
#     obj1 = obj.primary()
#     df,remain_data = obj.secondary()
#     update_df = obj.handle_blank_link(remain_data)
#     final = obj.merged(df,update_df)
   
    
    