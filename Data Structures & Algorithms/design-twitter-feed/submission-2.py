from sortedcontainers import SortedSet
import copy
import collections
import heapq

# Elements are automatically kept in sorted order
sorted_set = SortedSet([34, 1, 9, 5, 22])
print(sorted_set)


class Twitter:
    def __init__(self):
        self._relationship_db: dict[int, set[int]] = collections.defaultdict(set)
        self._feed: dict[int, dict[int, list[tuple]]] = collections.defaultdict(lambda: collections.defaultdict(list))
        self._feed_ordered: dict[int, SortedSet[dict]] = collections.defaultdict(lambda: SortedSet(key=lambda x: -x[0]))
        self._posts_db: dict[int, list[tuple]] = collections.defaultdict(list)
        self._timestamp = 0

    def get_ts(self):
        cur = self._timestamp
        self._timestamp += 1
        return cur

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = (self.get_ts(), userId, tweetId)
        self._posts_db[userId].append(tweet)
        self._feed[userId][userId].append(tweet)
        self._feed_ordered[userId].add(tweet)
        followers = self._relationship_db[userId]

        for follower_id in followers:
            if follower_id != userId:
                self._feed_ordered[follower_id].add(tweet)

    def getNewsFeed(self, userId: int) -> list[int]:
        posts = self._feed_ordered[userId][:10]
        return [x[2] for x in posts]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self._relationship_db[followeeId] or followerId == followeeId:
            return 
        self._relationship_db[followeeId].add(followerId)
        # add posts from followId to followerId's feed
        posts = copy.deepcopy(self._posts_db[followeeId])
        for post in posts:
            self._feed_ordered[followerId].add(post)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if not followerId in self._relationship_db[followeeId]:
            return
        self._relationship_db[followeeId].remove(followerId)
        # remove posts from `followeeId`
        to_remove = []
        for post in self._feed_ordered[followerId]:
            if post[1] == followeeId:
                to_remove.append(post)
        for key in to_remove:
            self._feed_ordered[followerId].remove(key)
