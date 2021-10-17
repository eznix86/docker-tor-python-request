from utils import change_ip as manager
from utils import bandwidth
import timeit

start_time = timeit.default_timer()


if __name__ == '__main__':
    manager.get_ip()
    ip = manager.get_proxied_ip()
    for x in range(0,5):
        checker = manager.IpChecker(ip)
        with checker.changed_ip() as ip:
            print(ip)

bandwidth.tor_details()

print("\nTime Elapsed :", timeit.default_timer() - start_time, "s")
