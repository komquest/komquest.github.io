```bash
Security Onion Cheat Sheet

Purpose: This is a TTP like sheet that will demonstrate some tips and tricks for Security Onion in hopes of making it use easier and more efficient.
This more like an idea pizza and not a really TTP on a single topic.

########TOPIC
~~SO Scripts~~
-->SO Scripts are used to do maintenance/manage tasks within SO. They are located in "/usr/sbin" and are all in the format "so-{scriptName}" Below is a list of some ones I found useful

-->so-*-[restart|start|stop|status]
These Scripts are used to start/stop/restart/view status of various services within SO. Everything from Elastic Search to Kibana to Bro has its own script for this, however, the most useful ones are:
	so-status --> This shows status for everything within SO, so you can make sure all services are running correctly
	so-restart --> this will restart ALL services within SO, useful for major changes or troubleshooting
	so-sensor-restart --> this will restart everything related to the sensor, if you just made changes to Kibana, elastic-search or Sguil this is the restart for you. Much faster than "so-restart"
	
-->so-email
Setup email forwarding for alerts

-->sosetup
If you want to reinstall SO or change its setup configuration

-->sostat
This will give you status for everything. It will display how much resources a particular process is consuming, and usually how much data it is processing/consuming/etc. This can be used for troubleshooting purposes esp when  you are trying to figure out where in the ELK stack a bottleneck exists. 

-->sostat-quick
This is more of a quick analysis to see if any problems are detected with your SO install. It also displays troubleshooting information.
(check out the other sostat scripts, they all offer various information for troubleshooting purposes)

-->so-user-*
These scripts add/delete/set passwords/etc of SO users (for services like Kibana). Particularly useful is "so-user-list" to see what users SO acknowledges
########/TOPIC


########TOPIC
~~ELK Stack a high level description~~

SO uses the Elasticsearch "ELK" (Elasticsearch, Logstash, Kibana) stack for the backbone of its operations. Data is pulled from the sensor (through Bro and Snort) and then pushed through this stack for processing. Thus, in order to troubleshoot data issues it is recommended to go down this stack in search of discrepancies. The stack:

network tap --> pcap --> bro/snort --> syslog --> logstash --> elasticsearch --> kibana/squert

WHERE:

network tap = this is the hardware level where the actual tap copies data to the SO sensors physical network interface, make sure the network interface is in promiscuous mode
pcap --> the network data stored to disk
bro/snort --> analyze the the pcap to pull data
syslog --> pushes data collected from bro/snort to logstash (in the form of jsons)
logstash --> receives data from syslog and makes it "pretty" before pushing it to Elasticsearch
elasticsearch --> indexs all data recived from logstash
kibana/squert --> displays/searches the data kept in Elasticsearch (frontend to Elasticsearch)

########/TOPIC

########TOPIC
~~Kibana Use notes~~
Here are some hints I found useful while using Kibana that can help with analysis

-->The Kibana Dashboard is where you can view bro/snort data in various "dashboards". The dashboards display tons of information and can be sometimes overwhelming. Here is a template to get started in analyzing the data:
	1. Start under "Bro Hunting --> Connections", this will show you all of the services bro collected data for ("Connections - Service") you can use this to determine where to look for data. For example, if "Connections - Service" displayed activity in ssl, http, and ssh, I would check those three categories for activity.
	2. "Bro Hunting --> Connections" also gives you a good rundown on source/destination IPs and ports and can be ordered to display the most activity per port or IP. Also under "Connections - Source Country" you can get country name of various IPs. (though this is not really as helpful as you might think, since nation states can always proxy through other countries)
	3. Under "Bro Hunting --> HTTP" you can use the "HTTP - Sites" for seeing what HTTP sites are being accessed, "HTTP - Sites Hosting EXE's" for seeing what sites are hosting EXE's and "HTTP - User Agent" to see what kind of devices are being used (This can be esp useful in snooping out strange devices or http requests made by scripts).
	4. Under "Bro Hunting --> SSL" you can use "SSL - Server" to see what SSL sites were accessed and "SSL - Certificate Subject" to find certs for what sites were accessed. Again this can help determine what sites the network is access most as well as sites from potential bad actors. "SSL - Certificate Subject" can also tell you what country each cert was registered under.
	5. The NIDS section ("Alert Data --> NIDS") shows you snort rules that were triggered,  you can use this to correlate bro logs with these triggers.
	
--> You can edit the time-frame for Kibana dashboards at the top right of webapp, make sure you are within the correct scope. 

--> If you want to search for a particular value within the dashboards, use the search bar at the top of screen. This is particularly useful for IP addresses. Note based off of which log category you have selected is where Kibaba will search, thus if you are under http, it will search within the constraints of http and the dashboards defined within that category.

--> For more advanced use you can always create your own dashboards, and dashboard categories. For dashboard categories create/edit these within "Dashboard" and for individual dash boards or graphs use the "Visualize" section of Kibana

--> And speaking of "Visualize" you can use this by itself to query individual dashboards. This can be useful if you want to create a custom one and query data from it, instead of creating a whole dashboard category. I did this during YS77 to help find port scanners from external sources.

--> The "Discover" category is used to do raw searches of Elasticsearch. This is mainly useful for finding the latest alerts or to see if Elasticsearch is receiving data.
########/TOPIC

########TOPIC
~~How to create a custom dashboard using Kibanas "Visualize"~~ (Port Scanner assistance)
If you want to customize a dashboard "Visualize" is the way to go. It can create dashes of many types with Data table, Graphs, and metrics to include a few. For data table you can pull bro based data and display it in columns of your choosing. This can help line up data from multiple sources and thus improve analysis. The following few steps shows how to make a basic table that can help find port scans that successfully connected. Note: depending on how much data you collect or access based off of time period, it can lead to slow downs. Be prepared for esp large sets of data to wait a few min for the data tables to load. There might be a way to optimize this, but at this point in time I have not figured out a way to do so (use search filters):
1. Navigate to "Visualize" within Kibana.
2. Click the plus button to create a new visualization, and then select Data Table
3. Select your data source, I used the "*:logstash-*" index.
4. Now "Metrics" should default to "Count" keep it like this.
5. Under "Buckets" click the "Split Rows" link to create a new column in the data table. (Split table creates a new table within the table)
6. To pull data sets from bro, you can look at the actual messages or grab names from other visualizations.  In this case:
	a) Aggregation = Terms
	b) Field = source_ip (from bro log contained within "*:logstash-*")
	c) Order By = Count
	d) Size = 100
7. Now click "Add sub-buckets" to added another "Split Rows" and repeat except have "Feild" as following values:
	a) source_port
	b) destination_ip
	c) destination_port
	d) respond_bytes (shows how many bytes were transferred)
	e) duration (shows how long this connection took place)
	f) connection_state_description.keyword (this will show if the connection was established or dropped)
8. Once you create all of the columns, hit "Save" at top of web app and give the Visualization a name. Now you should be able to query data. 
9. If you want to disable a column, next to the "Split Rows" on the left side there is a switch button "Disable aggregation"
10. Now type in an IP address or a port number and you should be able to see connections made. If you are not getting anything returned, try disabling "respond_bytes" and "duration"
########/TOPIC


########TOPIC
~~Important Paths~~
Here is a list of important filesystem paths for SO. You can also use the cheat sheet for more information, but listed here are the most commonly used/useful paths
Link to cheat sheet: (google "Security Onion Cheat Sheet")

-->Snort Config
/etc/nsm/<hostname interface>/snort.conf 

-->Bro Config
/opt/bro/etc/networks.cfg, node.cfg 

-->Bro Logs
/nsm/bro/logs/

-->Bro Intel.dat
/opt/bro/share/bro/intel/

-->PCAP file locations (use Wireshark and timestamps from Kibana to find the correct files you are looking for)
/nsm/sensor_data/<hostname-interface>/dailylogs

########/TOPIC

########TOPIC
~~Important Links~~
Here are some common network links used to access services locally or remotely:

-->Access Kibana
https://{Hostname or IP}/app/kibana

-->ssh to remote host
ssh rccp-admin@{IP of host}
########/TOPIC


########TOPIC
~~Troubleshooting~~

--> If you happen to move  your sensor to a new location, make sure to do a "sudo so-stop" --> "sudo so-start" and then wait for like an hour or two. It sometimes takes this long to start receiving new data from Elasticsearch

--> Use sostat to verify all process/services are working correctly. Also if something is disabled/malfunctioning, you can use so-{service name}-restart to restart it. If you restart Logstash I found that it will remain on "warn" for 5 to 10 min before it turns to "ok".

--> If everything is screwed up dont be afraid to rebuild. SO building is quite simple and comes in two parts: The OS install and then the SO install. Boot from the install media to install the OS and then boot to the freshly installed OS to install/setup SO. For the most part just use the defaults making sure the management device and the senor services are both installed on the same machine (evaluation mode). If setup is configured incorrectly you can always use the so scripts to correct ("sosetup") or just re-install. 

--> If you are having trouble accessing Kibana from a remote host it might be a firewall rule, check it by:
	a) sudo ufw disable
	b) check connection, if it works now, it is the firewall
	
--> If you have to reconfigure HOMENET:
	a)Modify Snort Conf file: /etc/nsm/<hostname interface>/snort.conf
		--> "ipvar HOME_NET [192.168.0.0/16,10.0.0.0/8,172.16.0.0/12, {Add your address range(s) here}]"
		--> Note: this only takes into play if the local network you are monitoring does not use the private IP address scheme RFC1918.
		--> ALSO, if SO is placed on an EXTERNAL tap, you need to make sure the public IP address is included in the HOMENET variable. Otherwise SNORT will not detect rule violations properly. Be sure to take into account the external IP address can change, so make sure you update as necessary.
	b)Modify the bro configuration: /opt/bro/etc/networks.cfg
		--> Note: External sensors do not need to modify the bro config to take into account the external IP, essentially you only need to modify this file if your internal network does not follow the private IP address scheme RFC1918
	c)Restart Snort and Bro (so-sensor-restart)

########/TOPIC

```
