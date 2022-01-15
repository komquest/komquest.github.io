# Bro cut out host and referer from logs 
```
cat filename | cut -f9 | sort | uniq | grep -f patternfile.txt -

cat filename | cut -f11 | sort | uniq | grep -f patternfile.txt -
```

# Bro Cut Fix TimeStamps and display custom fields:

```
bro-cut -d -n times.modified times.accessed times.created times.changed fuid
```

# Bro Fields:

```
**Bro Http Fields:**
1 ts
2 uid
3 id.orig_h
4 id.orig_p
5 id.resp_h
6 id.resp_p
7 trans_depth
8 method
9 host
10 uri
11 referrer
12 version
13 user_agent
14 request_body_len
15 response_body_len
16 status_code
17 status_msg
18 info_code
19 info_msg
20 tags
21 username
22 password
23 proxied
24 orig_fuids
25 orig_filenames
26 orig_mime_types
27 resp_fuids
28 resp_filenames
29 resp_mime_types

**Bro Conn Fields:**
1 ts
2 uid
3 id.orig_h
4 id.orig_p
5 id.resp_h
6 id.resp_p
7 proto
8 service
9 duration
10 orig_bytes
11 resp_bytes
12 conn_state
13 local_orig
14 local_resp
15 missed_bytes
16 history
17 orig_pkts
18 orig_ip_bytes
19 resp_pkts
20 resp_ip_bytes
21 tunnel_parents
```

# Bro Log Descriptions

http://gauss.ececs.uc.edu/Courses/c6055/pdf/bro_log_vars.pdf

# Ultimate loop to search through those logs:

```
for i in 'conn.*' 'dce_rpc.*' 'dns.*' 'files.*' 'ftp.*' 'http.*' 'intel.*' 'kerberos.*' 'mysql.*' 'ntlm.*' 'rdp.*' 'sip.*' 'smb_files.*' 'smtp.*' 'ssh.*' 'ssl.*' 'syslog.*' 'tunnel.*'; do echo "$i#################################################################################"; gun $i | smb | grep {IP}; done | tee {FILE}

```

