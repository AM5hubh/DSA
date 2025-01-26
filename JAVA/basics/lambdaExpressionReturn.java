package basics;

@FunctionalInterface
interface B {
    int add(int i, int j);
}

public class lambdaExpressionReturn {
    public static void main(String a[]) {
        B obj = (i, j) -> i + j;

        int result = obj.add(5, 4);
        System.out.println(result);
    }
}
