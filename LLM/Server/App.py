from fastapi import FastAPI,  Request
from fastapi.responses import HTMLResponse
from LLM.Models.Manger import manger
import requests

app = FastAPI()

my_manager = manger()

@app.get("/", response_class=HTMLResponse)
def choose_target():

    columns = list(my_manager.dfm.columns)
    html = "<h2>chosh somthing to ask?</h2><form method='post' action='/choose'>"
    html += "<select name='target_column'>"
    for col in columns:
        html += f"<option value='{col}'>{col}</option>"
    html += "</select><input type='submit' value='Next'/></form>"

    return f"<html><body>{html}</body></html>"

@app.post("/choose", response_class=HTMLResponse)
async def ask_values(request: Request):
    form = await request.form()
    target_column = form["target_column"]

    my_manager.question = target_column
    my_manager.dic = manger.enter_ask_enter_conditin(my_manager.dfm, target_column)

    # עמודות (חוץ מהשאלה)
    input_columns = [col for col in my_manager.dfm.columns if col != target_column]

    html = f"<h2>Enter values  (Target: {target_column})</h2>"
    html += "<form method='post' action='/submit'>"
    html += f"<input type='hidden' name='target_column' value='{target_column}' />"

    for col in input_columns:
        examples = list(my_manager.dfm[col].unique())
        html += f"<label>{col} (examples: {examples}):</label><br>"
        html += f"<input type='text' name='{col}' /><br><br>"

    html += "<input type='submit' value='Submit' /></form>"
    return f"<html><body>{html}</body></html>"

@app.post("/submit", response_class=HTMLResponse)
async def show_result(request: Request):
    form = await request.form()
    target_column = form["target_column"]
    # מקבל את הערכים של המשתמש לפי השדות בטופס
    user_input = [form[key] for key in form.keys() if key != "target_column"]
    # שלח את זה לפונקציית הסיווג שלך
    try:
        manager_json = {
            "dfm": my_manager.dfm.to_dict(),
            "question": my_manager.question,
            "dic": my_manager.dic,
            "list_condition":user_input
        }

        url = "http://127.0.0.1:8001/process"

        response = requests.post(url, json=manager_json)
        print(response)

        print(response.text[1:-1])
        print(type(response.text))

        # result = classified.classified_by_input(my_manager, user_input)
        result=response.text[1:-1]

    except Exception as e:
        return f"<p> Error while classifying: {str(e)}</p><a href='/'>Back</a>"
    return f"""
    <html>
        <body>
            <h2> Prediction for <u>{target_column}</u></h2>
            <p><b>Your input values:</b> {user_input}</p>
            <p><b>Prediction result:</b> <span style='color: green;'>"!" +{result }+"!"</span></p>
            <a href="/"> Try Again</a>
        </body>
    </html>
    """