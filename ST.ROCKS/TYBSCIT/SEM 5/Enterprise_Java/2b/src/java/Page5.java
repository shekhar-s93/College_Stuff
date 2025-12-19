import java.io.IOException;
import java.io.PrintWriter;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.URLDecoder;

@WebServlet("/Page5")
public class Page5 extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        out.println("<html><head><title>Page5</title></head>");
        out.println("<body bgcolor='lightblue'>");

        Cookie[] ck = request.getCookies();
        if (ck != null) {
            for (int i = 0; i < ck.length; i++) {
                if (ck[i].getName().equals("visit")) {
                    int count = Integer.parseInt(ck[i].getValue()) + 1;
                    out.println("<h1>Visit No: " + count + "</h1>");
                    ck[i] = new Cookie("visit", count + "");
                    response.addCookie(ck[i]);
                } else if (ck[i].getName().equals("username")) {
                    String decodedName = URLDecoder.decode(ck[i].getValue(), "UTF-8");
                    out.println("<h2>User: " + decodedName + "</h2>");
                }
            }
        }

        out.println("<h1><a href='Page1'>Back to Page 1</a></h1>");
        out.println("<h1><a href='Page2'>Back to Page 2</a></h1>");

        out.println("</body></html>");
    }
}
