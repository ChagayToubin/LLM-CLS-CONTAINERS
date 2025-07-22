# from encodings.punycode import insertion_sort
from fastapi import FastAPI, Request

app = FastAPI()


import pandas as pd
import json


@app.post("/process")
async def process_data(request: Request):
    body = await request.json()  # קבלת ה-JSON


    dfm = pd.DataFrame(body["dfm"]) if isinstance(body.get("dfm"), (dict, list)) else None


    question = body["question"]


    dic = body.get("dic", {})

    if not isinstance(dic, dict):
        raise ValueError("Expected 'dic' to be a dictionary")


    list_condition = body.get("list_condition", [])
    if isinstance(list_condition, str):

        list_condition = [item.strip() for item in list_condition.split(",")]
    elif not isinstance(list_condition, list):
        raise ValueError("Expected 'list_condition' to be a list or a comma-separated string")




    dic_count_main_value=get_main_key_dic_count(dfm,question)
    sum_value_calculation = {}
    for key in dic_count_main_value.keys():
        sum_value_calculation[key] = 1
    div_by = 0
    count = 0
    for key_no_yes, value in dic.items():
        for t in value.values():
            for k, v in t.items():
                if k == list_condition[count]:
                    # להסוי תנאי פשוט שאם זה לא שווה כמו לירך כנראה שהסויפו 1 ואז לחלק בעוד אחד מתחת
                    if sum(t.values()) == dic_count_main_value[key_no_yes]:
                        div_by = sum(t.values())
                    else:
                        div_by = dic_count_main_value[key_no_yes] + 1
                    sum_value_calculation[key_no_yes] *= (v/ div_by)

            count += 1
        count = 0
    return max(sum_value_calculation, key=sum_value_calculation.get)

def get_main_key_dic_count(df, question):
    values = df[question].unique()
    dic_count_main_question = {}
    for i in values:
        dic_count_main_question[i] = df[df[question] == i].shape[0]
    return (dic_count_main_question)





