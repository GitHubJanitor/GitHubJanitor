# TheGithubJanitor
TODO: CI badge

# Setup
Install Django on your host machine. (Be sure to explicitly uninstall earlier versions first, or use a virtualenv -
having earlier versions around seems to cause pre-1.4-style settings.py and urls.py files to be generated alongside the
new ones.)

Run the following commands:

    git clone git@github.com:GitHubJanitor/GitHubJanitor.git
    cd GitHubJanitor
    vagrant up
    vagrant ssh
      (then, within the SSH session:)
    ./manage.py runserver 0.0.0.0:8000

This will make the app accessible on the host machine as http://localhost:8000/ . The codebase is located on the host
machine, exported to the VM as a shared folder; code editing and Git operations will generally be done on the host.

# See also
Based on the django template https://github.com/torchbox/vagrant-django-template

# Authors
- [Federico Castagnini](https://github.com/facastagnini)
- [Patricio Palladino](https://github.com/alcuadrado)
- [Diego Alifano](https://github.com/diegus83)
