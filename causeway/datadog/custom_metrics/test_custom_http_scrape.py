import requests, json, urllib


r = requests.get('https://interact.staging.causeway.com/api/monitors')

# Convert to JSON string
output = r.text

# Convert string to Python dict 
output_dict = json.loads(output) 

# Print vaules
print(output_dict) 
# print(output_dict['freemem']) 
# freememory = output_dict['freemem']
# freememory_split = freememory.split(" ")
# freememory_val = int(freememory_split[0])
# print(freememory)
# print(freememory_split)
# print(freememory_val)


cpu = output_dict['uptime']
cpu_split = cpu.split(" ")
cpu_val = float(cpu_split[0])
print(cpu)
print(cpu_split)
print(cpu_val)




# print(output_dict['cpu'])   
# print(output_dict['status']) 

# status = output_dict['status']
# print(status)

# if status == "up":
#     status_val = 1
# else:
#     status_val = 0    
# print(status_metric)

