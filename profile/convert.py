'''
    `convert.py`
'''

from src.font import Font

import platform


DIR = 'profile/'


def main():
    ''' Main function '''
    print()

    convert(
        '{}{}'.format(DIR, 'v1.txt'),
        '{}{}'.format(DIR, 'v1_fancy.txt'),
        original_font='normal',
        title_font='math_sans_bold_italic',
        content_font='small_caps'
    )

    if platform.system() != 'Windows':
        print()


def convert(file_in_name, file_out_name, original_font='normal', title_font='math_sans_bold_italic', content_font='small_caps'):
    ''' Convert function '''
    font = Font()

    file_in = [i.replace('\n', '') for i in open(file_in_name, encoding='utf-8')]
    file_out = open(file_out_name, 'w', encoding='utf-8')

    # Transform line by line
    for i in range(len(file_in)):
        file_in[i] = font.transform(file_in[i], tag_name='title', source=original_font, target=title_font)
        file_in[i] = font.transform(file_in[i], source=original_font, target=content_font)

    file_in = '\n'.join(file_in)
    file_out.write(file_in)
    file_out.close()

    print('[NOTICE] Successfully created `{}` from `{}`.'.format(file_out_name, file_in_name))


main()
