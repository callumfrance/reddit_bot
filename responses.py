"""This file simply contains all of the bots possible responses to a comment.
"""

from random import randint # Used to generate a random response

all_types = (
        'normal',
        'big',
        'good',
        'bad',
        )

'''
==================
"Normal" responses
==================
'''
big_f_str = '+73 respects paid({})'

hstr = '[+1 respect paid]({})'

images = [
        "https://imgur.com/cvHBBLg",
        "https://imgur.com/Zd0Ydl2",
        "https://imgur.com/KD5Da6Q",
        "https://imgur.com/xWgjvmn",
        "https://imgur.com/cTNAqXR",
        "https://imgur.com/rkVbZrC",
        "https://imgur.com/WahbrgW",
        "https://imgur.com/oRcCbSq",
        "https://imgur.com/f43C1A8",
        # "https://imgur.com/7rrvGCJ",
        "https://imgur.com/A5ztGfY",
        "https://imgur.com/Gs0WfTQ",
        "https://imgur.com/jF3OjVA",
        "https://imgur.com/fFejZQ1",
        "https://imgur.com/mrvs6Mp",
        "https://imgur.com/yas7WUf",
        "https://imgur.com/lf43Dc6",
        "https://imgur.com/ZkfLxu3",
    ]


'''
====================
"Good bot" responses
====================
'''

respect_str = 'nice\n\n{}'

respect_images = [
        '[Here, have this fun celery snack I made for you](https://imgur.com/50Mg8a7)',
        '[Help yourself to some slices from my apple](https://imgur.com/Ba0F2VS)',
        '[I made you a banana banger. You don\'t have to have it if you don\'t want it.](https://imgur.com/VZcog2H)',
        '[I thought you might be thirsty so I got you a cup of tap water](https://imgur.com/nhtGuRr)',
        '[You can have a couple of my sultanas if you want](https://imgur.com/CFeVzOd)',
        ]


'''
===================
"Bad bot" responses
===================
'''

disrespect_str = [
        '[dab on the haters]',
        '[F]',
        '[i guess you could say this redditor does not pay their respects forward]',
        '[-1 respect paid]',
        '[not like this]',
        ]

disrespect_images = [
        "(https://imgur.com/Spra3ro)",
        "(https://imgur.com/qR5j41M)",
        "(https://imgur.com/8cKGzSH)",
        "(https://imgur.com/705IVIO)",
        ]

'''
========================================
Behaviour upon landing on a comment type
========================================
'''
def rand_image(size):
    """A function to return a random integer based on the size of the variable."""
    return randint(1, size)

def comment_action(comment_type):
    """Used to determine what kind of response is given.

    Returns the comment string.
    """
    final_comment = ''
    if comment_type == all_types[0]:
        a = rand_image(len(images))
        final_comment =  hstr.format(images[a - 1])
    elif comment_type == all_types[1]:
        a = rand_image(len(images))
        final_comment = big_f_str.format(images[a - 1])
    elif comment_type == all_types[2]:
        a = rand_image(len(respect_images))
        final_comment = respect_str.format(respect_images[a - 1])
    elif comment_type == all_types[3]:
        a = rand_image(len(disrespect_str))
        b = rand_image(len(disrespect_images))
        final_comment = disrespect_str[a - 1] + disrespect_images[b - 1]
    else:
        print("Invalid comment type")

    return final_comment

