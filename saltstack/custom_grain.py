import salt.utils
import salt.utils.platform

__proxyenabled__ = ['junos']
__virtualname__ = 'junos'
def __virtual__():
    '''
    Only work on proxy
    '''
    try:
        if salt.utils.platform.is_proxy() and \
           __opts__['proxy']['proxytype'] == 'junos':
            return __virtualname__
    except KeyError:
        pass

    return False

def my_custom_grain(proxy):
#    from jnpr.junos.command.fpcmemory import FPCMemory
    from jnpr.junos import Device
#from pprint import pprint
    from lxml import etree

    fpcdict = {}
    with Device(host="172.22.147.160", user="regress", passwd="MaRtInI") as dev:
        op = dev.rpc.get_fpc_information()
        x = op.findall('fpc')

    # print x
        for i in x:
            slot = i.find('slot').text
            state = i.find('state').text

            if state == 'Online':
                fpcdict.setdefault('FPCONLINE', []).append(slot)
         
    fpcdict = {'FPCONLINE':['1','2']}
    return fpcdict
