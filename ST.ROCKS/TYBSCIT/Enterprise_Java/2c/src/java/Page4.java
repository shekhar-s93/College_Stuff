import java.io.*;
import jakarta.servlet.*;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;

@WebServlet("/Page4")
public class Page4 extends HttpServlet {

    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        out.println("<html><head><title>Servlet Page4</title></head>");
        out.println("<body bgcolor=orange>");

        HttpSession hs = request.getSession(false);

        if (hs == null) {
            out.println("<h1>No active session. Please <a href=index.html>login again</a>.</h1>");
        } else {
            int visit = Integer.parseInt((String) hs.getAttribute("visit")) + 1;
            hs.setAttribute("visit", String.valueOf(visit));
            String uname = (String) hs.getAttribute("uname");

            out.println("<h1>Welcome " + uname + " to Page 4</h1>");
            out.println("<h1>You Visited " + visit + " Times</h1>");
            out.println("<h1>Session ID: " + hs.getId() + "</h1>");
        }

        out.println("<h2><a href=Page1>Go to Page 1</a></h2>");
        out.println("<h2><a href=Page2>Go to Page 2</a></h2>");
        out.println("<h2><a href=Page3>Go to Page 3</a></h2>");
        out.println("<h2><a href=Page5>Go to Page 5</a></h2>");
        out.println("<h2><a href=LogoutServlet>Terminate Session</a></h2>");

        out.println("</body></html>");
    }
}

