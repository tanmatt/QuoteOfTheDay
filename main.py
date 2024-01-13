import requests
import time

README = "README.md"
API_URL = "https://favqs.com/api/qotd"
API_QUOTE_KEY = 'quote'
API_QUOTE_BODY_KEY = 'body'
API_QUOTE_AUTHOR_KEY = 'author'


def _get_quote_of_the_day():
    r = requests.get(API_URL).json()
    quote_struct = r[API_QUOTE_KEY]
    quote = quote_struct[API_QUOTE_BODY_KEY]
    author = quote_struct[API_QUOTE_AUTHOR_KEY]
    line = quote + " - " + author
    print(line)
    return line


def _update_readme():
    """
    update main section first
    """
    quote = _get_quote_of_the_day()
    with open(README, 'r') as file:
        lines = file.readlines()  # Read all lines into a list

    with open(README, 'w') as file:  # Open in write mode to overwrite
        file.writelines(lines[:1])  # Write the first line
        file.write(quote + '\n')  # Write the new line on the second line
        file.writelines(lines[2:])  # Write the remaining lines minus the previous quote

    line = "- " + time.asctime(time.localtime()) + " | "
    try:
        line += quote
    except Exception as ex:
        line += ex.__str__()
    finally:
        """Appends a line to the end of a file."""
        with open(README, 'a') as file:
            file.write(line + '\n')


if __name__ == "__main__":
    _update_readme()
