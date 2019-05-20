# SDN-firewall
ryu based sdn firewall,  using mininet.    

1.firat start ryu:   
`ryu-manager ryu.app.rest_firewall`      
2.then start mininet:          
`python switch.py `          
3.then add rules and add port mirroring:        
```
xterm s1

curl -X PUT http://localhost:8080/firewall/module/enable/0000000000000001
curl -X POST -d '{"nw_src": "10.0.0.2", "nw_dst": "10.0.0.1", "nw_proto": "TCP"}' http://127.0.0.1:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "10.0.0.1", "nw_dst": "10.0.0.2", "nw_proto": "TCP"}' http://127.0.0.1:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "10.0.0.3", "nw_dst": "10.0.0.4", "nw_proto": "TCP"}' http://127.0.0.1:8080/firewall/rules/0000000000000001
curl -X POST -d '{"nw_src": "10.0.0.4", "nw_dst": "10.0.0.3", "nw_proto": "TCP"}' http://127.0.0.1:8080/firewall/rules/0000000000000001

ovs-vsctl del-port s1-eth4
ovs-vsctl add-port s1 s1-eth4 -- --id=@p get port s1-eth4 -- --id=@m create mirror name=m0 select-all=true output-port=@p -- set bridge s1 mirrors=@m

```

4.then start http server:         
```
xterm h1

python3 server.py
```

5.then monitor traffic:        
```
xterm h3
python3 monitor.py
```
6.then test firewall:          
```
xterm h2

curl "http://10.0.0.1:80"
curl "http://10.0.0.1:80/?search.pl?form=../../../../../../etc/passwd\x00"
```




