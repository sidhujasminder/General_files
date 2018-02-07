{% set val = salt.junos.rpc('get-chassis-inventory') %}
{% set val1 = val['rpc_reply']['chassis-inventory']['chassis']['chassis-module'] %}
show scheduler info:
  {% if val1 %}
  {% for i in val1 %}
  junos:
    - get_table
    - table: SchedulerTable
    - file: schedulerinfo.yml
    - target: i
  {% endfor %}
  {% endif %}
