'''
    `data.py`
'''


class Font:
    NORMAL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    SMALL_CAPS = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘ') + ('ᴏ̨',) + tuple('ʀsᴛᴜᴠᴡxʏᴢ')
    CIRCLED = 'ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ'
    CIRCLED_NEG = '🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩'
    FULLWIDTH = 'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ'
    MATH_BOLD = '𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳'
    MATH_BOLD_FRAKTUR = '𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟'
    MATH_BOLD_ITALIC = '𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛'
    MATH_BOLD_SCRIPT = '𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃'
    MATH_DOUBLE_STRUCK = '𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫'
    MATH_MONOSPACE = '𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣'
    MATH_SANS = '𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓'
    MATH_SANS_BOLD = '𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇'
    MATH_SANS_BOLD_ITALIC = '𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯'
    MATH_SANS_ITALIC = '𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻'
    PARENTHESIZED = '⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵'

class TagData:
    def __init__(self, name, target_font_name='math_sans_bold_italic'):
        self.name = name
        self.target_font_name = target_font_name
        self.state = 0
    
    def to_list(self):
        return [self.name, self.target_font_name, self.state]

    def to_dict(self):
        return {
            'name': self.name,
            'target_font_name': self.target_font_name,
            'state': self.state
        }

class AutoReplacementData:
    def __init__(self, original, target):
        self.original = original
        self.target = target
    
    def to_list(self):
        return [self.original, self.target]
    
    def to_dict(self):
        return {
            'original': self.original,
            'target': self.target
        }

class TextFileConverter:
    def __init__(self, file_in_name='a.txt', original_font_name='normal'):
        self.file_in_name = file_in_name
        self.original_font_name = original_font_name

    def convert(
        self,
        file_out_name='out.txt',
        target_font_name='small_caps',
        auto_replacement_list=list(),
        collapse=None,
        tag=None
    ):
        file_in = [i.replace('\n', str()) for i in open(self.file_in_name, encoding='utf-8')]
        file_out = open(file_out_name, 'w', encoding='utf-8')

        # Transform line-by-line
        for i in range(len(file_in)):
            file_in[i] = self.convert_line(
                file_in[i],
                target_font_name=target_font_name,
                tag=tag,
                auto_replacement_list=auto_replacement_list
            )

        file_in = '\n'.join(file_in)

        if collapse is not None:
            file_in = file_in.replace('\n{}'.format(collapse), str())
            file_in = file_in.replace('{}\n'.format(collapse), str())

        file_out.write(file_in)
        file_out.close()

        print('[NOTICE] Successfully created `{}` from `{}`.'.format(file_out_name, self.file_in_name))


    def convert_line(self, message, target_font_name='small_caps', tag=None, auto_replacement_list=list()):
        original_font = eval('Font.' + self.original_font_name.upper())
        target_font = eval('Font.' + target_font_name.upper())

        if tag != None:
            tag_target_font = eval('Font.' + tag.target_font_name.upper())
       
        # Auto Replacement Transformation
        for i in auto_replacement_list:
            message = message.replace(i.original, i.target)
        
        message = list(message)

        # Tag Transformation
        is_in_bb_tag = False
        if isinstance(tag, TagData):
            i = 0
    
            while i < len(message):
                if message[i] == '[':
                    is_in_bb_tag = True
                elif message[i] == ']':
                    is_in_bb_tag = False

                    try:
                        if message[i - 4:i + 1] == list('[img]'):
                            is_in_bb_tag = True
                        elif message[i - 5:i + 1] == list('[/img]'):
                            is_in_bb_tag = False
                    except IndexError:
                        pass
                
                if is_in_bb_tag:
                    i += 1
                    continue

                if message[i:i + len(tag.name) + 2] == list('<{}>'.format(tag.name)):
                    tag.state += 1
                    message = message[:i] + message[i + len(tag.name) + 2:]
                elif message[i:i + len(tag.name) + 3] == list('</{}>'.format(tag.name)):
                    tag.state -= 1
                    message = message[:i] + message[i + len(tag.name) + 3:]
                    
                if tag.state > 0:
                    try:
                        message[i] = tag_target_font[original_font.index(message[i])]
                    except (IndexError, ValueError):
                        pass
                i += 1

        # Normal Transformation
        is_in_bb_tag = False

        for i in range(len(message)):
            if message[i] == '[':
                is_in_bb_tag = True
            elif message[i] == ']':
                is_in_bb_tag = False

                try:
                    if message[i - 4:i + 1] == list('[img]'):
                        is_in_bb_tag = True
                    elif message[i - 5:i + 1] == list('[/img]'):
                        is_in_bb_tag = False
                except IndexError:
                    pass
            
            if not is_in_bb_tag:
                try:
                    message[i] = target_font[original_font.index(message[i])]
                except (IndexError, ValueError):
                    pass
        
        message = str().join(message)
        
        return message
    