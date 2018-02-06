{% set result = salt['junos.rpc']('get-interface-information','','json') %}
{% for iface in result['rpc_reply']['interface-information'][0]['physical-interface'] %}
{% if iface['admin-status'][0]['data'] == 'down' %}
salt://interface_up.set:
  junos:
    - install_config
    - template_vars:
        iface_name: {{ iface['name'][0]['data'] }}
{% endif %}
{% endfor %}
