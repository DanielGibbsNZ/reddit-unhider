import praw
import time

username = "Username"
password = "Password"
time_cutoff = int(time.time()) - (60 * 60 * 24)

num_hidden = 0
reddit = praw.Reddit(user_agent = "Reddit-unhider")

print "Logging in..."
reddit.login(username, password)

hidden_posts = reddit.user.get_hidden(limit = None)
for post in hidden_posts:
	if int(post.created_utc) >= time_cutoff:
		continue
	print "Unhiding [%s] ... " % post.title
	post.unhide()
	num_hidden += 1

print "\n%d posts unhidden!" % num_hidden
