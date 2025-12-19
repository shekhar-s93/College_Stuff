package mypack;

public class CheckerBean {
    private String username;
    private String password;

    // Getters & Setters
    public String getUsername() {
        return username;
    }
    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }
    public void setPassword(String password) {
        this.password = password;
    }

    // Validation method
    public boolean validate() {
        return "admin".equals(username) && "admin".equals(password);
    }
}
