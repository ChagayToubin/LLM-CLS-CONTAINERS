# Classification System with FastAPI


---

 Project Structure

- **`App.py` – Main FastAPI web application.  
  Provides HTML forms to select a target column, input feature values, and display predictions.

- **`CLS.py – Secondary FastAPI service.  
  Receives JSON data from `App.py`, processes it using the trained dictionary (`dic`), and returns predictions.

- **`Manger.py – Core manager class (`manger`).  
  Handles data loading, cleaning, splitting into train/test sets, model creation, and validation.

- **`BLD.py – Model-building logic.  
  Builds a nested dictionary of value counts for each feature and target class.

- **`CLN.py – Data cleaning logic.  
  Removes unnecessary columns like `id`.

- **`DAT.py – Data loading.  
  Loads CSV files using pandas.

- **`VLD.py – Validation and classification.  
  Contains logic for accuracy testing and prediction calculation.

---


---


