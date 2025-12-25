class A {
    int a;
    String name;
    
    A() {
        a = 32;
        name = null;
    }
    void show() {
        System.out.print(a + " " + name);
    }
}

class first {
    public static void main(String[] args){
        A obj = new A();
        obj.show();
    }
}