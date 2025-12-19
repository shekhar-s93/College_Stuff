<%@page contentType="text/html" pageEncoding="UTF-8" import="myPackage.*" %>
<!DOCTYPE html>
<html>
<head>
    <title>Validation Page</title>
</head>
<body>
    <jsp:useBean id="obj" scope="request" class="myPackage.CheckerBean" />
    <jsp:setProperty name="obj" property="*" />
    
    <% if (obj.validate()) { %>
        <h2 style="color: green;">Validation Successful!</h2>
        <p><strong>Name:</strong> <%= obj.getName() %></p>
        <p><strong>Age:</strong> <%= obj.getAge() %></p>
        <p><strong>Hobby:</strong> <%= obj.getHob() %></p>
        <p><strong>Email:</strong> <%= obj.getEmail() %></p>
        <p><strong>Gender:</strong> <%= obj.getGender() %></p>
    <% } else { %>
        <h2 style="color: red;">Validation Failed!</h2>
        <div style="color: red; font-weight: bold;">
            <%= obj.getError() %>
        </div>
        <br>
        <a href="javascript:history.back()">Go Back</a>
    <% } %>
</body>
</html>