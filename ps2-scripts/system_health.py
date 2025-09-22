#!/usr/bin/env python3
import psutil
import logging

# ------------------------------
# Set Thresholds
# ------------------------------
CPU_THRESHOLD = 80      # %
MEM_THRESHOLD = 80      # %
DISK_THRESHOLD = 80     # %
PROCESS_THRESHOLD = 150 # number of processes

# ------------------------------
# Setup Logging
# ------------------------------
logging.basicConfig(
    filename='system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def alert(message):
    print(message)
    logging.warning(message)

# ------------------------------
# Check CPU Usage
# ------------------------------
cpu = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu}%")
if cpu > CPU_THRESHOLD:
    alert(f"⚠️ High CPU usage: {cpu}%")

# ------------------------------
# Check Memory Usage
# ------------------------------
memory = psutil.virtual_memory().percent
print(f"Memory Usage: {memory}%")
if memory > MEM_THRESHOLD:
    alert(f"⚠️ High Memory usage: {memory}%")

# ------------------------------
# Check Disk Usage
# ------------------------------
disk = psutil.disk_usage('/').percent
print(f"Disk Usage: {disk}%")
if disk > DISK_THRESHOLD:
    alert(f"⚠️ High Disk usage: {disk}%")

# ------------------------------
# Check Running Processes
# ------------------------------
process_count = len(psutil.pids())
print(f"Running processes: {process_count}")
if process_count > PROCESS_THRESHOLD:
    alert(f"⚠️ High number of running processes: {process_count}")

