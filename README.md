# hike-hitch
## My Hike Hitch web application

1. User enters main page
  -Greeted with title
  -option to sign up or login 
  -view the hikes listed

2. Once a member, able to:
  -create profile
  -add image
  -links to social media
  -write bio
  -post a new hike
    *adding an image
    *description
    *location
    *Difficulty, etc
  -View hikes in the calendar
    *join existing hikes
  -few profiles of other hikers

* As a visitor, I want to sign up because I will be able to view the calendar of hikes and enjoy the features of the app.
* As a member(hiker), I want to log in, so I can view all the features of the app.
* As a hiker I want to check the calendar for other pre made hikes, because I want to join a hike that meets my requirements with other hikers of the same level, one of whom can drive me.
* As a hiker, I want to vew other members on the hike, because I want to determine if these are people Id be willing to go into the woods with.
* As a hiker, I want to create a new hike, because a hike does not exist that meets my requirements.
* As a hiker, I want to add a new trail because one does not exist in the system.
* As a hiker, I want to view the trails and and filter them based on what Im looking for.

## ERD Models

![ERD Model][Imgur](https://i.imgur.com/z7dHUN8.png))

## Technologies Used
1. Python
2. Django
3. pSQL

## Road Blocks

This was not the easiest of projects, as I learned in the later days of project week. 

Creating templates and writing the urls and view functions became fairly easy to pick up from the prior week's learnings. Occasionally I would write incorrect url paths and would be met with NoReverseMatch error, which I quickly learned to hate. As time grew between these errors, I felt more confidence in my path writing, but would soon be introduce to new errors.

Creating profiles became more of a task than I originally imagined it would be. With a one to one  relationship between User and Hiker(profile), I would have imagined their id's were going to correspond with one and another. Unfortunately, they became mismatched in the process of creating new users and I was left with profiles belonging to the wrong users. The bug lied in how I  was  constructing my Profile URL. I was happened to be searching for `hiker.id` instead  of `user.hiker.id`, as this OneToOne relationship was needing me to looking in a different column than what I was looking for.

One the last day before my project week I ran into the problem of not knowing how to access information on the intermediary tables betweenmy models. It led meto believe I should have constructed additional models to bridge  between my models with ManyToMany relations. So in a last minute attempt to have proper functionality I redrew my ERD. Adding a TrailChoice model between my Trail and Trip Models, and also a Team model between my Hiker and Trip model
![Imgur](https://i.imgur.com/GG1Af1L.jpg)

When I tried to fix my tables and run the server. This error showed after trying to created a trip.
So I was forced to return to the original state of my code.
![Imgur](https://i.imgur.com/4U2GKy6.png)