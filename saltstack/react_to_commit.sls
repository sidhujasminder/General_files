run interface sls:
  local.state.apply:
    - tgt: vmx
    - arg:
      - check_interface
