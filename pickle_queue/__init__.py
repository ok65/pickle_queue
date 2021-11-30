
# Library imports
from multiprocessing import Pipe
from queue import Empty


class PickleQueue:

    def __init__(self):
        self._get_pipe, self._put_pipe = Pipe()

    def put(self, obj):
        self._put_pipe.send(obj)

    def get(self, blocking=False):
        if not blocking and not self._get_pipe.poll():
            raise Empty
        return self._get_pipe.recv()
