# Interesting Backup locations:

ROOT/splunk/etc/users/
--> Custom user dashboards, reports, lookups, etc

ROOT/splunk/etc/apps/search/local/
--> Search app's various custom configs including stanza files for custom sourcetypes

ROOT/splunk/var/lib/splunk/
--> **Index location**

# Basic how lookups work:

Lookups add fields from an external source to your events based on the values of fields that are already present in those events. 
A simple lookup example would be a lookup that works with a CSV file that combines the possible HTTP status values (303, 404, 201, and so on) with their definitions. 
If you have an event that includes an HTTP status value, the lookup could add the HTTP status description to the event. 

**--> So lookups add fields to events based off of values of specified fields**
**--> Wildcards are avaliable through GUI under lookup definitions --> advanced options **

**Lookup via an uploaded csv file

```
index=a_finance earliest=0 
| lookup bank.csv host
```

**Lookup via a lookup definition** (Wildcards can be used for these, along with other special options)

```
index=a_finance earliest=0 
| lookup ex host
```

Once you run these commands, all fields specified will have additional fields added to their rows based off matches contained within your lookup files/definitions.

# Subsearch Limits:

**By default, subsearches return a maximum of 10,000 results and have a maximum runtime of 60 seconds.** In large production environments, it is possible that the subsearch in this example will timeout before it completes. The best option is to rewrite the query to limit the number of events that the subsearch must process. Alternatively, you can increase the maximum results and maximum runtime parameters.

# Accelerating Data Models

**Link**
--> https://docs.splunk.com/Documentation/Splunk/8.0.5/Knowledge/Acceleratedatamodels

----------------------------------------------------

This is how data model acceleration differs from report acceleration and summary indexing:

Report acceleration and summary indexing speed up individual searches, on a report by report basis. They do this by building collections of precomputed search result aggregates.

Data model acceleration speeds up reporting for the entire set of fields that you define in a data model and which you and your Pivot users want to report on. In effect it accelerates the dataset represented by that collection of fields rather than a particular search against that dataset.

----------------------------------------------------

When Splunk software finishes building a data model acceleration summary, its data model summarization process ensures that the summary always covers its summary range. The process periodically removes older summary data that passes out of the summary range. 

----------------------------------------------------

So it is best to set the Summary Range for a data model wide enough that it captures all of the searches you plan to run against it. 

----------------------------------------------------

There is a cost for this improvement in summarization search performance. The concurrent searches count against the total number of concurrent search jobs that your Splunk deployment can run, which means that **they can cause increased indexer resource usage. **

----------------------------------------------------

You can verify that Splunk software is scheduling searches to update your data model acceleration summaries. Inlog.cfg, set category.SavedSplunker=DEBUG and then watch scheduler.log for events like:

```

04-24-2013 11:12:02.357 -0700 DEBUG SavedSplunker - Added 1 scheduled searches for accelerated datamodels to the end of ready-to-run list

```

----------------------------------------------------

# tstats and .tsidx information


**time-series index files** --> which have the .tsidx

--> This could lead to faster searches graphical representations with the Graphical Network Topology App
https://splunkbase.splunk.com/app/4611/

Here are some articles on how to use the GN Top App and how tstats and .tsidx files work:

https://www.splunk.com/en_us/blog/machine-learning/understanding-and-baselining-network-behaviour-using-machine-learning-part-i.html

https://community.splunk.com/t5/Splunk-Search/What-is-tstats-and-why-is-so-much-faster-than-stats/td-p/116960 

# Places to get Sample Data

https://www.hs-coburg.de/index.php?id=927

https://docs.splunk.com/Documentation/Splunk/8.0.5/SearchTutorial/Systemrequirements#Download_the_tutorial_data_files

https://catalog.data.gov/organization/montgomery-county-of-maryland?page=7

# Notes for 8/10/2020

