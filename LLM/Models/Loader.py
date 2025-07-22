# import pandas as pd
# class loader:
#     @staticmethod
#     def load_file(name):
#         return pd.read_csv(name)
import pandas as pd
import os


class loader:
    @staticmethod
    def load_file(name):
        # מוצא את הנתיב האבסולוטי של הקובץ ביחס לפרויקט
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(base_dir, name)

        return pd.read_csv(full_path)
