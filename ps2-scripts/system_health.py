#!/usr/bin/env python3
import psutil

CPU_THRESHOLD = 0.1
MEM_THRESHOLD = 0.1
DISK_THRESHOLD = 0.1

cpu = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu}%")
if cpu > CPU_THRESHOLD:
    print(f"⚠️ High CPU usage: {cpu}%")

memory = psutil.virtual_memory().percent
print(f"Memory Usage: {memory}%")
if memory > MEM_THRESHOLD:
    print(f"⚠️ High Memory usage: {memory}%")

disk = psutil.disk_usage('/').percent
print(f"Disk Usage: {disk}%")
if disk > DISK_THRESHOLD:
    print(f"⚠️ High Disk usage: {disk}%")

