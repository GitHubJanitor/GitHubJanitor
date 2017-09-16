# TheGithubJanitor
TODO: CI badge

# Setup

# Test/dev environment
Run the following commands:

    brew install python3
    git clone git@github.com:GitHubJanitor/GitHubJanitor.git
    cd GitHubJanitor

    # this will bootstrap the virtualenv
    source setup_virtualenv.sh

    # manage the database
    python3 ./manage.py migrate

    # create admin user
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('federico', 'federico.castagnini@gmail.com', 'changeme')" | python manage.py shell

    # launch the dev service
    ./manage.py runserver 0.0.0.0:8000

This will make the app accessible on the host machine as http://localhost:8000/ .

# Authors
- [Federico Castagnini](https://github.com/facastagnini)
- [Diego Alifano](https://github.com/diegus83)
- [Srikanth Viswanathan](https://github.com/srikanth-viswanathan)
