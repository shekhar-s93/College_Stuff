class B {
    int a; String b;

    B(){
        a = 10; b = "Anything";
        System.out.println(a+" "+b);
    }
    B(B ref){
        a = ref.a;
        b = ref.b;
        System.out.println(a+" "+b);
    }
}

class A{
    public static void main(String[] args) {
        B r = new B();
        B r2 = new B(r);
    }
}