# Python API for Openmediavault

Based on [python-synology](https://github.com/StaticCube/python-synology) by [FG van Zeelst StaticCube](https://github.com/StaticCube/)

-----
## Installation (soon)
```sh
git clone https://github.com/orrpan/python-openmediavault.git
cd python-openmediavault
[sudo] pip install setup.py
```
-----
## Usage

### Module
------

You can import the module as `Openmediavault`.

```python

    from Openmediavault import Openmediavault

    print("Creating Valid API")
    api = Openmediavault("<OpenmediavaultIp>", "<OpenmediavaultPort>", "<Username>", "<Password>")

    print("=== Utilisation ===")
    print("CPU Load:   " + str(api.utilisation.cpu_total_load) + " %")
    print("Memory Use: " + str(api.utilisation.memory_real_usage) + " %")
    print("Net Up:     " + str(api.utilisation.network_up()))
    print("Net Down:   " + str(api.utilisation.network_down()))
    
    print("=== Storage ===")
    volumes = api.storage.volumes
    for volume in volumes:
        print("ID:         " + str(volume))
        print("Status:     " + str(api.storage.volume_status(volume)))
        print("% Used:     " + str(api.storage.volume_percentage_used(volume)) + " %")

    disks = api.storage.disks
    for disk in disks:
        print("ID:         " + str(disk))
        print("Name:       " + str(api.storage.disk_name(disk)))
        print("S-Status:   " + str(api.storage.disk_smart_status(disk)))
        print("Status:     " + str(api.storage.disk_status(disk)))
        print("Temp:       " + str(api.storage.disk_temp(disk)))
```

## Credits / Special Thanks
- https://github.com/StaticCube (forked from)
- https://github.com/florianeinfalt
- https://github.com/tchellomello
