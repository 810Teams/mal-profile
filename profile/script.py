'''
    `script.py`

    References
    - https://serennu.com/colour/hsltorgb.php
    - https://colorpalettes.net/color-palette-4202/
    - https://www.color-hex.com/color-palette/65486
'''

from src.data import AutoReplacementData
from src.data import TagData
from src.data import TextFileConverter

import platform


DIR = 'data/'
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
    'score_dim': {
        10: '#46ad7a', # '#57bb8a' dimmed by 10%
        8: '#9bbd5f',  # '#abc978' dimmed by 10%
        6: '#ffc942',  # '#ffd666' dimmed by 10%
        4: '#f29e49',  # '#f5b26c' dimmed by 10%
        2: '#e67350'   # '#eb8e71' dimmed by 10%
    },
    '#4202': [
        '#9579d1', # purple
        '#be9ddf', # light purple
        '#ffa5d8', # pink
        '#92ddea', # aqua
        '#7eb8da', # light blue
    ],
    'pink_martini': [
        '#dfffff', # aqua
        '#acd0ea', # light blue
        '#7f9fd0', # blue
        '#6760aa', # purple
        '#ffc5e8', # pink
    ]
}
AUTO_REPLACEMENT_LIST = [
    # New Tags
    AutoReplacementData('<profile>', '[center][size=120][color={}]'.format(PALETTE['font'])),
    AutoReplacementData('</profile>', '[/color][/size][/center]'),
    AutoReplacementData('<signature>', '[center][size=100][color={}][i]'.format(PALETTE['font'])),
    AutoReplacementData('</signature>', '[/i][/color][/size][/center]'),
    AutoReplacementData('<hr>', '[color={}]{}[/color]'.format(PALETTE['hr'], 60 * '━')),
    AutoReplacementData('<hr_s>', '[color={}]{}[/color]'.format(PALETTE['hr'], 36 * '━')),
    AutoReplacementData('<new>', '[i][color={}](New!)[/color][/i]'.format('red')),
    AutoReplacementData('<latest_h>', '[i][color=#E67C73]([/color][color=#E88671]L[/color][color=#EB9070]a[/color][color=#EE9A6E]t[/color][color=#F1A46D]e[/color][color=#F3AE6B]s[/color][color=#F6B86A]t[/color][color=#F9C268]![/color][color=#FCCC67])[/color][/i]'),
    AutoReplacementData('<latest_c>', '[i][color=#9579D1]([/color][color=#9280D2]L[/color][color=#8F87D3]a[/color][color=#8D8ED4]t[/color][color=#8A95D5]e[/color][color=#889CD6]s[/color][color=#85A3D7]t[/color][color=#83AAD8]![/color][color=#80B1D9])[/color][/i]'),
    # Text Variables
    AutoReplacementData('[10]', '[color={}]10[/color]'.format(PALETTE['score'][10])),
    AutoReplacementData('[9]', '[color={}]9[/color]'.format(PALETTE['score'][9])),
    AutoReplacementData('[8]', '[color={}]8[/color]'.format(PALETTE['score'][8])),
    AutoReplacementData('[7]', '[color={}]7[/color]'.format(PALETTE['score'][7])),
    AutoReplacementData('[6]', '[color={}]6[/color]'.format(PALETTE['score'][6])),
    AutoReplacementData('[5]', '[color={}]5[/color]'.format(PALETTE['score'][5])),
    AutoReplacementData('[4]', '[color={}]4[/color]'.format(PALETTE['score'][4])),
    AutoReplacementData('[3]', '[color={}]3[/color]'.format(PALETTE['score'][3])),
    AutoReplacementData('[2]', '[color={}]2[/color]'.format(PALETTE['score'][2])),
    AutoReplacementData('[1]', '[color={}]1[/color]'.format(PALETTE['score'][1])),
    # BB Code Tags Altering
    AutoReplacementData('[mal=', '[url=https://myanimelist.net/'),
    AutoReplacementData('[/mal]', '[/url]'),
    AutoReplacementData('[forum=', '[url=https://myanimelist.net/forum/?topicid='),
    AutoReplacementData('[/forum]', '[/url]'),
    AutoReplacementData('[blog=', '[url=https://myanimelist.net/blog.php?eid='),
    AutoReplacementData('[/blog]', '[/url]'),
    AutoReplacementData('[genre=', '[url=https://myanimelist.net/anime/genre/'),
    AutoReplacementData('[/genre]', '[/url]'),
    AutoReplacementData('[animelist=', '[url=https://myanimelist.net/animelist/'),
    AutoReplacementData('[/animelist]', '[/url]'),
    AutoReplacementData('[mangalist=', '[url=https://myanimelist.net/mangalist/'),
    AutoReplacementData('[/mangalist]', '[/url]'),
    AutoReplacementData('[profile=', '[url=https://myanimelist.net/profile/'),
    AutoReplacementData('[/profile]', '[/url]'),
    AutoReplacementData('[people=', '[url=https://myanimelist.net/people/'),
    AutoReplacementData('[/people]', '[/url]'),
    AutoReplacementData('[review=', '[url=https://myanimelist.net/reviews.php?id='),
    AutoReplacementData('[/review]', '[/url]'),
    AutoReplacementData('[twitter=', '[url=https://twitter.com/'),
    AutoReplacementData('[/twitter]', '[/url]'),
    AutoReplacementData('[pixiv=', '[url=https://pixiv.net/'),
    AutoReplacementData('[/pixiv]', '[/url]'),
    AutoReplacementData('[greasyfork=', '[url=https://greasyfork.org/'),
    AutoReplacementData('[/greasyfork]', '[/url]'),
    AutoReplacementData('[alphac=', '[url=https://wall.alphacoders.com/big.php?i='),
    AutoReplacementData('[/alphac]', '[/url]'),
    AutoReplacementData('[16p=', '[url=https://www.16personalities.com/profiles/'),
    AutoReplacementData('[/16p]', '[/url]'),
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
    AutoReplacementData('✦', '[color={}]✦[/color]'.format(PALETTE['#4202'][0])),
    AutoReplacementData('★', '[color={}]★[/color]'.format(PALETTE['#4202'][1])),
    AutoReplacementData('❤', '[size=80][color={}]❤[/color][/size]'.format(PALETTE['#4202'][2])),
    AutoReplacementData('✤', '[color={}]✤[/color]'.format(PALETTE['#4202'][3])),
    AutoReplacementData('✔', '[b][color={}]✔[/color][/b]'.format(PALETTE['score_dim'][10])),
    AutoReplacementData('✎', '[color={}]✎[/color]'.format(PALETTE['score_dim'][6])),
    AutoReplacementData('✒', '[color={}]✒[/color]'.format(PALETTE['score_dim'][4])),
]


