# taekwondo

Manage Taekwondo teams, competitors and competitions. Web based portal allows you to register competitor to particular competition.

## Demo
Not available yet.

## License

All source code in the [Taekwondo](https://github.com/valasek/taekwondo) is available under the GNU GPL v3 License. See [LICENSE.md](LICENSE.md) for details.

## Getting started

To get started with the app, clone the repo and then install Python 3 and Django 1.10:

```
$ cd ~/tmp
$ git clone https://github.com/valasek/taekwondo
$ cd taekwondo
```

Next, migrate the database:

```
$ ./manage.py makemigrations
$ ./manage.py migrate
```

Finally, run the test suite to verify that everything is working correctly:

```
$ ./manage.py test
```

If the test suite passes, you'll be ready to run the app in a local server:

```
$ ./manage.py runserver
```
