# SyllaBestie
#### UIUC CS222 Fall 2022
#### Created by: Chris Tang, Aditi Roy, Abena Laast, Eric Ly
course-project-group-14 created by GitHub Classroom

## Project Description
Every semester, students receive syllabi from every class with a multitude of information about grades, resources and dates. To help students manage their schedules, SyllaBestie goes through your syllabus and instantaneously outputs a calendar file with all the important dates to remember, which can be instantly imported into popular calendar platforms like Google Calendar and Apple Calendar.  Our motivation for creating SyllaBestie was to streamline the process of finding important dates for classes.  Many students (especially new freshman) struggle with keeping track of assignment dates for multiple classes throughout the semester.  Furthermore, not all classes import due dates and assignments onto Canvas or Moodle, and nobody likes constantly sifting through the syllabus to check when assignments are due.  With SyllaBestie, this process can be avoided because all due dates can be instantly transcribed into your digital calendar for increased visibility through your computer and phone!

## Architecture
The architecture for SyllaBestie consisted of the integration of a frontend, a backend, and a server.

### Frontend
The frontend consisted of Python, Flask, Jinja2, and Bootstrap.  The frontend allowed the user to interact with the backend with a pleasing-to-the-eye web application.  Using HTML, CSS, and Bootstrap, templates for webpages were created to display instructions, buttons, and an interface that the user could use to parse syllabi and call backend components.  We used libraries for Flask and frontend forms/security for the rendering of webpages and ensuring the downloading of pdf files was consistent.  The main webpages for the web app include: the homepage, the intermediate parsing page, the download csv page, and profile pages for the software developers.  The frontend was completed by Chris.  

### Backend
The backend consisted of Python and Flask.  Flask was chosen over other libraries for its lightweight characteristic as well as its ability to operate as a simple and clean frontend.  Once called by the frontend, the backend executes data/String mainpulation and parses a syllabus, which is passed as a pdf document, and then reads through it for dates as well as assignment/exam details.  
Note: In order for parsing to successfully execute, the syllabus must follow a specific structure: DATE ASSIGNMENT NAME. 
DATE is in MONTH/DAY form and ASSIGNMENT NAME can be anything.  An example syllabus can be found in our repository.  This structure was chosen because it was seen in multiple syllabi such as MA257.  This process utilized many Python libraries, namely those for parsing documents and regular exressions like PyPDF2, re, and csv. Backend work was completed by the backend team: Erik, Aditi, and Abena.   

### Server
The server is run on pythonanywhere.com, free web hosting server for Python and Flask applications.  The server allowed our application to be run on the Internet as opposed to being run locally, which would involve installation of software, an IDE to run it, etc.  Our server allowed us to integrate the frontend and backend on the Internet so that it could be easily used.  Creating the server to run our web application did not necessitate using any libraries, as libraries were already imported in the frontend and backend components.  The server was set up and configured by Chris.

## Installation Instructions
To run the application locally, clone the repository into an IDE (we used VSCode) and navigate to main/Frontend/app.  Run the application and then click the link in the terminal called 'http://127.0.0.1:5000/' to open SyllaBestie locally.

To utilize the web application version of SyllaBestie, please navigate to: <a href="https://chtang.pythonanywhere.com" target="_blank">here</a>.

## Group Members and Roles
Chris Tang - Software Developer for Frontend and Server     
Aditi Roy - Software Developer for Backend   
Abena Laast - Software Developer for Backend   
Erik Ly - Software Developer for Backend and Data Transfer   
