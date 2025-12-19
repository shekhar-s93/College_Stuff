import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/CalculatorServlet")
public class CalculatorServlet extends HttpServlet {

    @Override
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();

        out.println("<html><head><title>Calculator Result</title></head><body>");

        try {
            double n1 = Double.parseDouble(request.getParameter("txtN1"));
            double n2 = Double.parseDouble(request.getParameter("txtN2"));
            String opr = request.getParameter("opr");

            double result = 0;
            String operation = "";

            if (opr.equals("+")) {
                result = n1 + n2;
                operation = "Addition";
            } else if (opr.equals("-")) {
                result = n1 - n2;
                operation = "Subtraction";
            } else if (opr.equals("*")) {
                result = n1 * n2;
                operation = "Multiplication";
            } else if (opr.equals("/")) {
                if (n2 != 0) {
                    result = n1 / n2;
                    operation = "Division";
                } else {
                    out.println("<h3>Error: Division by zero is not allowed.</h3>");
                    out.println("</body></html>");
                    return;
                }
            }

            out.println("<h2>Operation: " + operation + "</h2>");
            out.println("<h2>Result = " + result + "</h2>");
        } catch (NumberFormatException e) {
            out.println("<h3>Error: Please enter valid numbers.</h3>");
        }

        out.println("</body></html>");
    }
}
