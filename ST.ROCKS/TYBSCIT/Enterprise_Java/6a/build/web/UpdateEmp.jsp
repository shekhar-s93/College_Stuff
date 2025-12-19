<%-- 
    Document   : UpdateEmp
    Created on : Sep 29, 2025, 11:34:52 AM
    Author     : SHEKHAR SUMAN
--%>

<%@ page contentType="text/html;charset=UTF-8" import="java.sql.*" %>
<html>
<head>
    <title>Employee Record Update</title>
</head>
<body>
    <h1>Employee Record Update</h1>

<%
    // Get form parameters
    String eno = request.getParameter("txtEno");
    String name = request.getParameter("txtName");
    String age = request.getParameter("txtAge");
    String sal = request.getParameter("txtSal");

    try {
        // Load JDBC driver
        Class.forName("com.mysql.cj.jdbc.Driver");

        // Connect to database (replace user & password as needed)
        Connection con = DriverManager.getConnection(
    "jdbc:mysql://localhost:3306/empdb", "root", "test");


        // Check if employee exists
        PreparedStatement stmt = con.prepareStatement("SELECT * FROM emp WHERE empid=?");
        stmt.setString(1, eno);
        ResultSet rs = stmt.executeQuery();

        if(rs.next()) {
            out.println("<h2>~~~ Employee " + name + " Exists ~~~</h2>");

            // Update salary
            PreparedStatement pst1 = con.prepareStatement(
                "UPDATE emp SET salary=? WHERE empid=?");
            pst1.setString(1, sal);
            pst1.setString(2, eno);
            pst1.executeUpdate();

            // Update age
            PreparedStatement pst2 = con.prepareStatement(
                "UPDATE emp SET age=? WHERE empid=?");
            pst2.setString(1, age);
            pst2.setString(2, eno);
            pst2.executeUpdate();

            out.println("<p style='color:green;'>Employee record updated successfully ✅</p>");
        } else {
            out.println("<h2 style='color:red;'>Employee Record does not exist ❌</h2>");
        }

        // Close resources
        rs.close();
        stmt.close();
        con.close();

    } catch(Exception e) {
        out.println("<h3 style='color:red;'>Error: " + e.getMessage() + "</h3>");
    }
%>
</body>
</html>

