import salt.client
local = salt.client.LocalClient()
local.cmd('*', 'test.arg', ['arg1', 'arg2'], kwarg={'foo': 'bar'})
