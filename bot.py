"""Helpful information for this bot.

https://gist.github.com/hzsweers/8595628

Heroku commands:
    heroku ps:scale worker=1
    heroku ps
    heroku logs
"""

# Author: callumfrance

import praw # the reddit bot library
import os   # library for interfacing with the operating system
import config # this is a file I wrote that contains credentials
from time import sleep # used to add a small delay in the program

class Bot:
    """This is a generic bot class that has some functionality that could be
    applied to multiple kinds of bots.

    - the login sequence
    - the storage method of comment checking
    - the comment tree method of comment checking
    """
    def __init__(self, user_agent_in, running_on_heroku):
        """The init creates the bot class.
        """
        self.r = []
        self.comments_replied_to = []
        self.bot_login(user_agent_in, running_on_heroku)
        self.comments_replied_to_init()

    def bot_login(self, user_agent_in, running_on_heroku):
        """Allow the bot to log in to, and operate in Reddit.

           Requires environment variables if running on Heroku.
           Otherwise, use a config file to log in from cmd or shell
        """
        if running_on_heroku:
            self.r = praw.Reddit(username=os.environ['REDDIT_USERNAME'],
                            password=os.environ['REDDIT_PASSWORD'],
                            client_id=os.environ['REDDIT_CLIENT_ID'],
                            client_secret=os.environ['REDDIT_CLIENT_SECRET'],
                            user_agent=user_agent_in)
        else:
            self.r = praw.Reddit(username=config.username,
                            password=config.password,
                            client_id=config.client_id,
                            client_secret=config.client_secret,
                            user_agent=user_agent_in)

    def comments_replied_to_init(self):
        """Loads in comments #'s from text file when the bot is initialised.

           If there is no text file, create empty list and create text file.
           In practicality, this function does NOT work on Heroku. This is
           because Heroku does not store dynamically generated content, so
           replied.txt is only updated when the bot is being used in
           cmd / shell mode, and not heroku mode.
        """
        if not os.path.isfile("replied.txt"):
            self.comments_replied_to = [' ',]
            with open("replied.txt", "a") as f:
                pass
        else:
            with open("replied.txt", "r") as f:
                self.comments_replied_to = f.read()
                self.comments_replied_to = self.comments_replied_to.split("\n")

    def check_match(self, in_comment):
        """This function ensures that the bot does not reply to comments that it
        has already replied to, or comments that it made.

        This uses imported values from 'replied.txt' as well as observing the
        reddit page's content to determine when to reply.
        """
        if (in_comment.id not in self.comments_replied_to) and \
                (in_comment.author != self.r.user.me()):
                    try:
                        sleep(2)
                        in_comment.refresh() # When checking comment info, always refresh a it first
                    except praw.exceptions.ClientException:
                        print("Praw Client Exception, skipping comment")
                        return False
                    print(len(in_comment.replies), "length of in comment replies")
                    for top_rep in in_comment.replies:
                        print(top_rep, "top rep", top_rep.author, "top rep author")
                        if top_rep.author is self.r.user.me():
                            print("I am the author of this reply so False")
                            return False
                    print("I did not author any replies so True")
                    self.comments_replied_to.append(in_comment.id)
                    with open("replied.txt", "a") as f:
                        f.write(in_comment.id + "\n")
                    return True
        else:
            print("comment was not a fresh match")
            return False

    def am_i_parent(self, in_comment):
        """This function determines if the parent of a given comment is the bot."""
        parent_comment = in_comment.parent()
        parent_comment.refresh() # When checking comment info, always refresh a it first
        print(parent_comment.author, self.r.user.me())
        if parent_comment.author == self.r.user.me():
            print("I authored this comment's parent")
            return True
        else:
            print("Parent was ", parent_comment.author)
            return False
