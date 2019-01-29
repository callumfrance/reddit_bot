from praw import exceptions
from bot import Bot
import triggers
import responses

def run_bot(b):
    """The subreddit streaming function.

    Will stream comments from a chosen subreddit, check for good match,
    and then process that match using generate_response().
    """
    for comment in b.r.subreddit('me_irl').stream.comments():
        for trig in triggers.all_triggers:
            if trig == comment.body.upper():
                pc = True
                if triggers.all_triggers[trig] in ['good', 'bad']:
                    pc = b.am_i_parent(comment)
                if not pc:
                    print("not parent comment, breaking")
                    continue
                print("\nFound a comment", comment.body)
                if b.check_match(comment):
                    print("A True match was found", ' ', comment, ' ', comment.author)
                    generate_response(comment, triggers.all_triggers[trig])
                continue

def generate_response(comment, comment_type):
    """The 'functionality' of the program.

    Called from run_bot() to provide the 'custom' response.
    """
    to_comment = responses.comment_action(comment_type)
    try:
        comment.reply(to_comment)
        print('reply given')
    except exceptions.APIException as apie:
        if hasattr(apie, 'message'):
            print(apie.message)
        else:
            print("Ratelimit was probably exceeded")
        print('reply not given')

if __name__ == '__main__':
    """The main of the entire program.

    Set heroku or cmd/shell mode.
    Create a reddit object instance.
    Infinitely loop the bot so that it constantly runs.
    """
    on_heroku = True # Simple boolean var which changes login steps
    b = Bot("Pay respects bot", on_heroku)

    print("Commence running")
    while True:
        run_bot(b)
