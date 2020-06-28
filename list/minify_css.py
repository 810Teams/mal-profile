'''
    minify_css.py
'''

from src.utils import notice

import platform
import requests

API_URL = 'https://cssminifier.com/raw'
CSS_NAME = 'brink-1.4.3'
CSS_PATH = 'web/css/{}.css'.format(CSS_NAME)
MIN_CSS_PATH = 'web/css/min/{}.min.css'.format(CSS_NAME)


def main():
    data = {'input': open(CSS_PATH, 'rb').read()}
    response = requests.post(API_URL, data=data)

    min_data = open(MIN_CSS_PATH, 'w')
    min_data.write(response.text)
    min_data.close()

    print()
    notice('Minified CSS `{}` has been created, minified from {} to {} characters.'.format(
        CSS_NAME,
        len(''.join(list(open(CSS_PATH)))),
        len(response.text)
    ))

    # Windows' cmd fix
    if platform.system() != 'Windows':
        print()


main()
