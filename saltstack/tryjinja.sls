{% for i in grains['FPCONLINE'] %}
show scheduler info for fpc {{ i }}:
  junos:
    - get_table
    - table: FPCMemory
    - file: fpcmemory.yml
    - target: fpc{{ i }}

{% endfor %}