```

sourcetype=linux_secure action=failure host!=mail* --> if it doesn't have a field "host" will not return values since you are looking at the field
sourcetype=linux_secure action=failure NOT host=mail* --> if it doesn't have a field "host" will return values

index=web status IN ("500", "503", "505")

```

Dashboards have a dark mode and can be referenced via a hyper link

#Can I make a dashboard in which has a bubble chart of all commands executed via sudo?


```
sourcetype=access_combined earliest=01/08/2018:12:45:00

```

Indexes can have access limits for secuirty purposes

Search Terms -->
Commands --> 
Functions --> Do operations on data
Arguments --> Supply these to functions
Clauses --> results grouped or defined

```
sourcetype=acc* status=200 | stats list(product_name) as "Games Sold" | top "Games Sold"

* | fields pid | top pid

index=web sourcetype=access* status=200 product_name=* | table JESSIONID,product_name,price | rename JSESSIONID as "User Session"

limit 20
sort
dedup 
rname ip as "IP_Address"

```

Transform Commands --> creat data into visuals


```

index=sales sourcetype=vendor_sales | top Vendor limit=5 showperc=False countfield="Number of Sales" useother=True

index=sales sourcetype=vendor_sales | stats distinct_count(product_name)

```

rare --> same as top command but with least valus

Dashboards are reports gathered together into a single pane of glass

Pivot --> Easy Reports without SPL


Goal --> RegEx --> Custom Command Feild --> Custom Dashboard

**Lookups allow you to define descriptions for data within splunk**

Automatic lookup does exist

```
| inputlookup http_csv

index=web soucetype=access_combined NOT status=200 | lookup http_status code as status

index=web soucetype=access_combined NOT status=200 | lookup http_status code as status, OUTPUT code as "HTTP Code", description as "HTTP Description"

```

Aug 10 20:01:56 vagrant sudo:  vagrant : TTY=pts/0 ; PWD=/home/vagrant ; USER=root ; COMMAND=/bin/ss -tulp


(?i)^(?:[^ ]* ){2}(?:[+\-]\d+ )?(?P<log_level>[^ ]*)\s+(?P<component>[^ ]+) - (?P<event_message>.+) 

**sourcetype=syslog sudo | rex field=_raw "sudo:.*COMMAND\=(?<X_KOMAND>.*)"**

**rex command or regex command?**

-->Use the rex command to either extract fields using regular expression named groups, or replace or substitute characters in a field using sed expressions.

-->Use the regex command to remove results that do not match the specified regular expression. 
  
  
  
# Tutorial, How to Install SAI (Splunk App for Infrastructure) using UDP instead of HEC (HTTP Event Collector) on *nix box

Disclaimer: I'm using collectd instead of statd, don't know much about statd yet, but I can imagine it will be much more useful. Usually how my luck works with these things

**Abstract**
HEC is a useful way to send metrics data, but I would like to send everything through a UF since it is less work from a network security point of view. Plus, when you use SAI to generate a script, it installs a UF anyway on the machine. It was a bit tricky to figure out since some of the Splunk do is sorta misleading, however, most of my trouble contributed to one single oversight on my part. Anyway lets begin!

1) On your Splunk Indexer/Search Head install the following Apps:
--> SAI App
--> SAI Addon **If you don't install the addon NOTHING WILL WORK**

2) In order to get your nix box up and running for UDP you need to configure logs and metrics, logs are much easier since all they require is a universal forwarder, so install that first, then use this docs:
https://docs.splunk.com/Documentation/InfraApp/2.1.0/Admin/ManualInstalLinuxUF

Start at step 2 , make sure your input and output are in the following directory of the UF:
${SPLUNK_HOME}/etc/apps/splunk_app_infra_uf_config/local

3. Now for the metrics install, this will require the install of collectd, but this docs will walk you through it:
https://docs.splunk.com/Documentation/InfraApp/2.1.0/Admin/ManageAgents

