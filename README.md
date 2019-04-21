# WiC Poll System
This project is meant to be a system for keeping track of the whimsical polls WiC members make in our space on the whiteboard. By keeping track of these polls electronically it allows more WiC members to participate and for record keeping. We can use the record of these polls for fun games like a "Familly Fued" game using the poll as survey questions.

This repository is for the API backend built in Flask. There is a [separate repository for the slack bot](https://github.com/Women-in-Computing-at-RIT/poll_system_slackbot) and a [different repository for the mobile app.](https://github.com/Women-in-Computing-at-RIT/poll_system_flutter_app)

Projects 2018-2019.

### how to run
Linux/Mac:
- ```export FLASK_APP=poll-system```
- ```export FLASK_ENV=development```
- ```flask run```

Windows:
- ```set FLASK_APP=poll-system```
- ```set FLASK_ENV=development```
- ```flask run```

Both: run after first ```flask run```
- ```flask init-db```
