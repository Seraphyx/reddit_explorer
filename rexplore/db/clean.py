import collections
from functools import reduce
from datetime import datetime


def clean_user(user):
	'''
	arg:
		user: reddit.redditor('<username>')
	'''
	out = collections.OrderedDict()

	out['id'] = user.id
	out['name'] = user.name
	# out['icon_img'] = user.icon_img

	out['pull_ts'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
	out['created_utc'] = datetime.utcfromtimestamp(user.created_utc).strftime('%Y-%m-%d %H:%M:%S')

	out['link_karma'] = user.link_karma
	out['comment_karma'] = user.comment_karma

	out['is_employee'] = user.is_employee
	out['is_mod'] = user.is_mod
	out['verified'] = user.verified

	return out

def getattr_deep(obj, attr, default=''):
	if obj is None:
		return default
	attr_list = attr.split('.')
	
	if attr_list[0] in vars(obj).keys():
		obj = getattr(obj, attr_list[0])
	else:
		return default

	if len(attr_list) == 1:
		return obj
	else:
		return getattr_deep(obj, '.'.join(attr_list[1:]))



def clean_comment(comment):

	out = collections.OrderedDict()

	def parse_author_id(comment):
		obj = getattr(comment, 'author', None)
		if obj is None:
			return ''

		print(vars(obj).keys())
		print(str(obj))
		print(type(obj.name))

		if 'id' in vars(obj).keys():
			return getattr(obj, 'id', '')
		return ''

	def parse_author_name(comment):
		obj = getattr(comment, 'author', None)
		if obj is None:
			return ''

		print(vars(obj).keys())
		print(str(obj))
		print(type(obj.name))

		if 'id' in vars(obj).keys():
			return getattr(obj, 'name', '')
		return ''

	def deepgetattr(obj, attr):
		"""Recurses through an attribute chain to get the ultimate value."""
		return reduce(getattr, attr.split('.'), obj)




	out['id'] = comment.id

	out['author'] 			= getattr_deep(comment, 'author.name')
	out['author_id'] 		= getattr_deep(comment, 'author.id')
	out['name'] 			= getattr_deep(comment, 'name', '')
	out['parent_id'] 		= getattr_deep(comment, 'parent_id', '')
	out['link_id'] 			= getattr_deep(comment, 'link_id', '')
	# out['subreddit'] = comment.subreddit.display_name
	out['subreddit_id'] 	= getattr_deep(comment, 'subreddit.id', '')
	# out['permalink'] = comment.permalink

	out['pull_ts'] 			= datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
	out['created_utc'] 		= datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S')

	out['depth'] 			= getattr_deep(comment, 'depth', 0)
	out['edited'] 			= getattr_deep(comment, 'edited', False)
	out['gilded'] 			= getattr_deep(comment, 'gilded', False)

	out['score'] 			= getattr_deep(comment, 'score', 0)
	out['ups'] 				= getattr_deep(comment, 'ups', 0)
	out['downs'] 			= getattr_deep(comment, 'downs', 0)
	out['controversiality'] = getattr_deep(comment, 'controversiality', 0)
	out['score_hidden'] 	= getattr_deep(comment, 'score_hidden', False)
	out['collapsed'] 		= getattr_deep(comment, 'collapsed', False)

	out['body'] 			= getattr_deep(comment, 'body')

	return out


if __name__ == '__main__':

	v = ",".join(["%s"] * 3)
	print(v)

	v = v.split(',')
	print(v)
	print(len(v))
	print(v[1:])
	print(len(v[1:]))
	print('.'.join(v[1:]))