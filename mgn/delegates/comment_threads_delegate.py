from flask import json
from mgn.repository.comment_thread_repository import CommentThreadsRepository


class CommentThreadsDelegate:
    comment_threads = None

    def __init__(self, comment_thread_id=None):
        self.comment_threads = CommentThreadsRepository(comment_thread_id)

    def add(self):
        result = self.comment_threads.add()
        return result

    def get(self):
        result = self.comment_threads.get()
        if result is not None:
            return json.dumps(result.serialize)
        return result
