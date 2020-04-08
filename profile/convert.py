'''
    `convert.py`
'''

from src.font import Font


def main():
    ''' Main function '''
    print()

    convert(
        'profile.txt',
        'profile_v1.txt',
        original_font='normal',
        title_font='math_sans_bold_italic',
        content_font='small_caps'
    )
    convert(
        'profile.txt',
        'profile_plain.txt', 
        original_font='normal',
        title_font='normal',
        content_font='normal'
    )

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
