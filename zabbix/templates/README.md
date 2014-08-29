redhat\_cluster\_template.xml
=====
This zabbix template illustrates how to monitor RedHat Cluster services.  
In this example we monitor zarafa-app and zarafa-arch.  

In the zabbix\_agentd.conf you must add:  
`UserParameter=rhcluster.status[*],sudo clustat -x -s $1|xmlstarlet sel -t -m //clustat/groups/group -v @$2`

Also modification of the /etc/sudoers file is required:  
- Disable requiretty for the zabbix user  

And allow the user to run clustat as root:  
- `zabbix   ALL=(root)  NOPASSWD:/usr/sbin/clustat`


teamspeak3\_zabbix.xml
=====
A simple example template illustrating how to monitor Teamspeak3.
