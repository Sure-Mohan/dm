import java.util.*;

public class SimulatedDataset {
    public static void main(String[] args) {
        System.out.println("RollNo\tName\tMarks");
        int[] rollNo = {1, 2, 3, 4, 5};
        String[] name = {"Asha", "Ravi", "Neha", "Kiran", "Raju"};
        int[] marks = {80, 70, 90, 85, 75};
        for (int i = 0; i < rollNo.length; i++) {
            System.out.println(rollNo[i] + "\t" + name[i] + "\t" + marks[i]);
        }
    }
}
