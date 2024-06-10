from Pyfiles.data_extraction import data_extraction
from Pyfiles.analysis import Analysis
import nltk
import pandas as pd

class Output:
    
     def output_primary(self,data):
        updated_list = []
         
        for k,j,col in zip(data['URL_ID'],data["URL"],data["Article_data"]):
             
            processed_word = Analysis().text_corpus(col)
            postive_dict,negative_dict = Analysis().master_dict_data()
            
            # Positive Score
            pos_count = []
            for i in processed_word:
                if i  in postive_dict:
                    pos_count.append(i)
            pos_score=len(pos_count)
            
            # Negative Score
            neg_count = []
            for i in processed_word:
                if i  in negative_dict:
                    neg_count.append(i)
            neg_score=len(neg_count)
            
            # Polarity Score
            
            polarity_score = ((pos_score - neg_score)/((pos_score + neg_score) + 0.000001))
            
            # Subjective_Score
            
            subjectivity_score = ((pos_score + neg_score)/ ((len(processed_word)) + 0.000001))
            
            # Average Sentence length
            
            total_sen=len(nltk.tokenize.sent_tokenize(col))
            avg_sen_len = round(len(processed_word)/ total_sen,0)
            
            # Percentage of complex word and complex word count
            
            per_of_complex_word,complex_word_count = Analysis().complexity_per(processed_word)
            
            # Fog Index
            
            fog_index = 0.4 * (avg_sen_len + per_of_complex_word)
            
            # Average Number of words per sentence 
            
            avg_no_words_per_sen = round(len(col)/total_sen,0)
            
            # Word count 
            
            word_count = len(processed_word)
            
            # Syllable per word
            
            syllable_per_word = Analysis().count_syllable_per_word(processed_word)
            
            # Average Word length 
            
            word_len = Analysis().avg_word_len(processed_word)
            avg_word_len  = round(word_len/len(processed_word),0)
            
            final_dict = {
                "URL_ID" : k,
                "URL"    : j,
                "Article_data": col,
                "Positive_Score" : pos_score,
                "Negative_Score" : neg_score,
                "Polarity Score" : polarity_score,
                "Subjective_Score": subjectivity_score,
                "AVG_Sentence_length": avg_sen_len,     
                "Percentage_Of_Complex_Word": per_of_complex_word,
                "Fog_Index": fog_index,
                "AVG_No_Of_Words_Per_Sentence" : avg_no_words_per_sen,
                "Complex_Word_Count": complex_word_count,
                "Word_Count": word_count,
                "Syllable_Per_Word": syllable_per_word,
                "Average_Word_Length" : avg_word_len
            }
            
            updated_list.append(final_dict)
        
        df= pd.DataFrame(updated_list)
        df.to_csv("C:\\Users\\Kalim\\OneDrive\\Desktop\\Assesment\\CSVfiles\\Output.csv")
        return df