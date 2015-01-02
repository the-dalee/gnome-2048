import time
import threading


class Timer(object):
    def __init__(self, on_tick):
        self._value = 0
        self._running = False
        self._on_tick = on_tick

    def start(self):
        self._running = True
        timer_thread = threading.Thread(None, self.timer_loop)
        timer_thread.start()

    def stop(self):
        self._running = False

    def reset(self):
        self._value = 0

    def timer_loop(self):
        last_time = time.time()
        while self._running:
            time.sleep(0.1)
            cur_time = time.time()
            if(cur_time - last_time > 1):
                last_time = cur_time
                self._value = self._value + 1
                self._on_tick(self._value)
