Description
==========

This is a test flask web server, designed to perform interview tasks.
It holds a list of following objects called candidates.

```
{
        'id': 1,
        'name': 'Volodymyr',
        'position': 'Software Test Engineer'
}
```

## Installation

*virtualenv*
Let's begin by installing Flask in a virtual environment. If you don't have virtualenv installed in your system, you can download it from [here](https://pypi.python.org/pypi/virtualenv)
```
sudo pip install virtualenv
virtualenv flask
flask/bin/pip install flask
```

Server can be run by just executing python code
```
chmod a+x app.py
./app.py &
```

Now your webserver is accessibleby this address `http://[your-host]:80/]

## Server allowed methods

- GET, `http://[your-host]/candidates/`, gives a list of all candidates. Returns 200
- GET, `http://[your-host]/candidates/<cand_id>`, shows a candidate with `id=<cand_id>`. Returns 200
- POST, `http://[your-host]/candidates/`, adds a new candidate. If a header `Content-Type: application/json` or `name` is absent, then 400 is returned. Returns 201
- DELETE, `http://[your-host]/candidates/<cand_id>`, deletes a candidate with `id=<cand_id>`. Returns 302
