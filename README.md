# Meme Project

## Meme module

This module has all the models and functions required for generating memes. It
is located in the meme folder.

## Usage

### Command line usage

You can run this module in command line using the following command:
```
python -m meme --path <path_of_the_file> --body <quote_body> --author <quote_author>
```

### Usage via webbrowser

For this just run the `app.py` file via your Python 3.x interpreter:
```
> python3 app.py
```

## Dependencies

Install all needed dependencies via `pip` like this:
```
pip install -r requirements.txt
```

[pillow](https://pillow.readthedocs.io/en/stable/) => This package is used to
draw text over images.