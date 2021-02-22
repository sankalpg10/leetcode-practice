from heapq import *
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.socialNetwork = {}
        self.tweets = {}
        self.time = 1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.socialNetwork:
            self.socialNetwork[userId] = {userId}
        if userId not in self.tweets:
            self.tweets[userId] = deque()
        
        self.tweets[userId].appendleft((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId not in self.socialNetwork: return []
        following = self.socialNetwork[userId]
        tweetHeap = []
        print(self.tweets[userId])
        for user in following:
            for time, tweet in self.tweets[user]:
                heappush(tweetHeap, [time, tweet])
                if len(tweetHeap) > 10:
                    heappop(tweetHeap)
        
        tweetHeap.sort(reverse=True)
        feed = [tweet for time, tweet in tweetHeap]
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId: return
        if followerId not in self.socialNetwork:
            self.socialNetwork[followerId] = {followerId}
            self.tweets[followerId] = deque()
        if followeeId not in self.socialNetwork:
            self.socialNetwork[followeeId] = {followeeId}
            self.tweets[followeeId] = deque()
        self.socialNetwork[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId or followerId not in self.socialNetwork: return
        if followeeId in self.socialNetwork[followerId]:
            self.socialNetwork[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
