<%@page contentType="text/html" import="java.sql.*"%>
<html>
<body>
<h1>Registration JSP Page</h1>
<%
    String uname = request.getParameter("txtName");
    String pass1 = request.getParameter("txtPass1");
    String pass2 = request.getParameter("txtPass2");
    String email = request.getParameter("txtEmail");
    String ctry  = request.getParameter("txtCon");

    if (pass1 != null && pass1.equals(pass2)) {
        Connection con = null;
        PreparedStatement stmt = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver"); 
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/logindb", "root", "test");

            // Better: mention column names
            stmt = con.prepareStatement("INSERT INTO user (Username, Password, Email, Country) VALUES (?,?,?,?)");
            stmt.setString(1, uname);
            stmt.setString(2, pass1);
            stmt.setString(3, email);
            stmt.setString(4, ctry);

            int row = stmt.executeUpdate();
            if (row == 1) {
                out.println("<h2>Registration Successful</h2>");
            } else {
                out.println("<h2>Registration Failed</h2>");
                %><jsp:include page="Register.html" /><%
            }
        } catch (Exception e) {
            out.println("Error: " + e.getMessage());
        } finally {
            try { if (stmt != null) stmt.close(); } catch(Exception ex){}
            try { if (con != null) con.close(); } catch(Exception ex){}
        }
    } else {
        out.println("<h2>Password Mismatch</h2>");
        %><jsp:include page="Register.html" /><%
    }
%>
</body>
</html>
