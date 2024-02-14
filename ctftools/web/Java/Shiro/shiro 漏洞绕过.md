# url请求绕过过程
## CVE-2020-1957
客户端请求URL: /xxx/..;/admin/
Shrio 内部处理得到校验URL为 /xxxx/..,校验通过
SpringBoot 处理 /xxx/..;/admin/ , 最终请求 /admin/, 成功访问了后台请求。

## CVE-2020-11989
客户端请求URL: /;/test/admin/page
Shrio 内部处理得到校验URL为/,校验通过
SpringBoot最终请求 /admin/page, 成功访问了后台请求。

## CVE-2020-13933
客户端请求URL:/admin/;page
Shrio 内部处理得到校验URL为/admin/,校验通过
SpringBoot最终请求 /admin/;page, 成功访问了后台请求。