// COPY CONSTRUCTOR

class B {
    int a; int b;

    B(){
        a = 3289;
        b = 833998;
        System.out.println(a+" "+b);
    }

    B(B cpy){
        a = cpy.a;
        b = cpy.b;
        System.out.println(a+" "+b);
    }
}

class a{
    public static void main(String[] args) {
        B obj = new B();
        B object = new B(obj);
    }
}