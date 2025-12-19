import java.io.*;
import java.sql.*;
import jakarta.servlet.*;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;

@WebServlet("/QuizServlet")
public class QuizServlet extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        out.println("<form action='ShowResult' method='post'>");

        try {
            // Load MySQL Driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Connect to Database
            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/qadb", "root", "test");

            Statement stmt = con.createStatement();
            ResultSet res = stmt.executeQuery("SELECT * FROM quiz");

            out.println("<table border='1' cellpadding='10'>");

            int qno = 0;
            while (res.next()) {
                qno++;

                // Question
                out.println("<tr><td colspan='2'><b>Q" + qno + ". " + res.getString("question") + "</b></td></tr>");

                // Options
                out.println("<tr><td><input type='radio' name='" + qno + "' value='" 
                        + res.getString("op1") + "'></td><td>" + res.getString("op1") + "</td></tr>");

                out.println("<tr><td><input type='radio' name='" + qno + "' value='" 
                        + res.getString("op2") + "'></td><td>" + res.getString("op2") + "</td></tr>");

                out.println("<tr><td><input type='radio' name='" + qno + "' value='" 
                        + res.getString("op3") + "'></td><td>" + res.getString("op3") + "</td></tr>");

                out.println("<tr><td><input type='radio' name='" + qno + "' value='" 
                        + res.getString("op4") + "'></td><td>" + res.getString("op4") + "</td></tr>");
            }

            out.println("</table>");
            out.println("<br><input type='reset'>");
            out.println("<input type='submit' value='SUBMIT'>");

            stmt.close();
            con.close();

        } catch (Exception e) {
            out.println("<h1>Error: " + e.getMessage() + "</h1>");
        }

        out.println("</form>");
    }
}
