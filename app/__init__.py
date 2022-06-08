import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), users=users)

@app.route('/haileyHobbies')
def haileyHobbies():
    return render_template('haileyHobbies.html', url=os.getenv("URL"), user=Hailey)

@app.route('/test')
def test():
    return render_template('child.html')

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
# and input it into the Jinja template for it to be formatted

HaileyName = "Hailey Moon"
HaileyPic = "./static/img/HaileyPic.png"
HaileyAbout = "Hi there! My name is Hailey and I am from South Korea and Boston, MA. I am passionate about the intersection of design and computer science, and I am always looking for opportunities to learn!"
HaileyEducation = Education("Boston University", "Expected May 2024", "Computer Science")
HaileyWork = []
HaileyWork.append(Work("UI/UX Designer", "Cashmate", \
    ["Conducted user research, problem validation, solution validation, created customer personas, 10 user stories, and user flows to plan for end-to-end app development and deployment by the end of the semester.", \
    "Designed typography, assets, low-fidelity, and high-fidelity wireframes using Figma for an IOS mobile application which used Firebase for backend and React Native for frontend."]))
HaileyWork.append(Work("Design Head", "BostonHacks", \
    ["Developed 6 unique website designs, 20+ marketing materials, and 9+ social media graphics on Figma by utilizing the theme colors and assets to establish a clear brand identity.", \
    "Lead a team of 8 designers and initiated communications with 4 other internal team heads to receive tasks, request information, and delegate work to prepare for 2 hybrid hackathons per year."]))
HaileyWork.append(Work("Graphic Design Intern", "BU Spark!", \
    ["Developed creative concepts for merchandise design and marketing graphics that align with Spark! branding guidelines to promote brand awareness", \
    "Coordinated with 2+ other interns and supervisor weekly to brainstorm fresh solutions for current projects and review designs in real-time."]))
HaileyHobby = []

HaileyHobby.append(Hobbies("Rock Climbing", "./static/img/RockClimbing.jpg"))
HaileyHobby.append(Hobbies("Tennis", "./static/img/Tennis.jpg"))
HaileyHobby.append(Hobbies("Cooking", "./static/img/Cooking.jpg"))

Hailey = User(HaileyName, HaileyPic, HaileyAbout, HaileyEducation, HaileyWork, HaileyHobby, "places")


# List of users that will be included in this portfolio
users = [Hailey]