def main():
    ''' Main function '''
    print()

    # Profile (810Teams)
    converter = TextFileConverter(
        file_in_name=DIR + 'profile.txt',
        original_font_name='normal'
    )
    converter.convert(
        file_out_name=DIR + 'profile_fancy.txt',
        target_font_name='small_caps',
        auto_replacement_list=AUTO_REPLACEMENT_LIST,
        collapse='<<<<',
        tag=TagData('title', target_font_name='math_sans_bold_italic')
    )

    # Profile (810Teams_EX)
    converter = TextFileConverter(
        file_in_name=DIR + 'profile_ex.txt',
        original_font_name='normal'
    )
    converter.convert(
        file_out_name=DIR + 'profile_ex_fancy.txt',
        target_font_name='small_caps',
        auto_replacement_list=AUTO_REPLACEMENT_LIST,
        collapse='<<<<',
        tag=TagData('title', target_font_name='math_sans_bold_italic')
    )


    # Signature
    converter = TextFileConverter(
        file_in_name=DIR + 'signature.txt',
        original_font_name='normal'
    )
    converter.convert(
        file_out_name=DIR + 'signature_fancy.txt',
        target_font_name='normal',
        collapse='<<<<',
        auto_replacement_list=AUTO_REPLACEMENT_LIST
    )

    if platform.system() != 'Windows':
        print()

main()
