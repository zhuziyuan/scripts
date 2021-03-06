#!/usr/bin/python

import json
import subprocess as sp
import sys

nargs = len(sys.argv)

if nargs == 1:
    services = []
    supervisor_services = sp.check_output(["sudo", "supervisorctl", "status"]).decode()
    for line in supervisor_services.splitlines():
        service_name = line.split()[0]
        services.append({"{#SUPERVISOR_SERVICE}": service_name })
    print(json.dumps({'data' : services }))

elif nargs == 3:
    supervisor_service = sys.argv[1]
    service_status = sp.check_output(["sudo", "supervisorctl", "status", supervisor_service]).decode()
    if "(no such process)" in service_status:
        print("Process does not exist")
    else:
        if sys.argv[2] == "uptime":
            service_uptime = service_status.split()[5]
            print(service_uptime)
        elif sys.argv[2] == "state":
            service_state = service_status.split()[1]
            if service_state == "RUNNING":
                print("1")
            elif service_state == "STOPPED":
                print("0")
            else:
                print("10")
        else:
            print("Wrong Argument")
else:
    print("Wrong")

