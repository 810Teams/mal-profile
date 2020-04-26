'''
    `script.py`
'''

from src.data import TextFileConverter

import platform


DIR = 'profile/'


def main():
    ''' Main function '''
    print()

    # v2
    converter = TextFileConverter(
        '{}{}'.format(DIR, 'v2.txt'),
        '{}{}'.format(DIR, 'v2_fancy.txt')
    )

    converter.convert(
        original_font='normal',
        title_font='math_sans_bold_italic',
        content_font='small_caps'
    )

    # v3
    converter = TextFileConverter(
        '{}{}'.format(DIR, 'v3.txt'),
        '{}{}'.format(DIR, 'v3_fancy.txt')
    )

    converter.convert(
        original_font='normal',
        title_font='math_sans_bold_italic',
        content_font='small_caps'
    )

    if platform.system() != 'Windows':
        print()

main()
