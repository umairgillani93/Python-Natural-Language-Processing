import praw
import math
from textblob import TextBlob

reddit = praw.Reddit(client_id = 'aT88p5tNrDVaag', client_secret = 'T6w909sG6HBUUrQz6ZtmwyUuT2c',
                    user_agent = 'subSentiment')

print(reddit)
# open file with subreddit names

with open('sb.txt') as f:

    for line in f:
        subreddit = reddit.subreddit(line.strip())
        # write web agent to get converter for datetime to epoch on a daily basis for updates
        day_start = 1510635601
        day_end = 1510721999

        sub_submissions = subreddit.submissions(day_start, day_end)

        sub_sentiment = 0
        num_comments = 0

        for submission in sub_submissions:
            if not submission.stickied:
                submission.comments.replace_more(limit=0)
                for comment in submission.comments.list():
                        blob = TextBlob(comment.body)
