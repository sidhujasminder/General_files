When a proxy is started it generates the following events on the event bus:

```
minion_start        {
    "_stamp": "2018-02-08T13:45:25.724743",
    "cmd": "_minion_event",
    "data": "Minion proxy01 started at Thu Feb  8 19:15:25 2018",
    "id": "proxy01",
    "pretag": null,
    "tag": "minion_start"
}
salt/minion/proxy01/start                {
    "_stamp": "2018-02-08T13:45:25.732755",
    "cmd": "_minion_event",
    "data": "Minion proxy01 started at Thu Feb  8 19:15:25 2018",
    "id": "proxy01",
    "pretag": null,
    "tag": "salt/minion/proxy01/start"
}
minion/refresh/proxy01    {
    "Minion data cache refresh": "proxy01",
    "_stamp": "2018-02-08T13:45:25.846433"
}
minion/refresh/proxy01    {
    "Minion data cache refresh": "proxy01",
    "_stamp": "2018-02-08T13:45:25.922161"
}
 

```
