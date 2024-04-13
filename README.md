
![image](https://github.com/brd0m/Dagster/assets/113246520/12d533a4-d15d-4385-b76a-c30f236bb61d)


Create a virtual environment with
```
python -m venv .pyenv 
source .pyenv/bin/activate #activate venv for Mac/Linux
.pyenv\Scripts\activate #activate venv for Windows
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
