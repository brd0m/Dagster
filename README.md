Create a virtual environment with
```
python -m venv .pyenv 
source .pyenv/bin/activate
.pyenv\Scripts\activate
```
To install Dagster
```     
pip install dagster dagster-webserver 
```
Run Dagster with

```
dagster dev -f dagster_test.py
```
To view outputs of SDAs:

```
Run Python
import Pickle
f = open('rellocationoffile','rb') #read file as binary
data = pickle.load(f)
data
```
