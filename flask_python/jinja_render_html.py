data = {'00:0b:ca:fe:00:01': [('interface_name', 'bme0.32768'),
                       ('ip_address', '128.0.0.17'),
                       ('mac_address', '00:0b:ca:fe:00:01', u'DATAVAN TC')],
 '00:0b:ca:fe:00:02': [('interface_name', 'bme0.32768'),
                       ('ip_address', '128.0.0.18'),
                       ('mac_address', '00:0b:ca:fe:00:02', u'DATAVAN TC')],
 '00:0b:ca:fe:00:03': [('interface_name', 'bme0.32768'),
                       ('ip_address', '128.0.0.19'),
                       ('mac_address', '00:0b:ca:fe:00:03', u'DATAVAN TC')],
 '00:0c:29:18:74:7f': [('interface_name', 'vlan.500'),
                       ('ip_address', '192.168.4.80'),
                       ('mac_address', '00:0c:29:18:74:7f', u'VMware, Inc.')],
 '2c:0e:3d:a0:29:0f': [('interface_name', 'vlan.1337'),
                       ('ip_address', '192.168.11.120'),
                       ('mac_address',
                        '2c:0e:3d:a0:29:0f',
                        u'SAMSUNG ELECTRO-MECHANICS(THAILAND)')],
 '30:b6:4f:23:74:05': [('interface_name', 'ge-0/0/8.0'),
                       ('ip_address', '40.40.40.2'),
                       ('mac_address',
                        '30:b6:4f:23:74:05',
                        u'Juniper Networks')],
 'f4:5c:89:b4:ba:af': [('interface_name', 'vlan.1337'),
                       ('ip_address', '192.168.11.110'),
                       ('mac_address', 'f4:5c:89:b4:ba:af', u'Apple, Inc.')]}

daemon_errmsg = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<table style="width:100%">
          <tr>
            <th>OUI</th>
            <th>MAC</th>
            <th>IP</th>
            <th>address-book Entry?</th>
            <th>Part of policy?</th>
            <th>Add to firewall?</th>
          </tr>
          

        {% for key , value in data.iteritems() %}
        <tr>
            <td style = "text-align: center;">{{ value[2][2] }}</td>
            <td style = "text-align: center;">{{ value[2][1] }}</td>
            <td style = "text-align: center;">{{ value[1][1] }}</td>
            <td style = "text-align: center;">Yes - "LEMON MAC PRO"</td>
            <td style = "text-align: center;">Yes - "SAFE"</td>
            <td style = "text-align: center;"><button name="button">Add to SRX Policy: SAFE</button></td>
          
        </tr>
        {% endfor %}
       
</table>

</body>
</html>

"""


from jinja2 import Environment

#data_daemon_errmsg = Environment().from_string(daemon_errmsg).render(data=data)
import jinja2
loader = jinja2.FileSystemLoader('basic.html')
env = jinja2.Environment(loader=loader)
template = env.get_template('')
print template.render(data=data)
