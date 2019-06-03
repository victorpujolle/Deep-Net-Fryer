import praw

reddit = praw.Reddit(client_id='jY4RL92sf7AVSA',
                     client_secret='uSWci46GVGSdnCkBwMvpvzxw-K4',
                     username='Arnaudp44',
                     password='sxks*63k',
                     user_agent='prawFetcher')

subreddit = reddit.subreddit('Dankmemes')

hot_python = subreddit.hot(limit=10)

# for submission in hot_python:
#
#     # dir_sub = dir(submission)
#
#     if not submission.stickied:
#         print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title,
#                                                                                submission.ups,
#                                                                                submission.downs,
#                                                                                submission.visited))


top_all = subreddit.top('all', limit=10)
for submission in top_all:
    if not submission.stickied:
        print('Title: {}, ups: {}, downs: {}, Have we visited?: {}'.format(submission.title,
                                                                               submission.ups,
                                                                               submission.downs,
                                                                               submission.visited))
