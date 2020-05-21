import blog_script, contests_script, user_script, submissions_script
import requests, json
from bs4 import BeautifulSoup

username = input(">")
user_script.extract_data(username)
blog_script.extract_data(username)
submissions_script.extract_data(username)
contests_script.extract_data(username)