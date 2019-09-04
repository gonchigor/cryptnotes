Install:

Require python3, pip, git, venv on computer.

1. Clone source code from GitHub. In destination directory run command:
    git clone https://github.com/gonchigor/cryptnotes.git
2. Create virtual environment for project. Run command:
    python -m venv env
3. Activate virtual environment. Run command: 
    env\scripts\activate
4. Install python packages: 
    pip install -r cryptnotes\requirements.txt
5. Go to directory cryptnotes. Run command: 
    cd cryptnotes

If you want to use clean database:

1. Delete file db.sqlite3 in cryptnotes directory.
2. Run command from cryptnotes directory: 
    python manage.py migrate

Run application:

1. Activate virtual environment.
2. Go to directory cryptnotes.
3. Run command: 
    python manage.py runserver
4. In browser goto link: http://127.0.0.1:8000/

Run unittests:

1. Activate virtual environment.
2. Go to directory cryptnotes.
3. Run command: 
    python -m unittest notes\unittest.py

You can use some parameters for unittest. For example, "-v" for additional test information. 
