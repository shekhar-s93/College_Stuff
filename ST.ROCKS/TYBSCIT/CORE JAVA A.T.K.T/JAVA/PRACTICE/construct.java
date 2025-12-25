class First {
    int a;
    int b;
    String name;
    int d;

    First() {
        a = 100;
        b = 2849;
        d = a + b;
        name = "Shekhar Suman";
    }

    void show() {
        System.out.print("The addition of A and B : "+d+ " " + ", and the name of Performer is : "+name);
    }
    
}

class construct{
    public static void main(String[] args) {
        First obj = new First();
        obj.show();
    }
}