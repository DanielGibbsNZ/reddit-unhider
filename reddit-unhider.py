import argparse
import praw
import time

parser = argparse.ArgumentParser(description="A script to unhide posts on Reddit.")
parser.add_argument("-u", "--username", help="Username to log into Reddit with.", action="store")
parser.add_argument("-p", "--password", help="Password to log into Reddit with.", action="store")
parser.add_argument("-d", "--days-to-keep", help="The number of days of posts to not unhide.", type=int, default=1, action="store")
args = parser.parse_args()

if args.days_to_keep < 0:
	args.days_to_keep = 0


reddit = praw.Reddit(user_agent="Reddit-unhider")
reddit.login(args.username, args.password)

time_cutoff = int(time.time()) - (args.days_to_keep * 60 * 60 * 24)
num_hidden = 0
after = None
no_more = False
while not no_more:
	hidden_posts = reddit.user.get_hidden(limit=None, params={"after" : after})
	no_more = True
	for post in hidden_posts:
		no_more = False
		if int(post.created_utc) >= time_cutoff:
			after = "t3_%s" % post.id
			continue
		print "Unhiding [%s] ... " % post.title
		post.unhide()
		num_hidden += 1

print "\n%d posts unhidden!" % num_hidden
