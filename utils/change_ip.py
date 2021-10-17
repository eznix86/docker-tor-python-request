import functools
from contextlib import contextmanager
import requests
import time
from utils import tor

def get_ip(proxies=None, headers=None):
    r = requests.get("http://icanhazip.com", proxies=proxies, headers=headers)
    return r.text


proxies = {
  "http": "http://localhost:8118"
}

headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11'
}

get_proxied_ip = functools.partial(get_ip, proxies, headers)

class IpChecker:
  
  def __init__(self, previous_ip) -> None:
      self.previous_ip = previous_ip

  def _has_ip_changed(self) -> bool:
    time.sleep(0.5)
    self.current_ip = get_proxied_ip()
    return self.previous_ip != self.current_ip

  def _wait_for_ip_change(self):
     while True:
        time.sleep(0.5)
        if self._has_ip_changed():
          self.previous_ip = self.current_ip
          break

  @contextmanager
  def changed_ip(self):
    try:
      tor.change_ip()
      self._wait_for_ip_change()
      yield self.previous_ip
    finally:
      pass

