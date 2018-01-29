import praw
import pprint
import configparser
import time 

from pprint import pprint

from rexplore import db

import uuid

# See: https://github.com/wlindner/python-reddit-scraper/blob/master/scraper.py

'''
How to insert

User:
	init = db.initialize('../config/config.ini')
	init.insert_user(user)

'''


# uses environment variables
# http://praw.readthedocs.io/en/latest/getting_started/configuration/environment_variables.html
reddit = praw.Reddit('myapp', user_agent='myapp user agent')

def config():
	config = configparser.ConfigParser()
	config.read('config.ini')
	return config


def main():

	print ('logged in to Reddit as: ' + str(reddit.user.me()))

	subreddit = reddit.subreddit('Showerthoughts')
	# for index, submission in enumerate(subreddit.submissions()):
	# 	if index % 100 == 0 and index > 0: print(str(index) + ' inserted so far')
	# 	print(submission)
	for submission in reddit.subreddit('learnpython').hot(limit=10):
		print(submission.title)



def test():

	print(vars(reddit))

	# (1) List of all popular subreddits
	subreddits = reddit.subreddits.popular()
	for subreddit in subreddits:
		print(subreddit)

	# (2) List of all posts in a subreddit
	subreddit = reddit.subreddit('overwatch')


	# (3) List of all users from the posts


	# (4) List of all posts from user

	user = reddit.redditor('Makirole')
	print('===============')
	'''
	{'_fetched': True,
	 '_info_params': {},
	 '_mod': None,
	 '_reddit': <praw.reddit.Reddit object at 0x0000026D6FC2DA20>,
	 '_replies': <praw.models.comment_forest.CommentForest object at 0x0000026D7212CFD0>,
	 '_submission': Submission(id='5623n2'),
	 'approved_at_utc': None,
	 'approved_by': None,
	 'archived': True,
	 'author': Redditor(name='chaoscontrol91'),
	 'author_flair_css_class': None,
	 'author_flair_text': None,
	 'banned_at_utc': None,
	 'banned_by': None,
	 'body': 'I like this a lot better. ',
	 'body_html': '<div class="md"><p>I like this a lot better. </p>\n</div>',
	 'can_gild': True,
	 'can_mod_post': False,
	 'collapsed': False,
	 'collapsed_reason': None,
	 'controversiality': 0,
	 'created': 1475744159.0,
	 'created_utc': 1475715359.0,
	 'depth': 0,
	 'distinguished': None,
	 'downs': 0,
	 'edited': False,
	 'gilded': 0,
	 'id': 'd8ftv3d',
	 'is_submitter': False,
	 'likes': None,
	 'link_id': 't3_5623n2',
	 'mod_note': None,
	 'mod_reason_by': None,
	 'mod_reason_title': None,
	 'mod_reports': [],
	 'name': 't1_d8ftv3d',
	 'num_reports': None,
	 'parent_id': 't3_5623n2',
	 'permalink': '/r/Overwatch/comments/5623n2/real_hanzo_with_a_twist/d8ftv3d/',
	 'removal_reason': None,
	 'report_reasons': None,
	 'saved': False,
	 'score': 8,
	 'score_hidden': False,
	 'stickied': False,
	 'subreddit': Subreddit(display_name='Overwatch'),
	 'subreddit_id': 't5_2u5kl',
	 'subreddit_name_prefixed': 'r/Overwatch',
	 'subreddit_type': 'public',
	 'ups': 8,
	 'user_reports': []}
	'''
	print(user._path)
	print('===============')

	# user_values = db.clean_user(user)
	# pprint(user_values)


	#===== Insert user
	init = db.initialize('../config/config.ini')
	init.insert_user(user)


	post = reddit.submission(id='5623n2')
	print('post=====================================================')
	print('post=====================================================')
	print('post=====================================================')
	print(post)
	pprint(vars(post))
	print(len(post.comments))
	print(post.comments[0])
	comment = post.comments[2]

	print('post=====================================================')
	print('post=====================================================')
	print('post=====================================================')
	pprint(vars(comment))



	#===== Insert Comment
	# init.insert_comment(comment)

	# print(comment.id)
	# for reply_i, reply in enumerate(comment._replies):
	# 	print(len(reply._replies))
	# 	print('\treply = %d [depth=%d][id=%s][parent=%s]' % (reply_i, reply.depth, reply.id, reply.parent_id))
	# 	for reply_2_i, reply_2 in enumerate(reply._replies):
	# 		print(len(reply_2._replies))
	# 		print('\t\treply = %d [depth=%d][id=%s][parent=%s]' % (reply_2_i, reply_2.depth, reply_2.id, reply_2.parent_id))

	# print(len(comment._replies))

	def comment_recursive(comment_obj):
		for reply_i, reply in enumerate(comment_obj._replies):
			print(('\t' * reply.depth) + 'reply = %d [depth=%d][id=%s][parent=%s][replies=%d]' % (reply_i, reply.depth, reply.id, reply.parent_id, len(reply._replies)))
			init.insert_comment(reply)
			if len(reply._replies) > 0:
				comment_recursive(reply)



	post.comments.replace_more(limit=None)
	for comment_i, comment in enumerate(post.comments):
		print("===== Comment #%d" % comment_i)
		comment_recursive(comment)


	# values_dict = db.clean_comment(comment)
	# print(values_dict)


	# for comment in post.comments:
	# 	print(comment)
	# 	pprint(vars(comment))


	# print('user.comments')
	# print(vars(user.comments).keys())
	# print('user.comments === LOOP')
	# for index, comment in enumerate(user.comments.new()):
	#     print('============================= ' + str(index))
	#     print(':::: %s' % comment.subreddit)
	#     print(comment.body)
	    # ckeys = vars(comment).keys()



if __name__ == '__main__':
	# main()
	test()

	# print(getattr({}, 'a', None))



	# key = uuid.uuid4()
	# print(key)
	# print(type(key))
	# print('inserting', repr(key.bytes))
	# print('INSERT INTO xyz (id) VALUES (%s)', key.bytes)
	# print("""A single line string literal""" == "A single line string literal")
	# print("""A single line stri"ng literal""")

	# test = {'a':1, 'b': 'wefwaf'}

	# test1 = [t for t, k in test.items()]
	# print(test1)
	# print(tuple(test1))

