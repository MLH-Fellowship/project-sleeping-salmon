import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Personal Portfolio", url=os.getenv("URL"), user=you)

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Personal Portfolio", url=os.getenv("URL"), user=you)

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