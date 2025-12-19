import java.io.*;
import jakarta.servlet.*;
import jakarta.servlet.http.*;
import jakarta.servlet.annotation.WebServlet;

@WebServlet("/LoginServlet")
public class LoginServlet extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        String uname = request.getParameter("txtId");   // user ID
        String upass = request.getParameter("txtPass"); // password

        out.println("<html><head><title>Servlet LoginServlet</title></head>");

        if ("Shekhar".equals(uname) && "12345".equals(upass)) {
            out.println("<body bgcolor='blue'>");
            out.println("<h1>Welcome !!! " + uname + "</h1>");
        } else {
            out.println("<body bgcolor='red'>");
            out.println("<h1>Login Fail !!!</h1>");
        }

        out.println("</body></html>");
    }
}
