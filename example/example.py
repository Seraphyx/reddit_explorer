import praw
import pprint

# See: https://github.com/wlindner/python-reddit-scraper/blob/master/scraper.py


# uses environment variables
# http://praw.readthedocs.io/en/latest/getting_started/configuration/environment_variables.html
reddit = praw.Reddit(
	client_id='client_id',
	client_secret='client_secret',
	password='password',
	user_agent='project_name by /u/username',
	username='username')


def main():

	print ('logged in to Reddit as: ' + str(reddit.user.me()))

	subreddit = reddit.subreddit('Showerthoughts')
	# for index, submission in enumerate(subreddit.submissions()):
	# 	if index % 100 == 0 and index > 0: print(str(index) + ' inserted so far')
	# 	print(submission)
	for submission in reddit.subreddit('learnpython').hot(limit=10):
		print(submission.title)


if __name__ == '__main__':
	# main()
	# print(reddit.user.me())
	# print(reddit.read_only)

	user = reddit.redditor('Makirole')
	print(user.link_karma)
	print(vars(user).keys())
	print('user.comments')
	print(vars(user.comments).keys())
	print('user.comments === LOOP')
	for index, comment in enumerate(user.comments.new()):
	    print('============================= ' + str(index))
	    print(':::: %s' % comment.subreddit)
	    print(comment.body)
	    ckeys = vars(comment).keys()

	pprint.pprint(ckeys)