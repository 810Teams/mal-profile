'''
    `script.py`
'''

from src.data import AutoReplacementData
from src.data import TagData
from src.data import TextFileConverter

import platform


DIR = 'profile/'
PALETTE = {
    'hr': '#e8e8e8',
    'font': '#0f0f0f'
}
PALETTE_SCORE = {
    10: '#57bb8a',
    9: '#81c281',
    8: '#abc978',
    7: '#d5d06f',
    6: '#ffd666',
    5: '#fac469',
    4: '#f5b26c',
    3: '#f0a06e',
    2: '#eb8e71',
    1: '#e67c73',
}


def main():
    ''' Main function '''
    print()

    auto_replacement_list = [
        # Tags
        AutoReplacementData('<profile>', '[size=120][color={}]'.format(PALETTE['font'])),
        AutoReplacementData('</profile>', '[/color][/size]'),
        AutoReplacementData('<hr>', ('[color={}]' + 60 * '━' + '[/color]').format(PALETTE['hr'])),
        # Text Variables
        AutoReplacementData('<score_10>', '[color={}]10[/color]'.format(PALETTE_SCORE[10])),
        AutoReplacementData('<score_9>', '[color={}]9[/color]'.format(PALETTE_SCORE[9])),
        AutoReplacementData('<score_8>', '[color={}]8[/color]'.format(PALETTE_SCORE[8])),
        AutoReplacementData('<score_7>', '[color={}]7[/color]'.format(PALETTE_SCORE[7])),
        AutoReplacementData('<score_6>', '[color={}]6[/color]'.format(PALETTE_SCORE[6])),
        AutoReplacementData('<score_5>', '[color={}]5[/color]'.format(PALETTE_SCORE[5])),
        AutoReplacementData('<score_4>', '[color={}]4[/color]'.format(PALETTE_SCORE[4])),
        AutoReplacementData('<score_3>', '[color={}]3[/color]'.format(PALETTE_SCORE[3])),
        AutoReplacementData('<score_2>', '[color={}]2[/color]'.format(PALETTE_SCORE[2])),
        AutoReplacementData('<score_1>', '[color={}]1[/color]'.format(PALETTE_SCORE[1])),
        # Bullet Varibles
        AutoReplacementData('◆10', '[color={}]◆[/color]'.format(PALETTE_SCORE[10])),
        AutoReplacementData('◆9', '[color={}]◆[/color]'.format(PALETTE_SCORE[9])),
        AutoReplacementData('◆8', '[color={}]◆[/color]'.format(PALETTE_SCORE[8])),
        AutoReplacementData('◆7', '[color={}]◆[/color]'.format(PALETTE_SCORE[7])),
        AutoReplacementData('◆6', '[color={}]◆[/color]'.format(PALETTE_SCORE[6])),
        AutoReplacementData('◆5', '[color={}]◆[/color]'.format(PALETTE_SCORE[5])),
        AutoReplacementData('◆4', '[color={}]◆[/color]'.format(PALETTE_SCORE[4])),
        AutoReplacementData('◆3', '[color={}]◆[/color]'.format(PALETTE_SCORE[3])),
        AutoReplacementData('◆2', '[color={}]◆[/color]'.format(PALETTE_SCORE[2])),
        AutoReplacementData('◆1', '[color={}]◆[/color]'.format(PALETTE_SCORE[1])),
        # BB Code Tag Altering
        AutoReplacementData('[genre=', '[url=https://myanimelist.net/anime/genre/'),
        AutoReplacementData('[/genre]', '[/url]'),
        AutoReplacementData('[animelist=', '[url=https://myanimelist.net/animelist/'),
        AutoReplacementData('[/animelist]', '[/url]'),
        AutoReplacementData('[profile=', '[url=https://myanimelist.net/profile/'),
        AutoReplacementData('[/profile]', '[/url]'),
        AutoReplacementData('[people=', '[url=https://myanimelist.net/people/'),
        AutoReplacementData('[/people]', '[/url]'),
        AutoReplacementData('[review=', '[url=https://myanimelist.net/reviews.php?id='),
        AutoReplacementData('[/review]', '[/url]'),
        AutoReplacementData('[twitter=', '[url=https://twitter.com/'),
        AutoReplacementData('[/twitter]', '[/url'),
        # Auto-coloring
        AutoReplacementData('✔', '[color={}]✔[/color]'.format(PALETTE_SCORE[10])),
        AutoReplacementData('✎', '[color={}]✎[/color]'.format(PALETTE_SCORE[6])),
    ]

    # v2
    converter = TextFileConverter(
        file_in_name=DIR + 'v2.txt',
        original_font_name='normal'
    )
    converter.convert(
        file_out_name=DIR + 'v2_fancy.txt',
        target_font_name='small_caps',
        tag=TagData('title', target_font_name='math_sans_bold_italic'),
        auto_replacement_list=auto_replacement_list
    )

    # v3
    converter = TextFileConverter(
        file_in_name=DIR + 'v3.txt',
        original_font_name='normal'
    )
    converter.convert(
        file_out_name=DIR + 'v3_fancy.txt',
        target_font_name='small_caps',
        tag=TagData('title', target_font_name='math_sans_bold_italic'),
        auto_replacement_list=auto_replacement_list
    )

    if platform.system() != 'Windows':
        print()

main()
