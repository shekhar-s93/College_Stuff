import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.net.URLEncoder;

@WebServlet("/Page1")
public class Page1 extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        String uname = request.getParameter("txtName");

        // If username not provided, use default
        if (uname == null || uname.trim().isEmpty()) {
            uname = "Guest";
        }

        String encodedName = URLEncoder.encode(uname, "UTF-8");

        // Create cookies
        Cookie ck1 = new Cookie("username", encodedName);
        Cookie ck2 = new Cookie("visit", "1");
        response.addCookie(ck1);
        response.addCookie(ck2);

        // HTML output
        out.println("<html>");
        out.println("<head><title>Page1</title></head>");
        out.println("<body bgcolor='pink'>");
        out.println("<h1>~~~ Welcome " + uname + " ~~~</h1>");
        out.println("<h1><a href='Page2'>Click to visit Page 2</a></h1>");
        out.println("</body>");
        out.println("</html>");
    }
}
