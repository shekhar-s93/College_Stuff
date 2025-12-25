class B{
    int a; String b; boolean c;
    
    B(){
        a = 100; b = "Shekhar"; c = true;
    }

    void Disp() {
        System.out.print(a+ " " + b + " " + c);
    }
}

class A{
    public static void main(String[] args){
        B obj = new B();
        obj.Disp();
    }
}