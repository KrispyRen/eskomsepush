# EskomSePush

## Description
Python wrapper for the EskomSePush API to get the Eskom Loadshedding schedule for your area

## Disclaimer
I am a beginner programmer and this is my first code commit. If you have better ways of coding it or find bugs in my code, please feel free to fix :)

## Functions
- `get_status()` **get the National loadshedding schedule**
- `get_allowance()` **check your credits**
- `search_areas()` **search area using text search**
- `get_area_information` **get the area information based on the `area_id` (use `search_areas()` to get the `area_id`**
- `get_area_information_test` **for testing purposes. Does not count towards your credits**
- `get_areas_nearby` **search for areas nearby (longitude and latitude as input)**
- `get_topics_nearby` **find topics created by users nearby (longitude and latitude as input)**

## version 1.1 (work in progress)

- Add logging 

## Additional notes
- Remember to obtain your `API_KEY` by [regisering](https://eskomsepush.gumroad.com/l/api)
- Put your `API_KEY` in a .env file 
- Add `BASE_URL = "https://developer.sepush.co.za/business/2.0"` in the .env file
- Install all the dependencies from the requirements.txt file
- Create app.py (mine is ignored in the .gitignore file) to create an object of the class EskomSePush

## Resources 
EskomSePush API [documentation](https://documenter.getpostman.com/view/1296288/UzQuNk3E#intro)


