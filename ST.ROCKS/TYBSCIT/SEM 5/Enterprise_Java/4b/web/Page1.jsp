<%-- 
    Document   : Page1
    Created on : Sep 29, 2025, 9:28:51 AM
    Author     : SHEKHAR SUMAN
--%>

<%@ page contentType="text/html;charset=UTF-8" %>
<html>
<head>
    <title>Login Page</title>
</head>
<body>
    <h2>Enter Login Details</h2>
    <form action="Validate.jsp" method="post">
        Username: <input type="text" name="username" required><br><br>
        Password: <input type="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>

