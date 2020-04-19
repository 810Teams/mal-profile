'''
    `script.py`
'''

from src.data import TextFileConverter

import platform


DIR = 'profile/'


def main():
    ''' Main function '''
    print()

    converter = TextFileConverter(
        '{}{}'.format(DIR, 'v1.txt'),
        '{}{}'.format(DIR, 'v1_fancy.txt')
    )

    converter.convert(
        original_font='normal',
        title_font='math_sans_bold_italic',
        content_font='small_caps'
    )

    if platform.system() != 'Windows':
        print()

main()
