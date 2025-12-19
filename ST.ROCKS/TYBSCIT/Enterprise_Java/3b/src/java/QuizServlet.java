import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

@WebServlet("/QuizServlet")
public class QuizServlet extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        out.println("<html><head><title>Quiz</title></head><body>");
        out.println("<h1>Welcome to the Quiz!</h1>");
        out.println("<form action='ShowResult' method='post'>"); // Use POST for form submission

        try {
            // Load MySQL Driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // Connect to Database (replace password if needed)
            Connection con = DriverManager.getConnection(
                    "jdbc:mysql://localhost:3306/qadb", "root", "test");

            Statement stmt = con.createStatement();
            ResultSet res = stmt.executeQuery("SELECT * FROM quiz");

            out.println("<table border='1' cellpadding='10'>");

            int qno = 0;
            while (res.next()) {
                qno++;

                // Question
                out.println("<tr><td colspan='2'><b>Q" + qno + ". " + res.getString("Question") + "</b></td></tr>");

                // Options
                out.println("<tr><td><input type='radio' name='" + qno + "' value='"
                        + res.getString("Op1") + "'></td><td>" + res.getString("Op1") + "</td></tr>");

                out.println("<tr><td><input type='radio' name='" + qno + "' value='"
                        + res.getString("Op2") + "'></td><td>" + res.getString("Op2") + "</td></tr>");

                out.println("<tr><td><input type='radio' name='" + qno + "' value='"
                        + res.getString("Op3") + "'></td><td>" + res.getString("Op3") + "</td></tr>");

                out.println("<tr><td><input type='radio' name='" + qno + "' value='"
                        + res.getString("Op4") + "'></td><td>" + res.getString("Op4") + "</td></tr>");
            }

            out.println("</table>");
            out.println("<br><input type='reset'>");
            out.println("<input type='submit' value='SUBMIT'>");

            stmt.close();
            con.close();

        } catch (Exception e) {
            out.println("<h1>Error: " + e.getMessage() + "</h1>");
        }

        out.println("</form></body></html>");
    }
}
