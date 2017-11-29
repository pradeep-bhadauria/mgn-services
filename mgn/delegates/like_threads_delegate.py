from flask import json
from mgn.repository.like_threads_repository import LikeThreadsRepository


class LikeThreadsDelegate:
    like_threads = None

    def __init__(self, like_thread_id=None):
        self.like_threads = LikeThreadsRepository(like_thread_id)

    def add(self):
        result = self.like_threads.add()
        return result

    def get(self):
        result = self.like_threads.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result