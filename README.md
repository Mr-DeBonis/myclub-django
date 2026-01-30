# My First Django App

This is my follow up from the [django  wednesdays club app from codemy.com](https://www.youtube.com/playlist?list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy).

# Installation

1. Create virtual environment and install requirements:
    ```
   pip install -r requirements.txt
    ```

2. To create changes from the model:
    ```
    python manage.py makemigrations
    ```
    * To preview sql migrations, run:
    ```
    python manage.py sqlmigrate events 0001
    ```
2. To apply changes to the database:

```
python manage.py migrate
```

3. Create an admin

```
python manage.py createsuperuser
```

4. Access the django shell:

```
python manage.py shell

```

## Running tests

```
python manage.py test events

```

# PDF generation
It uses [z3c.rml](https://github.com/zopefoundation/z3c.rml) to generate pdfs from templates.
* [z3c.RML reference](https://raw.githubusercontent.com/zopefoundation/z3c.rml/refs/heads/master/src/z3c/rml/rml-reference.pdf)
* [RML official docs](https://docs.reportlab.com/rmlfornewbies/)