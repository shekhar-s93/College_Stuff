class first {
    int a = 32;
    int b = 66;
    int c = a+b;

    void show(){
        System.out.print(c);
    }
}

class Practice{
    public static void main(String[] args) {
        first obj = new first();
        obj.show();
    }
}