import time
from collections import deque
from threading import Lock

class TokenBucket:
    def __init__(self,capacity,fill_rate):
        self.capacity=float(capacity)
        self.fill_rate=fill_rate
        self.tokens=float(capacity)
        self.timestamp=time.time()
        self.lock=Lock()

    def consume(self,tokens):
        print("Token Bucket Algorithm ")
        with self.lock:
            if tokens<=self.tokens:
                self.tokens-=tokens
                return True
            return False
    
    def refill(self):
        with self.lock:
            now=time.time()
            delta=self.fill_rate*(now-self.timestamp)
            self.tokens=min(self.capacity,self.tokens+delta)
            self.timestamp=now


class SlidingWindow:
    def __init__(self,capacity,window_size):
        self.capacity=capacity
        self.window_size=window_size
        self.timestamps=deque()
        self.lock=Lock()

    def consume(self):
        with self.lock:
            now=time.time()
            print(f"Sliding Bucket inside")
            while self.timestamps and now-self.timestamps[0] >self.window_size:
                self.timestamps.popleft()
            if len(self.timestamps) <self.capacity:
                self.timestamps.append(now)
                return True
            return False


        






class LoadBalancer:
    def __init__(self,token_bucket,sliding_window):
        self.token_bucket=token_bucket
        self.sliding_window=sliding_window
    
    def handle_request(self):
        self.token_bucket.refill()
        if not self.token_bucket.consume(1):
            raise Exception("Token Bucket capacity exceeded!")
        if not self.sliding_window.consume():
            raise Exception("Sliding window capacity exceeded")

token_bucket=TokenBucket(100,10)
sliding_window=SlidingWindow(100,60)
load_balancer=LoadBalancer(token_bucket,sliding_window)


while True:
    try:
        load_balancer.handle_request()
        print("Request Handled succesfully!")
    except Exception as e:
        print(str(e))
        time.sleep(1)