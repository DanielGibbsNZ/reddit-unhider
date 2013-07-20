import praw
import time

username = "Username"
password = "Password"
days_to_keep = 1

time_cutoff = int(time.time()) - (days_to_keep * 60 * 60 * 24)
num_hidden = 0
after = None
reddit = praw.Reddit(user_agent="Reddit-unhider")

print "Logging in..."
reddit.login(username, password)

no_more = False
while not no_more:
	hidden_posts = reddit.user.get_hidden(limit=None, params={"after" : after})
	no_more = True
	for post in hidden_posts:
		no_more = False
		if int(post.created_utc) >= time_cutoff:
			after = post.id
			continue
		print "Unhiding [%s] ... " % post.title
		post.unhide()
		num_hidden += 1

print "\n%d posts unhidden!" % num_hidden
