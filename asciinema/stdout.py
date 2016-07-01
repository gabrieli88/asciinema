import time
import codecs


class Stdout:

    def __init__(self, max_wait=None):
        self.frames = []
        self.max_wait = max_wait
        self.last_write_time = time.time()
        self.duration = 0
        self.decoder = codecs.getincrementaldecoder('UTF-8')('replace')

    def write(self, data):
        text = self.decoder.decode(data)
        if text:
            delay = self._increment_elapsed_time()
            self.frames.append([delay, text])

        return len(data)

    def close(self):
        self._increment_elapsed_time()

    def _increment_elapsed_time(self):
        # delay = int(delay * 1000000) / 1000000.0 # millisecond precission
        now = time.time()
        delay = now - self.last_write_time

        if self.max_wait and delay > self.max_wait:
            delay = self.max_wait

        self.duration += delay
        self.last_write_time = now

        return delay
