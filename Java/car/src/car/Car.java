package car;

public class Car {

    int MaxSpeed= 100;
    int MinSpeed = 0;

    double weight = 4079;

    boolean isTheCarOn = false;
    char condition;
    String nameOfCar;

    double maxfuel = 16;
    double currentFuel =8;
    double mpg  =  26.4;

    int numberOfPeople = 1;

    public Car() {
        condition = 'a';
        nameOfCar = "Lucy";
    }

    public double getMaxfuel(){
        return this.maxfuel;
    }


    public  void  printVariables(){
        System.out.println(MaxSpeed);
        System.out.println(MinSpeed);
        System.out.println(weight);
        System.out.println(condition);
        System.out.println(isTheCarOn);
    }

    public  void wreckCar(){
        condition = 'c';
    }

    public static void main(String[] args){
        Car familyCar = new Car();
        familyCar.printVariables();
        Car aliceCar = familyCar;
        familyCar.wreckCar();
        System.out.println("Alice car: ");
        aliceCar.printVariables();
 }


}

