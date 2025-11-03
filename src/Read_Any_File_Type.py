
import pandas as pd
import os

class reading_data:

    def __init__(self,filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File does not exist: {filepath}")
        self.filepath = filepath
        self.data = None

    def read_data(self):

        try:
            ext = self.filepath.lower()

            if ext.endswith(".csv"):
                self.data = pd.read_csv(self.filepath)

            elif ext.endswith((".xls", ".xlsx")):
                self.data = pd.read_excel(self.filepath)

            elif ext.endswith(".json"):
                self.data = pd.read_json(self.filepath)

            elif ext.endswith(".xml"):
                self.data = pd.read_xml(self.filepath)

            elif ext.endswith(".txt"):
                self.data = pd.read_csv(self.filepath, sep="\t", engine="python")

            elif ext.endswith(".ods"):  # OpenDocument Spreadsheet
                self.data = pd.read_excel(self.filepath, engine="odf")

            elif ext.endswith(".html") or ext.endswith(".htm"):
                self.data = pd.read_html(self.filepath)[0]

            elif ext.endswith(".parquet"):
                self.data = pd.read_parquet(self.filepath)

            elif ext.endswith(".feather"):
                self.data = pd.read_feather(self.filepath)

            else:
                print("Unsupported file type")
                return None

            print(f"[SUCCESS] File loaded successfully: {type(self.data)}")
            return self.data

        except Exception as e:
            print(f"Error reading file: {e}")
            return None