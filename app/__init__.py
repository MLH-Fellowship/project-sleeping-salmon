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

@app.route('/ariaHobbies')
def ariaHobbies():
    return render_template('ariaHobbies.html', url=os.getenv("URL"), user=Aria)

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
AriaName = "Aria Richardson"
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
users = [Hailey, Aria]