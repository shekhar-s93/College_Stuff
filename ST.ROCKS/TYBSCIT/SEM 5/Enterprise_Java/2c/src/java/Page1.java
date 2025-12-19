import java.io.*;
import jakarta.servlet.*;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.*;

@WebServlet("/Page1")
public class Page1 extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        out.println("<html><head><title>Servlet Page1</title></head>");
        out.println("<body bgcolor='yellow'>");

        HttpSession hs = request.getSession(true);

        if (hs.isNew()) {
            String name = request.getParameter("txtName");
            hs.setAttribute("uname", name);
            hs.setAttribute("visit", "1");

            out.println("<h1>Welcome First Time, " + name + "</h1>");
        } else {
            out.println("<h1>Welcome Again</h1>");
            int visit = Integer.parseInt((String) hs.getAttribute("visit")) + 1;
            hs.setAttribute("visit", String.valueOf(visit));
            out.println("<h1>You Visited " + visit + " Times</h1>");
        }

        out.println("<h2><a href='Page2'>Go to Page 2</a></h2>");
        out.println("<h2><a href='LogoutServlet'>Terminate Session</a></h2>");
        out.println("</body></html>");
    }
}
