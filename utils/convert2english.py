def convert_to_english(text):
    mapping = {
        'آ': 'A',
        'ا': 'A',
        'ب': 'B',
        'پ': 'P',
        'ت': 'T',
        'ث': 'S',
        'ج': 'J',
        'چ': 'CH',
        'ح': 'H',
        'خ': 'KH',
        'د': 'D',
        'ذ': 'Z',
        'ر': 'R',
        'ز': 'Z',
        'س': 'S',
        'ش': 'SH',
        'ص': 'S',
        'ض': 'Z',
        'ط': 'T',
        'ظ': 'Z',
        'ع': 'E',
        'غ': 'G',
        'ف': 'F',
        'ق': 'G',
        'ک': 'K',
        'گ': 'G',
        'ل': 'L',
        'م': 'M',
        'ن': 'N',
        'و': 'V',
        'ه': 'H',
        'ی': 'Y',
        ' ': ' ',  # preserve spaces
    }

    english_text = ''
    for char in text:
        if char in mapping:
            english_text += mapping[char]
        else:
            english_text += char  # preserve characters not in the mapping

    return english_text

# Test the function
texts = ['کف زمینی', 'بدنه چپ', 'تعداد طبقات', 'L-تعداد# طبقات']
for text in texts:
    print(f'Original text: {text}')
    print(f'English text: {convert_to_english(text)}')
    print()
