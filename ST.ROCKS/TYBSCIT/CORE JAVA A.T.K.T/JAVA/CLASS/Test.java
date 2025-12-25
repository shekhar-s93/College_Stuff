class Demo {
    int a = 32;
    String b = "Shekhar Suman";

    void show() {
        System.out.print(a + " " + b);
    }
}

class Shekhar {
    String c = "Fucking Shreya";
    int d = 97400;

    void show() {
        System.out.println(c + d);
    }
}

// Now we have to defining the object in the core java programming Language.

class Test{ // here the class name should be as the file name.
    public static void main(String[] args) {
        Demo r=new Demo();
        r.show();

        Shekhar r2;
        r2=new Shekhar();
        r2.show();
    }
}

