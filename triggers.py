"""This file simply contains all of the bots possible triggers for a comment.
"""

f_triggers = {
        "F" : 'normal',
        "*F*" : 'normal',
        "_F_" : 'normal',
        "**F**" : 'normal',
        "__F__" : 'normal',
        "#F" : 'normal',
        "##F" : 'normal',
        "###F" : 'normal',
        "####F" : 'normal',
        "#####F" : 'normal',
        "######F" : 'normal',
    }

# The below trigger was scrapped because it didn't work in practice
bf = \
"FFFFFFFFFFFFF\n" + \
"FFFFFFFFFFFFF\n" + \
"FFF\n" + \
"FFF\n" + \
"FFFFFFFFFFFFF\n" + \
"FFFFFFFFFFFFF\n" + \
"FFF\n" + \
"FFF\n" + \
"FFF\n" + \
"FFF\n" + \
"FFF"

big_f = dict()
big_f[bf] = 'big'

disrespect = {
        "BAD BOT" : 'bad',
        "BAD BOT." : 'bad',
        }

respect = {
        "GOOD BOT" : 'good',
        "GOOD BOT." : 'good',
        }

all_triggers = {
        **f_triggers,
        **big_f,
        **disrespect,
        **respect,
        }


if __name__ == '__main__':
    print(big_f)
    print("all_triggers:\n\n", all_triggers)