The hardest part is getting the **write_splunk** and processmon into the correct plugin dir, base off your *nix build, but just read carefully enough and it will be easy enough.

After that you need to configure your collectd config located in **/etc/collectd/** (for a Ubuntu box)

Configuring what metrics you want is outside of this tutorial, but for the config file you need this for UDP to work:

```
<Plugin write_splunk>
        server "127.0.0.1"
        buffersize 9000
        useudp true
        udpport 2222
        Dimension "entity_type:nix_host"
</Plugin>

```

Where:

server --> The server where the UF is located at (usually local)
udport --> The port the UF is listening on (You set this up in the next step)
buffersize --> whatever, increase if you have alot of metrics
useudp --> This tells write_splunk to use udp instead of HEC
Dimension --> YOU NEED THIS, this is more of a placeholder, but is required for the indexer to parse correctly!

After that configure the rest of your metrics/plugins/options for collectd, read the docs mentioned above/the sample config file for more information.

ONE MORE THING --> Make sure you specify the host as the local IP of the box, otherwise, SAI will not be able to differentiate  hosts!

Now Start collectd

3) Now we configure the UF to receive the  write_splunk udp packets. Use this doc for help:
https://docs.splunk.com/Documentation/InfraApp/2.1.0/Admin/WriteCollectdToUF

Basically all you need to do is open 

```
${SPLUNK_HOME}/etc/apps/splunk_app_infra_uf_config/local/inputs.conf
```
and add this to it:

```
[udp://{UDP_PORT (Same as what you specified in collectd.conf}]
index = em_metrics
sourcetype = em_metrics_udp
no_appending_timestamp = true
```

where:
index --> this is a custom index setup by SAI addon, only change if required and are able to update the addon
sourcetype --> this tells the addon what it is, so it can be processed correctly
no_appending_timestamp = true --> because this makes it just work

4) Now restart your UF and Splunk and SAI App should now work for your host. 

**IDEA** --> the script that you download for SAI "auto config"  forces HEC, but if you modify it you can create a script that can be pushed to multiple hosts...

Here are my input and output configs for reference, I did not include my collectd config since it was too long. However the sample config in doc: 
https://docs.splunk.com/Documentation/InfraApp/2.1.0/Admin/ManageAgents 
is more than enough:

```
[default]
host = SAI_vagrant

[monitor:///var/log/syslog]
disabled = false
sourcetype = syslog

[monitor:///var/log/auth.log]
disabled = false
sourcetype = syslog

[monitor:///home/vagrant/splunkforwarder/var/log/splunk/*.log]
disabled = false
index = _internal

[udp://2222]
index = em_metrics
sourcetype = em_metrics_udp
no_appending_timestamp = true
```


```
[tcpout]
defaultGroup = splunk-app-infra-autolb-group

[tcpout:splunk-app-infra-autolb-group]
disabled = false
server = 127.0.0.1:8090
```
  
  
# Important notes on how to get collectd, uf, and SAI working together

collectd_http

**The HTTP Event Collector (HEC) lets you send data and application events to a Splunk deployment over the HTTP and Secure HTTP (HTTPS) protocols. HEC uses a token-based authentication model.** You can generate a token and then configure a logging library or HTTP client with the token to send data to HEC in a specific format. This process eliminates the need for a Splunk forwarder when you send application events.

After you enable HEC, as a developer, you can use HEC tokens in your app to send data to HEC. You do not need to include Splunk credentials in your app or supported files

Source --> Tells Splunk What type of data it is
Index --> Tells Splunk where to save it/process it

For optimal performance, limit the number of source types contained within an index to fewer than 20 if possible.  --> So indexs can only contain certain source types

**Here is the install script from SAI, basically it wants you to setup HEC, but it also installs a UF, so why not just pipe it though the UF???**

```
export SPLUNK_URL="192.168.33.10" && export HEC_PORT="8088" && export RECEIVER_PORT="8089" && export INSTALL_LOCATION="/opt/"  && export HEC_TOKEN="aa3a8d75-415c-470d-97ac-dcb1a419d1b5" && export SAI_ENABLE_DOCKER=  && export DIMENSIONS= METRIC_TYPES=cpu,uptime,memory METRIC_OPTS=cpu.by_cpu LOG_SOURCES="/etc/collectd/collectd.log%collectd,\$SPLUNK_HOME/var/log/splunk/*.log*%uf,/var/log/syslog%syslog,/var/log/auth.log%syslog" AUTHENTICATED_INSTALL=No && export INSTALL_LOCATION="/opt/" && wget  http://192.168.33.10:8000/static/app/splunk_app_infrastructure/unix_agent/unix-agent.tgz && tar -xzf "unix-agent.tgz" || gunzip -c "unix-agent.tgz" | tar xvf - && cd unix-agent && bash install_uf.sh && bash install_agent.sh && cd .. && rm -rf unix-agent && rm -rf unix-agent.tgz
```


bash install_uf.sh && bash install_agent.sh --> These are all that are run, these scripts install and configure the UF and collectd


Basically it looks like it is installing a forwarder.... but it uses HEC instead of UDP???? --> Might be easier to script, plus HEC seems to work better
for cloud solutions.


/home/vagrant/splunkforwarder/etc/apps/search/local --> new location for a uf "inputs.conf" file, it looks like this one is set if I enable inputs via CLI, not from
a config file --> each "app" should be in this folder.

Pulled this from script: --> This "output.conf" belongs in ${SPLUNK_HOME}/etc/apps/splunk_app_infra_uf_config/local
-------------------------------------------

```
[tcpout]
defaultGroup = splunk-app-infra-autolb-group

[tcpout:splunk-app-infra-autolb-group]
disabled = false
server = $Server:$Port

```

-------------------------------------------


splunk_hostname=$(hostname) --> in collectd.conf, you need to set the hostname so that SAI knows how to distinguish machines of type.
splunk_home="/opt/splunkforwarder" --> Line 295, so it looks like I need to change this if I have a custom forwarder install location

The code below shows how the collectd.conf is configured, it looks like you can have HEC and UDP based off of what evn vars you set
-----------------------------------------------------

```
echo -e "\n<Plugin write_splunk>" >> collectd.conf
echo -e "           server \"$splunk_url\"" >> collectd.conf
if [ "$metric_use_udp" = "YES" ]; then
    echo -e "           useudp true" >> collectd.conf
    echo -e "           udpport $udp_port" >> collectd.conf
    if [ -n "$metric_buffer_size" ]; then
        echo -e "           buffersize $metric_buffer_size" >> collectd.conf
    fi
else
    echo -e "           port \"$hec_port\"" >> collectd.conf
    echo -e "           token \"$hec_token\"" >> collectd.conf
    echo -e "           ssl true" >> collectd.conf
    echo -e "           verifyssl false" >> collectd.conf
fi
echo -e "           Dimension \"entity_type:nix_host\"" >> collectd.conf

echo -e "</Plugin>" >> collectd.conf
get_splunk_hostname

sed_inplace "s/#Hostname    \"collectd.server.sample\"/Hostname    \"$splunk_hostname\"/g" "collectd.conf"
```

----------------------------------------------------------

--> Line 287 This code proves that you can have an HEC and UDP mode, and you always need the **"entity_type:nix_host"** in the plugin config
--> Also this is the "Right way" to build your collectd.conf 

For HEC, the **write_splunk plugin** for collectd forwards it directly from the plugin, so the uf is never touched for metrics, however, a uf still needs 
to be setup for log reporting. Thus the SAI uses HEC and a UF for its stuff, If only I can forward to a uf both the metrics and Logs, it just seems more logical that
way....

Also there seems to be a slightly differnt group from what I am using for my output.conf, maybe that is why SAI can't seem to see anything...


splunk_app_infra_uf_config="splunk_app_infra_uf_config"

--> This code seems to create the SAI dir within the UF file stucture and per doc tutorials, it would seem we would want to save our inputs and outputs
to:

**${SPLUNK_HOME}/etc/apps/splunk_app_infra_uf_config/local**

**So it looks like I need the dir and then make inputs.conf and outputs.conf**

-----------------------------------------------------

```
# overwrite default inputs.conf, not forwarding any logs
function clean_up_inputs {
    uf_inputs_conf="$splunk_home/etc/apps/SplunkUniversalForwarder/local/inputs.conf"

    if [ -d "$splunk_home/etc/apps/SplunkUniversalForwarder/local" ]; then
        $_sudo mv "$splunk_home/etc/apps/SplunkUniversalForwarder/local" "$splunk_home/etc/apps/SplunkUniversalForwarder/local.$(date +'%Y%m%d-%H%M%S').bak"
    fi

    $_sudo mkdir -p "$splunk_home/etc/apps/SplunkUniversalForwarder/local"

    $_sudo touch "$uf_inputs_conf"
    $_sudo chmod a+w "$uf_inputs_conf"
    # overwrite default and etc/system/default and SplunkUniversalForwarder/default
    echo -e "[monitor://\$SPLUNK_HOME/var/log/splunk]" >> "$uf_inputs_conf"
    echo -e "disabled = true" >> "$uf_inputs_conf"
    echo -e "\n[monitor://\$SPLUNK_HOME/var/log/splunk/metrics.log]" >> "$uf_inputs_conf"
    echo -e "disabled = true" >> "$uf_inputs_conf"
    echo -e "\n[monitor://\$SPLUNK_HOME/var/log/splunk/splunkd.log]" >> "$uf_inputs_conf"
    echo -e "disabled = true" >> "$uf_inputs_conf"
}
```

-----------------------------------------------------
--> This code suggests that if you want overwrite UF defaults for input, you save it to "$splunk_home/etc/apps/SplunkUniversalForwarder/local/inputs.conf"
--> This is differnt from what I was initally taught, since I thought everything was saved via "/etc/system/local" but I guess this overrides everything?
"/etc/system/local" originally  has nothing in it

Below is a correct inputs.conf that gets udp from collectd
-------------------------------------

```
[default]
host = vagrant

[monitor:///var/log/syslog]
disabled = false
sourcetype = syslog

[monitor:///var/log/auth.log]
disabled = false
sourcetype = syslog

[monitor:///home/vagrant/splunkforwarder/var/log/splunk/*.log]
disabled = false
index = _internal

[udp://2222]
index = em_metrics
sourcetype = em_metrics_udp
no_appending_timestamp = true
```

-------------------------------------


**So SAI needs two parts to work: the acutal app and then the addon, the addon actually tells the indexer how to interperate data...
so that was my problem all along, guess now I know how to set this up manually.**
  
  
# SAI Testing with Splunk:

**Todays notes:**

se a deployment server. The deployment server can ease distribution of configurations, but does not make a forwarder forward data by itself. You must use the deployment server to deliver configurations to the forwarders so that they collect the data you want and send it to the place you want.

Key configuration files are:

    inputs.conf controls how the forwarder collects data.
    outputs.conf controls how the forwarder sends data to an indexer or other forwarder.
    server.conf for connection and performance tuning.
    deploymentclient.conf for connecting to a deployment server.


    Troubleshooting

    --> Make sure to restart the forwarder and Splunk in order for it to work?
    --> collectd config: /etc/collectd
    

The metric event is not properly structured, source=2222, sourcetype=em_metrics_udp, host=127.0.0.1, index=em_metrics. Metric event data without a metric name and preoperly formated numerical values are invalid and cannot be indexed. Ensure the input metric data is not malformed, have one or more keys of the form "metric_name:<metric>" (e.g..."metric_name:cpu.idle") with corresponding floating point values. 


Received event for unconfigured/disabled/deleted index=em_metrics with source="source::udp:2222" host="host::127.0.0.1" sourcetype="sourcetype::em_metrics_udp". So far received events from 1 missing index(es). 8/5/2020, 11:11:39 PM


-->By these errors it seems malformed data is being sent to the indexer, so my server side is working...
-->Maybe I am not sending to SAI???

After I restart of Splunk I got this error again:
The metric event is not properly structured, source=2222, sourcetype=em_metrics, host=127.0.0.1, index=em_metrics. Metric event data without a metric name and preoperly formated numerical values are invalid and cannot be indexed. Ensure the input metric data is not malformed, have one or more keys of the form "metric_name:<metric>" (e.g..."metric_name:cpu.idle") with corresponding floating point values. 

--> something is not talking correctly...

**Links to important Doc pages**

Send collectd data to a local universal forwarder
https://docs.splunk.com/Documentation/InfraApp/2.1.0/Admin/WriteCollectdToUF

Getting Data From TCP and UDP ports
https://docs.splunk.com/Documentation/Splunk/8.0.5/Data/Monitornetworkports#Add_a_network_input_using_inputs.conf

Manually configure log collection on a *nix host for Splunk App for Infrastructure
https://docs.splunk.com/Documentation/InfraApp/2.1.0/Admin/ManualInstalLinuxUF

Manually configure metrics collection on a *nix host for Splunk App for Infrastructure
https://docs.splunk.com/Documentation/InfraApp/2.1.0/Admin/ManageAgents

Monitor files and directories with inputs.conf
https://docs.splunk.com/Documentation/Splunk/8.0.5/Data/Monitorfilesanddirectorieswithinputs.conf#Configuration_settings


# Quick Tutorial: How to get Splunk up and running on a nix (Indexer and Forwarder on same machine)

1. Download Splunk Enterprise and Universal Forwarder for nix (as a tar)
2. Extract tars, make sure Indexer and Forward are in different dirs (I had both of mine in home folder and to make sure they where not running as root)
3. Go to "bin" dir for indexer run command:
```
./splunk start ----accept-license.
```
4. The indexer will prompt for admin user creation, create a user.
5. The indexer will now start, ports 8000 and 8089 (http and api) will be listening.
6. Login to Splunk via http, navigate to to settings --> forwarders and receivers, then setup a receiver port number.
7. Go back to nix box and start the forwarder, splunk inside bin (yes the forwarder binary has the same name as the the indexer!):
```
./splunk start ----accept-license.
```
8. Just like the indexer, the forwarder will ask for admin user creation
9. After that the forwarder will be running, only an api port will be open since, there is no http for forwarders! In this case, the setup will ask you specify a different port for api since 8089 by default is being used by the indexer, so select a new port. 
10. Now the forwarder is running, make sure to setup the inputs (data to read) and outputs (location of indexer):
```
#output
./splunk add forward-server 127.0.0.1:8090
#input
./splunk add monitor /var/log
``` 
11. The local config files "FORWARDER_ROOT"/etc/system/local" will now be updated and the forwarder should be forwarding data. Verify by logging into http and checking the data summary under search.
12. Complete!
  
# Splunk General Admin Commands
/opt/splunk/bin/splunk start|restart|stop

sudo ./splunk enable boot-start -user {linux user to start as} 

 
# Quick Ref Guide:
https://www.splunk.com/pdfs/solution-guides/splunk-quick-reference-guide.pdf
  
# Visualization Reference
https://docs.splunk.com/Documentation/Splunk/7.3.1/Viz/Visualizationreference
  
# About transforming commands and searches
https://docs.splunk.com/Documentation/Splunk/7.3.1/Search/Aboutreportingcommands
  
# Command Types:
https://docs.splunk.com/Documentation/Splunk/7.3.1/SearchReference/Commandsbytype#Transforming_commands
  
