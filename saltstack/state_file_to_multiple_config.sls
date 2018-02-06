{% set result = salt['junos.rpc']('get-interface-information','','json') %}
{% for iface in result['rpc_reply']['interface-information'][0]['physical-interface'] %}
{% if iface['admin-status'][0]['data'] == 'down' %}
name_{{ iface['name'][0]['data'] }}:
  file.copy:
    - name: /srv/salt/interface_up_{{ iface['name'][0]['data'].replace('/','_')}}_file.set
    - source: /srv/salt/interface_up.set
    - user: root
    - group: root
    - mode: 0644
{% endif %}
{% endfor %}
{% for iface in result['rpc_reply']['interface-information'][0]['physical-interface'] %}
{% if iface['admin-status'][0]['data'] == 'down' %}
salt://interface_up_{{ iface['name'][0]['data'].replace('/','_') }}_file.set:
  junos:
  - install_config
  - template_vars:
      iface_name: {{ iface['name'][0]['data'] }}
{% endif %}
{% endfor %}
