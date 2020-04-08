'''
    `convert.py`
'''

from src.font import Font


def main():
    ''' Main function '''
    convert('profile_editor.txt', 'profile_decorized.txt', 'normal', 'math_sans_bold_italic', 'small_caps')
    convert('profile_editor.txt', 'profile_plain.txt', 'normal', 'normal', 'normal')


def convert(file_in_name, file_out_name, original_font_name, title_font_name, content_font_name):
    ''' Convert function '''
    font = Font()

    file_in = [i.replace('\n', '') for i in open(file_in_name, encoding='utf-8')]

    file_out = open(file_out_name, 'w', encoding='utf-8')

    for i in range(len(file_in)):
        file_in[i] = font.transform_tag(file_in[i], tag_name='title', source=original_font_name, target=title_font_name)
        file_in[i] = font.transform(file_in[i], source=original_font_name, target=content_font_name)

    file_in = '\n'.join(file_in)

    file_out.write(file_in)
    file_out.close()


main()
