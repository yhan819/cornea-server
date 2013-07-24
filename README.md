Cornea Reader
======

### Important: How to run ###

(Currently, this application uses coffeescript, handlebars, and less. You may need to install some or all of these libraries to be able to run the application, even locally)

1. Activate the environment: <code>source ~/DIRECTORYPATH/bin/activate</code>
2. Run the app: <code>python run.py</code>
3. Each time you open the application, run <code>python compiler.py</code>, then REFRESH! (necessary)

### Links ###

- <a href="https://github.com/namejames91/reader2" target="_blank">James' Reader Repository</a>

- <a href="https://docs.google.com/document/d/1beOk0C9akyP1IJbl2NXgXpm7TkNPocqTxNZEK1QNKyc/edit" target="_blank">TODO list</a>

- <a href="http://github-markdown-preview.heroku.com/" target="_blank">Markdown Preview</a>

- <a href="http://flask.pocoo.org/docs/tutorial/" target="_blank">Flask Tutorial</a>

### Initial Setup ###

1. get virtualenv and python2.7

2. clone the repo and go into that directory.

3. create virtualenv

    <code>virtualenv -p python2.7 ~/DIRECTORYPATH</code>

4. activate the environment:

    <code>source ~/DIRECTORYPATH/bin/activate</code>

5. install required packages with pip

    <code>pip install -r requirements.txt</code>

6. Go to internal/dev-env to set up the zsh environment (screenshot is there). It shows your git branch status as well! :)

7. SETUP DB, if cornea.db doesn't exist in your local repo, create the local db first

    <code>python db_create.py</code>

8. if you have cornea.db, upgrade to the latest db

    <code>python db_upgrade.py</code>
