from system import Mscan

resultIpArray = Mscan.startNmapScan(ipList)
�����ipList example : ['127.0.0.1']
�����startNmapScan���ص���ip�˿� ���ص�list��ʽ���£�

['127.0.0.1 + NmapService: [open tcp <22> ssh product: OpenSSH version: 6.0p1 Debian 4+deb7u2 extrainfo: protocol 2.0 ostype: Linux]', '127.0.0.1 + NmapService: [open tcp <80> http product: nginx version: 1.2.4]', '127.0.0.1 + NmapService: [open tcp <9000> tcpwrapped]']

from system import Mscan

Mscan.getHttp(resultIpArray)

��������Ƿ���http web�ĺ��� ���ص�list ['http://127.0.0.1:80/']