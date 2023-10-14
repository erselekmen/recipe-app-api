
class Tweet():
    
    def __init__(self, tweet_id, text, comment, like, unlike, repost):
        self.tweet_id = tweet_id
        self.text = text
        self.comment = comment
        self.like = like
        self.unlike = unlike
        self.repost = repost

    def like_increment(self):
        self.like += 1

    def unlike_increment(self):
        self.unlike += 1


class Comment(Tweet):
    
    def __init__(self, comment_id):
        self.comment_id
