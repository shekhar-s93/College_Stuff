<%-- 
    Document   : updateEmployee
    Created on : Sep 29, 2025, 8:33:29 PM
    Author     : SHEKHAR SUMAN
--%>

<%@ page contentType="text/html;charset=UTF-8" import="java.sql.*" %>
<html>
<head>
    <title>Employee Update</title>
</head>
<body>
<%
    String eno = request.getParameter("eno");
    String name = request.getParameter("name");
    String age = request.getParameter("age");
    String desg = request.getParameter("desg");
    String salary = request.getParameter("salary");

    Connection con = null;
    PreparedStatement ps = null;

    try {
        Class.forName("com.mysql.cj.jdbc.Driver");
        con = DriverManager.getConnection("jdbc:mysql://localhost:3306/empinfo", "root", "test");

        String sql = "UPDATE employee SET name=?, age=?, desg=?, salary=? WHERE eno=?";
        ps = con.prepareStatement(sql);
        ps.setString(1, name);
        ps.setString(2, age);
        ps.setString(3, desg);
        ps.setString(4, salary);
        ps.setString(5, eno);

        int rows = ps.executeUpdate();

        if (rows > 0) {
            out.println("<h3>Employee record updated successfully!</h3>");
        } else {
            out.println("<h3>No employee found with ENO: " + eno + "</h3>");
        }
    } catch (Exception e) {
        out.println("<h3>Error: " + e.getMessage() + "</h3>");
    } finally {
        if (ps != null) try { ps.close(); } catch (Exception ex) {}
        if (con != null) try { con.close(); } catch (Exception ex) {}
    }
%>
</body>
</html>

