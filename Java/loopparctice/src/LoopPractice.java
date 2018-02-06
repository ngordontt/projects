public class LoopPractice {
    public static void practiceWhileLoop(){
        int x =0;
        while(x<5){
            System.out.println("The valuie of x is " + x);
            x++;
        }
    }

    public static void practiceDoWhileLoop(){
        int x =0;
        do{
            System.out.println("The valuie of x is " + x);
            x++;
        } while (x<10);
    }

    public static void main(String[] args) {

        practiceWhileLoop();
        practiceDoWhileLoop();
    }
}
