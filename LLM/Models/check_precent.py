

from LLM.Models.Classified import classified

class check:
    @staticmethod
    def precent_right(instance):

        df_check=instance.check_test

        count_right=0
        list_columns_check=df_check.values.tolist()

        index_to_remov = df_check.columns.get_loc(instance.question)

        for i in list_columns_check :
            copy = i.copy()
            copy.pop(index_to_remov)

            if classified.classified_by_input(instance,copy)==i[index_to_remov]:
                count_right+=1
        print((count_right/ df_check.shape[0]) * 100, "%")
