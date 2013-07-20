Reddit Unhider
==============

A Python script to unhide posts on Reddit. Many users on Reddit routinely hide posts when they are done reading them, resulting in a large amount of hidden posts over time.
If a user wanted to unhide all of their previously hidden posts, they would have to manually click "unhide" on each post: potentially a very time-consuming process.

This script methodically unhides all the hidden posts saved on a user's account. It is designed to be run in the background over time, as the Reddit API limits requests to no more than 30 requests per minute.
By default it does not unhide posts that are less than a day old in order to not affect the daily browsing of users.

**Note:** It looks like Reddit only stores the 450 most recently hidden items anyway, so this tool isn't as useful as I thought it would be.

Dependencies
------------

This script uses [PRAW: The Python Reddit API Wrapper](https://github.com/praw-dev/praw/) to communicate with the Reddit API. It can be installed using `pip` or `easy_install`.
