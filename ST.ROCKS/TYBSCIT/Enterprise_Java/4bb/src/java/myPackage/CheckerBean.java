package myPackage;

public class CheckerBean {
    private String name, age, hob, email, gender, error;
    
    public CheckerBean() {
        error = "";
    }
    
    // Setter methods
    public void setName(String n) {
        name = n;
    }
    
    public void setAge(String a) {
        age = a;
    }
    
    public void setHob(String h) {
        hob = h;
    }
    
    public void setEmail(String e) {
        email = e;
    }
    
    public void setGender(String g) {
        gender = g;
    }
    
    public void setError(String e) {
        error = e;
    }
    
    // Getter methods
    public String getName() {
        return name;
    }
    
    public String getAge() {
        return age;
    }
    
    public String getHob() {
        return hob;
    }
    
    public String getEmail() {
        return email;
    }
    
    public String getGender() {
        return gender;
    }
    
    public String getError() {
        return error;
    }
    
    // Validation method
    public boolean validate() {
        boolean res = true;
        error = ""; // Reset error messages
        
        // Name validation
        if (name == null || name.trim().equals("")) {
            error += "Enter First Name. ";
            res = false;
        }
        
        // Age validation
        if (age == null || age.trim().equals("")) {
            error += "Age is required. ";
            res = false;
        } else if (age.length() > 2) {
            error += "Age Invalid (too many digits). ";
            res = false;
        } else {
            try {
                int ageValue = Integer.parseInt(age);
                if (ageValue <= 0 || ageValue > 150) {
                    error += "Age must be between 1 and 150. ";
                    res = false;
                }
            } catch (NumberFormatException e) {
                error += "Age must be a valid number. ";
                res = false;
            }
        }
        
        // Email validation
        if (email == null || email.trim().equals("")) {
            error += "Email is required. ";
            res = false;
        } else if (!email.contains("@") || !email.contains(".")) {
            error += "Email format is invalid. ";
            res = false;
        }
        
        // Gender validation
        if (gender == null || gender.trim().equals("")) {
            error += "Gender is required. ";
            res = false;
        }
        
        // Hobby validation
        if (hob == null || hob.trim().equals("")) {
            error += "Hobby is required. ";
            res = false;
        }
        
        return res;
    }
}