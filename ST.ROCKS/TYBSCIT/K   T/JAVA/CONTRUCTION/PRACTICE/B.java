class A{
    int a; String b;

    A(){
        a = 19;
        b = "Shekhar";
        System.out.println("Your name is: "+b+", and your age is : "+a);
    }
    A(A cpy){
        a = cpy.a;
        b = cpy.b;
        System.out.println("Your name is: "+b+", and your age is : "+a);
    }
}

class B{
    public static void main(String[] args) {
        A ob = new A();
        A obj = new A(ob);
        
    }
}