import wmi


def avg(value_list):
    num = 0
    length = len(value_list)
    for val in value_list:
        num += val
    return num / length


w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
sensors = w.Sensor()
cpu_temps = []
gpu_temp = 0
for sensor in sensors:
    if sensor.SensorType == u'Temperature' and not 'GPU' in sensor.Name:
        cpu_temps += [float(sensor.Value)]
    elif sensor.SensorType == u'Temperature' and 'GPU' in sensor.Name:
        gpu_temp = sensor.Value
print
"Avg CPU: {}".format(avg(cpu_temps))
print
"GPU: {}".format(gpu_temp)