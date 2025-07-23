


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
            if check.classified_by_input(instance,copy)==i[index_to_remov]:
                count_right+=1
        return ((count_right/ df_check.shape[0]) * 100, "%")


    @staticmethod
    def classified_by_input(instace,list_condition):
        # self.dfm, self.dic, self.question,
        dic_count_main_value = check.get_main_key_dic_count(instace.dfm, instace.question)
        sum_value_calculation = {}
        for key in dic_count_main_value.keys():
            sum_value_calculation[key] = 1
        div_by = 0
        count = 0
        x=0
        for key_no_yes, value in instace.dic.items():
            for t in value.values():
                for k, v in t.items():
                    if k == list_condition[count]:
                        # להסוי תנאי פשוט שאם זה לא שווה כמו לירך כנראה שהסויפו 1 ואז לחלק בעוד אחד מתחת
                        if sum(t.values()) == dic_count_main_value[key_no_yes]:
                            div_by = sum(t.values())
                        else:
                            div_by = dic_count_main_value[key_no_yes] + 1
                        sum_value_calculation[key_no_yes] *= (v / div_by)


                count += 1
            count = 0

        return max(sum_value_calculation, key=sum_value_calculation.get)

    @staticmethod
    def get_main_key_dic_count(df, question):

        values = df[question].unique()
        dic_count_main_question = {}
        for i in values:
            dic_count_main_question[i] = df[df[question] == i].shape[0]
        return (dic_count_main_question)


