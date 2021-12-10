# COMSW4156_JICC
COMS W4156 Team Project: JICC
# API
1. get dining hall menu items
- this API receives a dining hall ID and returns a list of menu items for that dining hall
```python
@app.route('/getDiningMenu/<hallID>')
```
2. get dining halls
- this API returns information about each dining hall in the database
```python
@app.route('/getDiningHalls')
```
3. get food item information
- this API returns information about all the food items in the database
```python
@app.route('/getFoodItems')
```
4. get food reviews
- this API receives a food item ID and returns a list of reviews for that item.
```python
@app.route("/getFoodReviews/<foodId>")
```
5. get dining hall swipes
- this API receives a dining hall ID and returns a list of timestamps indicating when a person has reviewed that dining hall.
```python
@app.route("/getDiningHallSwipes/<diningHall>")
```


# Development
## Build
### Python Setup
```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```
### PostgreSQL Setup
We assume there is a PostgreSQL instance running on port 5432 in the GCP cluster. If one is not started, follow this [guide](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
## Run 
To start the Flask server, run
```
python3 Src/server.py 
```
## Test
In the source directory:
This should take about 2 minutes.
```
python3 -m unittest
```

# Continuous Integration
Our CI reports are located in Github Actions: https://github.com/tinedkim/COMSW4156_JICC/actions/workflows/python-app.yml

The CI reports include coverage reports, style checker reports, and bug finder reports.
