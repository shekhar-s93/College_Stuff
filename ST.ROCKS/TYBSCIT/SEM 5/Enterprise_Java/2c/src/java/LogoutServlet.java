import java.io.*;
import jakarta.servlet.*;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;

@WebServlet("/LogoutServlet")
public class LogoutServlet extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        out.println("<html><head><title>Logout</title></head>");
        out.println("<body bgcolor='lightgrey'>");

        // Get the session; if exists, invalidate
        HttpSession hs = request.getSession(false);
        if (hs != null) {
            hs.invalidate();
        }

        out.println("<h1>You are logged out successfully.</h1>");
        out.println("<h2><a href='index.html'>Go back to Login Page</a></h2>");

        out.println("</body></html>");
    }
}
