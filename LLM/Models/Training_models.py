import json
class training_models:

    @staticmethod
    def training_model_question(df,question):

        dic = {}
        value_unic = df[question].unique()
        columns_df = [col for col in df.columns if col != question]

        for uniqe in value_unic:
            dic[uniqe] = {}
            # מילוי של כל דבר במפתחות של העמודות שיש לו בטבלה חוץ ממנו כמובן
            for columns in columns_df:
                dic[uniqe][columns] = {}

                uniqe_value_in_columns = df[columns].unique()
                for v in uniqe_value_in_columns:
                    dic[uniqe][columns][v] = 0
                # עשכיו אני ייצר דאטה ביס חדש לפי התנאי שאני רוצה
                condition_df = df[df[question] == uniqe]
                for value_in_columns in condition_df[columns]:
                    dic[uniqe][columns][value_in_columns] += 1

                #     אם יש 0 אז למלאות את כולם עוד 1
                if 0 in dic[uniqe][columns].values():
                    dic[uniqe][columns] = {k: v + 1 for k, v in dic[uniqe][columns].items()}

        # print(json.dumps(dic, indent=4))

        return dic
    @staticmethod
    def get_question(df):
        for clo in df.columns:
            print(clo,end=" ")
        print('\n')
        print('chose one to ask ')
        chose=input()
        if chose in df.columns:

            return chose
        else:
            print('no validetion please enter again')
            training_models.get_question(df)




