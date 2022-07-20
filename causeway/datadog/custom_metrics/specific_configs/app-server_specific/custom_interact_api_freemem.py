from datadog_checks.checks import AgentCheck
import requests, json, urllib

class interact_api_freemem(AgentCheck):
  def check(self, instance):
    r = requests.get('https://interact.staging.causeway.com/api/monitors')

    # Convert to JSON string
    output = r.text

    # Convert string to Python dict 
    output_dict = json.loads(output) 

    # Process vaules  
    freememory = output_dict['freemem']
    freememory_split = freememory.split(" ")
    freememory_val = int(freememory_split[0])
    self.count('external.interact_api.free_memory', freememory_val)