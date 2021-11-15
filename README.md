# COMSW4156_JICC
COMS W4156 Team Project: JICC
# API
# Development
## Build
### Python Setup
```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```
### PostgreSQL Setup
We assume there is a PostgreSQL instance running on port 5432. If one is not started, follow this [guide](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
## Run 
To start the Flask server, run
```
python3 Src/server.py 
```
# API endpoints
1. get dining hall menu items
- this API receives a dining hall ID and returns a list of menu items for that dining hall
```python
@app.route('/getDiningMenu/<diningHall>')
```

## Test
