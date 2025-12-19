<%@page contentType="text/html" import="java.sql.*"%>
<html>
<body>
<h1>Login JSP Page</h1>
<%
    String uname = request.getParameter("txtName");
    String pass  = request.getParameter("txtPass");

    Connection con = null;
    PreparedStatement stmt = null;
    ResultSet rs = null;

    try {
        Class.forName("com.mysql.cj.jdbc.Driver"); 
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/logindb", "root", "test");

        stmt = con.prepareStatement("SELECT Password FROM user WHERE Username=?");
        stmt.setString(1, uname);
        rs = stmt.executeQuery();

        if (rs.next()) {
            String dbPass = rs.getString("Password");
            if (pass.equals(dbPass)) {
                out.println("<h1>~~~ LOGIN SUCCESSFUL ~~~</h1>");
            } else {
                out.println("<h1>Incorrect Password!</h1>");
            }
        } else {
            out.println("<h1>User does not exist!</h1>");
            %><jsp:include page="Register.html" /><%
        }

    } catch (Exception e) {
        out.println("Error: " + e.getMessage());
    } finally {
        try { if (rs != null) rs.close(); } catch(Exception ex) {}
        try { if (stmt != null) stmt.close(); } catch(Exception ex) {}
        try { if (con != null) con.close(); } catch(Exception ex) {}
    }
%>
</body>
</html>
