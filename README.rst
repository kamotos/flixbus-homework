flixbus
=======

Flixbus Data Engineer/Backend Developer homework assignment

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test



Docker
^^^^^^

To run project in dev environment (make sure you have the latest versions of docker and docker-compose installed) :

::

  $ docker-compose -f dev.yml build
  $ docker-compose -f dev.yml run django python manage.py migrate
  $ docker-compose -f dev.yml up -d


