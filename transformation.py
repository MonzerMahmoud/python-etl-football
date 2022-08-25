import pandas as pd
import extraction
import loading

class Transformation:

    def __init__(self):
        print("Transformation")
        self.extractionObj = extraction.Extraction()
        
        self.data = self.extractionObj.get_Matches()
        
        if self.check_if_match_valid(self.data):
            print("Transformation successful")
            loading.Loading(self.data)
        else:
            print("Transformation failed")




    def check_if_match_valid(self, df: pd.DataFrame) -> bool:
        print("Checking if match is valid")
        if df.empty:
            print("No matches found")
            return False

        df.drop_duplicates(subset=['matchId'], keep='first', inplace=True)
        df.dropna(inplace=True)
        
        df['date'] = pd.to_datetime(df['date'])

        if pd.Series(df['matchId']).is_unique:
            print("All matches have unique IDs")
            pass
        else:
            print("Not all matches have unique IDs")
            return Exception("Duplicate matchIds found")

        print("Matches valid")
        
        return True


    
    
   