#introduction
> This document is for setup a conchdb cluster in the unimelb research cloud instances.
#run the couchdb container
> sudo docker run --rm -d --name couchdb -p 5984:5984 -p 4369:4369 -p 9100-9200:9100-9200 -v /data:/opt/couchdb/data -e "COUCHDB_USER=admin" -e "COUCHDB_PASSWORD=admin" ibmcom/couchdb3:3.0.0
#modify the "vm.args"
> sudo docker exec -it couchdb bash  
> sudo find / -name "vm.args"   
> echo "-name couchdb@172.26.130.129" /opt/couchdb/etc/vm.args    
> echo "-setcookie testtest" >/opt/couchdb/etc/vm.args  
> echo "-kernel inet_dist_listen_min 9100" >/opt/couchdb/etc/vm.args  
> echo "-kernel inet_dist_listen_max 9200" >/opt/couchdb/etc/vm.args  
> echo "-kernel error_logger silent" >/opt/couchdb/etc/vm.args  
> echo "-sasl sasl_error_logger false" >/opt/couchdb/etc/vm.args  
> echo "+K true" >/opt/couchdb/etc/vm.args  
> echo "+A 16" >/opt/couchdb/etc/vm.args  
> echo "+Bd -noinput" >/opt/couchdb/etc/vm.args  
> cat /opt/couchdb/etc/vm.args    
> sudo docker restart couchdb
#modify the authority
> sudo chmod 775 /data  

#test connection
> erl -name bus@172.26.133.24 -setcookie 'brumbrum' -kernel inet_dist_listen_min 9100 -kernel   
> inet_dist_listen_max 9200  
> erl -name car@172.26.131.157 -setcookie 'brumbrum' -kernel inet_dist_listen_min 9100 -kernel   
> inet_dist_listen_max 9200  
> net_kernel:connect_node('car@172.26.131.157').  
> net_kernel:connect_node('bus@172.26.133.24').

#config
> curl http://admin:admin@172.26.130.129:5984/_uuids?count=2  
> curl -X PUT http://admin:admin@172.26.130.129:5984/_node/_local/_config/admins/admin -d '"admin"'  
> curl -X PUT http://admin:admin@172.26.130.129:5984/_node/_local/_config/chttpd/bind_address -d '"0.0.0.0"'  
> curl -X PUT http://admin:admin@172.26.130.129:5984/_node/_local/_config/couchdb/uuid -d '"FIRST-UUID-GOES-HERE"'  
> curl -X PUT http://admin:admin@172.26.130.129:5984/_node/_local/_config/couch_httpd_auth/secret -d '"SECOND-UUID-GOES-HERE"'  

#membership 
> curl -u admin:admin -X GET 172.26.130.129:5984/_membership

#setup cluster and add node
> curl -X POST -H "Content-Type: application/json" http://admin:admin@172.26.131.157:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "admin", "password":"admin", "port": 5984, "node_count": "4", "remote_node": "172.26.131.215", "remote_current_user": "admin", "remote_current_password": "admin" }'  
> curl -X POST -H "Content-Type: application/json" http://admin:admin@172.26.131.157:5984/_cluster_setup -d '{"action": "add_node", "host":"172.26.131.215", "port": 5984, "username": "admin", "password":"admin"}'  
> 
> curl -X POST -H "Content-Type: application/json" http://admin:admin@172.26.131.157:5984/_cluster_setup -d '{"action": "enable_cluster", "bind_address":"0.0.0.0", "username": "admin", "password":"admin", "port": 5984, "node_count": "4", "remote_node": "172.26.130.129", "remote_current_user": "admin", "remote_current_password": "admin" }'  
> curl -X POST -H "Content-Type: application/json" http://admin:admin@172.26.131.157:5984/_cluster_setup -d '{"action": "add_node", "host":"172.26.130.129", "port": 5984, "username": "admin", "password":"admin"}'  
> 
> curl -X POST -H "Content-Type: application/json" http://admin:admin@172.26.131.157:5984/_cluster_setup -d '{"action": "finish_cluster"}'  

#delete node from cluster
> curl "http://admin:admin@172.26.130.129:5984/_node/_local/_nodes/couchdb@172.26.128.126"  
> curl -X DELETE "http://admin:admin@172.26.130.129:5984/_node/_local/_nodes/couchdb@172.26.128.126?rev=1-967a00dff5e02add41819138abb3284d"  


#verify cluster setup
> curl http://admin:admin@172.26.130.129:5984/_cluster_setup  

#create database
> curl -XPUT "http://admin:admin@172.26.130.129:5984/tt"  
#delete database
> curl -X DELETE admin:admin@172.26.130.129:5984/tt  
#upload data
> curl -XPOST "http://admin:admin@172.26.130.129:5984/twitter/_bulk_docs " --header "Content-Type: application/json" \
>   --data @./datatest.json  
