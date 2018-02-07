{% set val = salt.junos.rpc('get-chassis-inventory') %}
{% set val1 = val['rpc_reply']['chassis-inventory']['chassis']['chassis-module'] %}
{% for instance in val1 %}
{% if instance is mapping %}
{% if 'FPC' in instance['name'] %}
show scheduler info for {{ instance['name'].lower().replace(' ', '') }}:
  junos:
    - get_table
    - table: SchedulerTable
    - file: schedulerinfo.yml
    - target: {{ instance['name'].lower().replace(' ', '') }}
  {% endif %}
  {% endif %}
  {% endfor %}
