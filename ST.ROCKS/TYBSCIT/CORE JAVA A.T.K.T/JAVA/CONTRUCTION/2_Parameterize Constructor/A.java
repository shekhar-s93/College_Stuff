class B {
    int a;
    int b;

    B(int x, int y){
        a = x;
        b = y;
    }
    B(int a, String b){
        System.err.println(a+" the name is : "+b);                
    }
    void show(){
        System.out.println(a + " " +b);
    }
}

class A {
    public static void main(String[] args) {
        B obj = new B(45, 88);
        obj.show();
        B bj = new B(19, "Shekhar");
    }
}