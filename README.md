## Skeletal Flask server with Jinja2 templates and Bootstrap 5 HTML

This project uses the [poetry utility](https://python-poetry.org/docs/).
If you don't already have it installed, please follow the instructions
on that page before buiding this project with the following commands:

    git clone git@github.com:holdenweb/py-star.git your-dir
    cd your-dir
    poetry install
    poetry build
    poetry run serve

If all has gone well this will create an HTTP server listening on
TCP port 8000 on all IP addresses.

Note that while the template established the layout of the page,
the variable data is inserted by the program at render time.
While the data in the current version is constant, there are many
interesting ways to gerenate it.
