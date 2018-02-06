{% for i in grains['FPCONLINE'] %}
get fpcmemory for fpc {{ i }}:
  schedule.present:
  - function: junos.get_table
  - job_args:
    - FPCMemory
    - fpcmemory.yml
  - job_kwargs:
      target: fpc{{ i }}  
  - splay: 10
  - seconds: 10
  - returner: iagent_influxdb
{% endfor %}
