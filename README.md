A Heroku/Flask-powered JSONP Wrapper for Texas Reservoir Data
=============================================================

This [Heroku](http://www.heroku.com/) [Flask](http://flask.pocoo.org/) app takes the [JSON feed of reservoir data](http://waterdatafortexas.org/reservoirs/recent-conditions.json) from the Texas Water Development Board's [Water Data for Texas](http://waterdatafortexas.org/reservoirs/statewide) web site in turns it into a jQuery consumable JSONP feed. In theory, this should work for any JSON feed you toss at it.

Installation and Usage
----------------------

*This guide assumes you already have Heroku installed and set up on your machine.*

First run:

    pip install -r requirements.txt

Then set up git for Heroku:

    git init
    git add .
    git commit -m "Initial commit"

Create a Heroku app, then deploy to it:

    heroku create
    git push heroku master

Finally, give Heroku the go ahead to fire up one dyno (this should not incur any charges), and open the app:

    heroku ps:scale web=1
    heroku open

**You will need to add `/reservoirs.json` to the end of the URL to view the feed.**
