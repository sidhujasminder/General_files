run interface sls:
  local.state.apply:
    - tgt: {{ data['hostname'] }}
    - arg:
      - check_interface
