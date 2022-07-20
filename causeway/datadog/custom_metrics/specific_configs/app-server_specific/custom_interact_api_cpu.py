from datadog_checks.checks import AgentCheck
import requests, json, urllib

class interact_api_cpu(AgentCheck):
  def check(self, instance):
    r = requests.get('https://interact.staging.causeway.com/api/monitors')

    # Convert to JSON string
    output = r.text

    # Convert string to Python dict 
    output_dict = json.loads(output) 

    # Process vaules  
    cpu = output_dict['cpu']
    cpu_split = cpu.split(" ")
    cpu_val = float(cpu_split[0])
    self.count('external.interact_api.cpu', cpu_val)