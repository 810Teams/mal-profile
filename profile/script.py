'''
    `script.py`

    References
    - https://serennu.com/colour/hsltorgb.php
    - https://colorpalettes.net/color-palette-4202/
'''

from src.data import AutoReplacementData
from src.data import TagData
from src.data import TextFileConverter

import platform


DIR = 'profile/'
PALETTE = {
    'hr': '#e8e8e8',
    'font': '#0f0f0f',
    'score': {
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
    },
}
AUTO_REPLACEMENT_LIST = [
    # Tags
    AutoReplacementData('<profile>', '[size=120][color={}]'.format(PALETTE['font'])),
    AutoReplacementData('</profile>', '[/color][/size]'),
    AutoReplacementData('<hr>', ('[color={}]{}[/color]').format(PALETTE['hr'], 60 * '━')),
    # Text Variables
    AutoReplacementData('<score_10>', '[color={}]10[/color]'.format(PALETTE['score'][10])),
    AutoReplacementData('<score_9>', '[color={}]9[/color]'.format(PALETTE['score'][9])),
    AutoReplacementData('<score_8>', '[color={}]8[/color]'.format(PALETTE['score'][8])),
    AutoReplacementData('<score_7>', '[color={}]7[/color]'.format(PALETTE['score'][7])),
    AutoReplacementData('<score_6>', '[color={}]6[/color]'.format(PALETTE['score'][6])),
    AutoReplacementData('<score_5>', '[color={}]5[/color]'.format(PALETTE['score'][5])),
    AutoReplacementData('<score_4>', '[color={}]4[/color]'.format(PALETTE['score'][4])),
    AutoReplacementData('<score_3>', '[color={}]3[/color]'.format(PALETTE['score'][3])),
    AutoReplacementData('<score_2>', '[color={}]2[/color]'.format(PALETTE['score'][2])),
    AutoReplacementData('<score_1>', '[color={}]1[/color]'.format(PALETTE['score'][1])),
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
    AutoReplacementData('[/twitter]', '[/url]'),
    # Bullets Coloring
    AutoReplacementData('◆10', '[color={}]◆[/color]'.format(PALETTE['score'][10])),
    AutoReplacementData('◆9', '[color={}]◆[/color]'.format(PALETTE['score'][9])),
    AutoReplacementData('◆8', '[color={}]◆[/color]'.format(PALETTE['score'][8])),
    AutoReplacementData('◆7', '[color={}]◆[/color]'.format(PALETTE['score'][7])),
    AutoReplacementData('◆6', '[color={}]◆[/color]'.format(PALETTE['score'][6])),
    AutoReplacementData('◆5', '[color={}]◆[/color]'.format(PALETTE['score'][5])),
    AutoReplacementData('◆4', '[color={}]◆[/color]'.format(PALETTE['score'][4])),
    AutoReplacementData('◆3', '[color={}]◆[/color]'.format(PALETTE['score'][3])),
    AutoReplacementData('◆2', '[color={}]◆[/color]'.format(PALETTE['score'][2])),
    AutoReplacementData('◆1', '[color={}]◆[/color]'.format(PALETTE['score'][1])),
    # Auto bullets coloring
    AutoReplacementData('✦', '[color={}]✦[/color]'.format('#9579d1')),
    AutoReplacementData('★', '[color={}]★[/color]'.format('#be9ddf')),
    AutoReplacementData('✶', '[color={}]✶[/color]'.format('#ffa5d8')),
    AutoReplacementData('❤', '[color={}]❤[/color]'.format('#92ddea')),
    AutoReplacementData('✤', '[color={}]✤[/color]'.format('#7eb8da')),
    AutoReplacementData('✔', '[b][color={}]✔[/color][/b]'.format('#48b07e')),
    AutoReplacementData('✎', '[color={}]✎[/color]'.format('#ffcd42')),
    AutoReplacementData('✒', '[color={}]✒[/color]'.format('#f2a14a')),
]


def main():
    ''' Main function '''
    print()

    # v2
    converter = TextFileConverter(
        file_in_name=DIR + 'v2.txt',
        original_font_name='normal'
    )
    converter.convert(
        file_out_name=DIR + 'v2_fancy.txt',
        target_font_name='small_caps',
        auto_replacement_list=AUTO_REPLACEMENT_LIST,
        collapse='<<<<',
        tag=TagData('title', target_font_name='math_sans_bold_italic')
        
    )

    # v3
    converter = TextFileConverter(
        file_in_name=DIR + 'v3.txt',
        original_font_name='normal'
    )
    converter.convert(
        file_out_name=DIR + 'v3_fancy.txt',
        target_font_name='small_caps',
        auto_replacement_list=AUTO_REPLACEMENT_LIST,
        collapse='<<<<',
        tag=TagData('title', target_font_name='math_sans_bold_italic')
    )

    if platform.system() != 'Windows':
        print()

main()
