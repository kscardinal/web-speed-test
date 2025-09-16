from pythonping import ping
from icecream import ic

response_list = ping('8.8.8.8', count=4)  # Send 4 pings
print(response_list.rtt_avg_ms)  # Average round-trip time in ms

ic(ping('8.8.8.8', count=4, size=36, interval=0.1))

ic(ping('8.8.8.8', count=1, size=36))