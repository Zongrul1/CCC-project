#Config a Docker client to use HTTP Proxy
If you want to access the Internet inside a Docker container to do some debugging/testing etc. You may need to config the Docker client in addition to the configuration you may have done on the instance (/etc/environment) and for the Docker daemon (/etc/systemd/system/docker.service.d/http-proxy.conf).

All you need to do is to create or edit ~/.docker/config.json and add the following configuration:

> {
>     "proxies":{  
>         "default":{  
>             "httpProxy":"http://wwwproxy.unimelb.edu.au:8000",  
>             "httpsProxy":"http://wwwproxy.unimelb.edu.au:8000",            "noProxy":"localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.unimelb.edu.au,.cloud.unimelb.edu.au"  
>         }
>     }
> }