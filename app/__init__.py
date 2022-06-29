import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime
from playhouse.shortcuts import model_to_dict
import re
load_dotenv()
app = Flask(__name__)


if os. getenv ( "TESTING" ) == "true":
	print ("Running in test mode")
	mydb= SqliteDatabase( 'file: memory?mode=memory&cache=shared', uri=True)
else:
	mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
		user=os.getenv("MYSQL_USER"),
		password=os.getenv("MYSQL_PASSWORD"),
		host=os.getenv("MYSQL_HOST"),
		port=3306)

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
    return render_template('index.html', title="Personal Portfolio", url=os.getenv("URL"), user=you)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Personal Portfolio", url=os.getenv("URL"), user=you)

@app.route('/timeline', methods=["POST", "GET"])
def timeline():
    return render_template('timeline.html', title="Timeline")

@app.route('/api/timeline_post', methods=[ 'POST' ])
def post_time_linepost():
    regex = r'\b[A-Za-z0-9.%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b'
    if not request.form['name']:
        return "Invalid name", 400
    elif not (re.fullmatch(regex, request.form['email'])):
        return "Invalid email", 400
    elif not request.form['content']:
        return "Invalid content", 400
    else:
        name = request.form['name']
        email = request.form['email']
        content = request.form['content']
        timeline_post = TimelinePost.create(name=name, email=email, content=content)
        return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts' : [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route("/api/timeline_post/<int:id>", methods=['DELETE'])
def delete_time_line_post(id):
    qry=TimelinePost.delete().where (TimelinePost.id==id)
    qry.execute()
    sid = str(id)
    return ("successfully deleted post #" + sid + "\n")

# This is the User class that defines everything that will be inputted into the portfolio template
class User:
    def __init__(self, name, pic, education, work, hobbies, places):
        self.name = name
        self.pic = pic
        self.education = education
        self.work = work
        self.hobbies = hobbies
        self.places = places

# Education class is composed of school (school name), grad (graduation date), major (area of study), and year (ex. freshman)
class Education:
    def __init__(self, school, grad, major, year):
        self.school = school
        self.grad = grad
        self.major = major
        self.year = year

# Experience class is composed of an image of work example, title (job title), company, and description
class Experience:
    def __init__(self, img, title, company, description):
        self.img = img
        self.title = title
        self.company = company
        self.description = description

# Hobby class is composed of title (hobby name), description of the hobby, and an image
class Hobby:
    def __init__(self, title, description, img):
        self.title = title
        self.description = description
        self.img = img

# Map class is compposed of the city and country of the location.
# More information may be needed and so more attributes may be added later on
class Places:
    def __init__(self, city, country):
        self.city = city
        self.country = country


# We've defined all the classes we'll use above, so from here on we'll make instances of the classes to break down a user's data into these classes
# This way, we can input it into the Jinja template for it to be formatted!

yourName = "Hailey Moon"

yourPic = "../static/img/Headshot.png"

yourEd = Education("Boston University", "Expected May 2024", "Computer Science", "Junior")

yourWork = []
yourWork.append(Experience(
    "../static/img/Cashmate.png",
    "UI/UX Designer",
    "Cashmate",
    "Designed a social budgeting app for the young adults of the modern era that utilizes external motivators to encourage healthy financial habits."
    )
)
yourWork.append(Experience(
    "../static/img/BostonHacks.png",
    "Design Head",
    "BostonHacks",
    "Led a team of 8 to design website wireframes, social media graphics, and brand merchandise for 3 hybrid hackathons for 100+ students."
    )
)
yourWork.append(Experience(
    "../static/img/Spark.png",
    "Graphic Design Intern",
    "BU Spark!",
    "Developed creative concepts for merchandise design and marketing graphics that align with BU Spark!, a technology incubator and experimental learning at Boston University."
    )
)
yourHobbies = []
yourHobbies.append(Hobby(
    "Rock Climbing",
    "First out of curiosity as to why all my friends were suddenly into rock climbing, I followed them to the gym one day. \
    A lot of things were a surprise (such as the fact that there was no rope to hold me up!), but above all that I was hooked after that day. \
    The versatility of skill, the intricate and subtle control, the social problem solving, and more are some reasons I'm addicted.",
    "../static/img/Rock-Climbing.png"
    )
)
yourHobbies.append(Hobby(
    "Cooking",
    "I'll admit, I've fallen prey to the temptation of delivery apps many days a semester. But even so, I do enjoy cooking. \
    Something about the act makes me present and clear-headed. I'll also have to admit that I'm not a good cook, though.",
    "../static/img/Cooking.png"
    )
)
yourHobbies.append(Hobby(
    "Music",
    "I love everything relating to music. I love playing it, listening to it, experiencing it, sharing it, and even writing it sometimes. \
    Don't let the picture of a piano fool you though, my taste in music isn't exclusively classic. Recently I've gotten into R&B, hyperpop, \
    metal, and indie.",
    "../static/img/Music.png"
    )
)

# This is the instance of "you", everything that will be on the portfolio is written in this object
you = User(yourName, yourPic, yourEd, yourWork, yourHobbies, "places")
