import java.io.*;
import jakarta.servlet.*;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;

@WebServlet("/Page2")
public class Page2 extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        out.println("<html><head><title>Servlet Page2</title></head>");
        out.println("<body bgcolor='lightblue'>");

        HttpSession hs = request.getSession(false);

        if (hs == null) {
            out.println("<h1>No active session. Please <a href='index.html'>login again</a>.</h1>");
        } else {
            int visit = Integer.parseInt((String) hs.getAttribute("visit")) + 1;
            hs.setAttribute("visit", String.valueOf(visit));

            out.println("<h1>Welcome Again, " + hs.getAttribute("uname") + "</h1>");
            out.println("<h1>You Visited " + visit + " Times</h1>");
            out.println("<h1>Your Session ID: " + hs.getId() + "</h1>");
            out.println("<h1>You Logged in at: " + new java.util.Date(hs.getCreationTime()) + "</h1>");
        }

        out.println("<h2><a href='Page1'>Back to Page 1</a></h2>");
        out.println("<h2><a href='Page3'>Go to Page 3</a></h2>");
        out.println("<h2><a href='Page4'>Go to Page 4</a></h2>");
        out.println("<h2><a href='LogoutServlet'>Terminate Session</a></h2>");

        out.println("</body></html>");
    }
}
