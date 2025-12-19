<%-- 
    Document   : Validate
    Created on : Sep 29, 2025, 9:30:25 AM
    Author     : SHEKHAR SUMAN
--%>

<%@ page contentType="text/html;charset=UTF-8" import="mypack.*" %>
<html>
<head><title>Validation Page</title></head>
<body>
<jsp:useBean id="obj" class="mypack.CheckerBean" scope="request" />
<jsp:setProperty name="obj" property="*" />

<%
    if (obj.validate()) {
%>
        <jsp:forward page="Welcome.jsp" />
<%
    } else {
%>
        <jsp:forward page="Error.jsp" />
<%
    }
%>
</body>
</html>

