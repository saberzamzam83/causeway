from datadog_checks.checks import AgentCheck
import requests, json, urllib

class interact_api_status(AgentCheck):
  def check(self, instance):
    r = requests.get('https://interact.staging.causeway.com/api/monitors')

    # Convert to JSON string
    output = r.text

    # Convert string to Python dict 
    output_dict = json.loads(output) 

    status = output_dict['status']

    if status == "up":
       status_val = 1
    else:
       status_val = 0    
    
    self.count('external.interact_api.status', status_val)