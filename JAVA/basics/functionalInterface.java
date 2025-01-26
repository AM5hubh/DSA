package basics;

@FunctionalInterface
interface A {
    void show(int i);
}

public class functionalInterface {
    public static void main(String args[]) {

        // A obj = new A() {
        // public void show(int i) {
        // System.out.println("in show "+i);
        // }
        // };
        A obj = i -> System.out.println("in show "+ i);   //lambda expression
        obj.show(5);
    }

}