from crypt import methods
import os

from flask import Flask, render_template, request
from dotenv import load_dotenv
from playhouse.shortcuts import model_to_dict
from peewee import *
import datetime
import regex as re

load_dotenv()
app = Flask(__name__)



if os.getenv("TESTING")=="true":
    print("Running in test mode")
    mydb= SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )
    


print(mydb)
class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb
mydb.connect()
mydb.create_tables([TimelinePost])

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), users=users)


@app.route('/ariaHobbies')
def ariaHobbies():
    return render_template('ariaHobbies.html', url=os.getenv("URL"), user=Aria)

@app.route('/api/timeline_post', methods=['POST'])
def post_time_linepost():

    name = request.form['name']
    email = request.form['email']
    content = request.form['content']

    regex = r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b'
    if not request.form['name']:
        return "Invalid name", 400
    elif not (re.fullmatch(regex, request.form['email'])):
        return "Invalid email", 400
    elif not request.form['content']:
        return "Invalid content", 400
    else:
        timeline_post = TimelinePost.create(name=name, email=email, content=content)
        return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return { 
        'timeline_posts': [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/timeline', methods=["POST", "GET"])
def timeline():
    return render_template('timeline.html', title="Timeline")


# This is the User class that defines everything that will be inputted into the portfolio template
class User:
    def __init__(self, name, pic, about, education, work, hobbies, places):
        self.name = name
        self.pic = pic
        self.about = about
        self.education = education
        self.work = work
        self.hobbies = hobbies
        self.places = places

# Education class is composed of school (school name), grad (graduation date), and major (area of study)
class Education:
    def __init__(self, school, grad, major):
        self.school = school
        self.grad = grad
        self.major = major

# Work class is composed of title (job title), company, and description
class Work:
    def __init__(self, title, company, description):
        self.title = title
        self.company = company
        self.description = description

# Hobbies class is composed of hobby (hobby name), description of the hobby, and img (source to the image)
class Hobbies:
    def __init__(self, hobby, img):
        self.hobby = hobby
        self.img = img

# Map class is compposed of the city and country of the location.
# More information may be needed and so more attributes may be added later on
class Places:
    def __init__(self, city, country):
        self.city = city
        self.country = country


# We've defined all the classes we'll use above, so from here on we'll make instances of the classes to break down a user's data
#
AriaName = "Arianna Richardson"
AriaPic = "./static/img/AriaPic.png"
AriaAbout = "Hello! My name is Arianna and I am from Bowie, MD! I enjoy coding and creating digital media. I have skills in both graphic design and video production. Nice to meet you!"
AriaEducation = Education("Rochester Institute of Technology", "Expected May 2024", "New Media Interactive Development")
AriaWork = []
AriaWork.append(Work("Equal Rights Amendment Coalition Social Media Internship", "", \
    ["Internship with the ERA Coalition where I create social media content spreading awareness on the Equal Rights Amendment."]))
AriaWork.append(Work("National Society of Black Engineers (NSBE) SEEK Program", "", \
    ["Taught engineering concepts to elementary school kids."]))
AriaWork.append(Work("Google Computer Science Summer Institute", "", \
    ["A virtual summer program teaching students JavaScript sponsored by Google for graduating seniors interested in a career in computer science."]))
AriaWork.append(Work("Communications Intern", "", \
    ["Assisted in the redesign of my high school website", \
    "Shot and edited photos and videos with Adobe software.", \
    "Created promotional content representing the high school for prospective families and school social media(i.e video production, photos, reported on school current events)."]))
AriaHobby = []
AriaHobby.append(Hobbies("Digital Art", "./static/img/DigitalArt.jpg"))
AriaHobby.append(Hobbies("Singing", "./static/img/Sing.jpg"))
AriaHobby.append(Hobbies("Baseball", "./static/img/Baseball.jpg"))

Aria = User(AriaName, AriaPic, AriaAbout, AriaEducation, AriaWork, AriaHobby, "places")


# List of users that will be included in this portfolio
users = [Aria]