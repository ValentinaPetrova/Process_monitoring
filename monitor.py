import psutil
import time
import threading
from collections import defaultdict

class ProcessMonitor:
    def __init__(self, interval=5):
        self.interval = interval
        self.process_data = []
        self.previous_cpu = defaultdict(float)
        self.current_alerts = []

    def fetch_processes(self):
        process_list = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'ppid']):
            try:
                pinfo = proc.info
                pinfo['is_child'] = pinfo['ppid'] != 0
                process_list.append(pinfo)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return process_list

    def detect_anomalies(self, processes):
        alerts = []
        for p in processes:
            pid = p['pid']
            cpu = p['cpu_percent']
            mem = p['memory_percent']
            if cpu - self.previous_cpu[pid] > 50:
                alerts.append(f"High CPU spike detected in PID {pid} ({p['name']})")
            self.previous_cpu[pid] = cpu
        
        self.recent_alerts = alerts
        return alerts

    def update(self):
        while True:
            self.process_data = self.fetch_processes()
            alerts = self.detect_anomalies(self.process_data)
            if alerts:
                for alert in alerts:
                    print("ALERT:", alert)
            time.sleep(self.interval)
            self.current_alerts = alerts

    def start(self):
        threading.Thread(target=self.update, daemon=True).start()

monitor = ProcessMonitor()
monitor.start()
