# Real-Time Process Monitor Web App
A full-stack web application for real-time process monitoring using Flask (Python) on the backend and vanilla JavaScript/HTML on the frontend.

The app provides detailed information about currently running system processes, supports live refresh, sorting, filtering, anomaly detection, and child process tracking.

## Features
- Monitor running system processes
- Display: PID, Name, CPU %, Memory %, Username, Is Child
- Sortable columns (ascending & descending by click)
- Filter by process name (live input field)
- Set auto-refresh interval
- Detect spikes in CPU usage (>50%)
- Identify child processes using PPID

## Architecture
```
process-monitor/
├── monitor.py          # Monitors process data and detects anomalies
├── restapi.py          # Flask app exposing APIs and frontend
├── templates/
│   └── frontend.html   
├── static/            
├── requirements.txt    
└── README.md          
```
## How Sorting and Filtering Work
### Sorting
Click column headers (PID, Name, CPU %, Memory %) to toggle between ascending and descending.
The frontend calls /processes with:
 - sort_by: the selected column
 - order: asc or desc

### Filtering
Live text input filters by process name.
 - Sends filter param in the API call.

## Anomaly Detection
Every 5 seconds (or as configured), the monitor.py checks CPU usage.
If a process’s CPU spikes by more than 50% compared to the last sample, an alert is printed to the console.

## Child Process Detection
Each process includes a ppid field (parent process ID).
If ppid != 0, it's marked as a child process.
Displayed in the table under "Is Child?"
