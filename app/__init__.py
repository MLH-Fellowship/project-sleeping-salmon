import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Personal Portfolio", url=os.getenv("URL"), user=Hailey)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', url=os.getenv("URL"), user=Hailey)

# This is the User class that defines everything that will be inputted into the portfolio template
class User:
    def __init__(self, name, pic, education, work, hobbies, places):
        self.name = name
        self.pic = pic
        self.education = education
        self.work = work
        self.hobbies = hobbies
        self.places = places

# Education class is composed of school (school name), grad (graduation date), and major (area of study)
class Education:
    def __init__(self, school, grad, major, year):
        self.school = school
        self.grad = grad
        self.major = major
        self.year = year

# Experience class is composed of title (job title), company, and description
class Experience:
    def __init__(self, img, title, company, description):
        self.img = img
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
# and input it into the Jinja template for it to be formatted

yourName = "Hailey Moon"
yourPic = "../static/img/Headshot.png"
yourEd = Education("Boston University", "Expected May 2024", "Computer Science", "Rising Junior")
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
yourHobby = []
yourHobby.append(Hobbies("Rock Climbing", "./static/img/RockClimbing.jpg"))
yourHobby.append(Hobbies("Tennis", "./static/img/Tennis.jpg"))
yourHobby.append(Hobbies("Cooking", "./static/img/Cooking.jpg"))

Hailey = User(yourName, yourPic, yourEd, yourWork, yourHobby, "places")