
from LLM.Models.Clean import clean
from LLM.Models.Loader import  loader
from LLM.Models.Training_models import training_models
# from LLM.Models.Classified import classified
# from LLM.Models.check_precent import check
import json
class manger:
    def __init__(self):
        # df = loader.load_file("../files/mushroom.csv")
        df = loader.load_file("files/mushroom.csv")
        df=clean.clean_file(df)

        df_random = df.sample(frac=1, random_state=42)
        split_index = int(0.7 * len(df))

        self.dfm=df_random[:split_index]
        self.check_test = df_random[split_index:]

        return
    @staticmethod
    def chose_whate_to_do():
        print('------------------\n'
              'To ask a question to check whate the answer by statistics press 1\n'
              'Check how many percent is correct press 2 ')
        return input()

    @staticmethod
    def init_program(name):
        file=loader.load_file(name)
        # return  clean.clean_file(file)
        return file

    @staticmethod
    def enter_ask_enter_conditin(file,question):
        dic=training_models.training_model_question(file,question)
        return dic

    @staticmethod
    def get_question_check(df):
        return training_models.get_question(df)

    @staticmethod
    def enter_value(instance):
        # que, df
        exemple = ''
        list = []
        list_colmuns = [col for col in instance.dfm.columns if col != instance.question]
        for inp in list_colmuns:
            exemple = instance.dfm[inp].unique()
            print(f" please enter  {inp} \nexeple {exemple}")
            list.append(input())

        return list
    def control_all(self):

        self.choice = manger.chose_whate_to_do()
        self.question = manger.get_question_check(self.dfm)
        self.dic = manger.enter_ask_enter_conditin(self.dfm, self.question)
        print(self.question+"===")

        if   self.choice == '1':
            list_condition = manger.enter_value(self)


            # answer=classified.classified_by_input(self,list_condition)

            print(f"The highest probability is that  {self.question} it is {answer} ")

        elif self.choice=='2':
            # check.precent_right(self)
            print()
        else:
            print('unvalide inpute')