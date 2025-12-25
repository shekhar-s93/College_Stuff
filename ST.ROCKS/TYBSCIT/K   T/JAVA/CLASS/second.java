class second_class {
    int age;
    int b;
    double c;
    String name;
    String Class;

    second_class() {
        age = 18;
        b = 79;
        c = 999.00;
        name = "Shekhar Suman";
        Class = "B.sc.I.T";
    }

    void show(){
        System.out.print("Your name is : " + name + ", and your age is : "+age+", you are persuing : "+Class);
    }
}

class second{
    public static void main(String[] args) {
        second_class obj = new second_class();
        obj.show();
    }
}