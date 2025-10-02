
    public static void main(String[] args)
    import java.util.Scanner;
public class GradeCalculator{
    public static void main(String[] args){
         Scanner input = new Scanner(System.in); 
         String[] names = new String[5];
         int[] marks = new int[5];

         System.out.println("Welcome to my Grade Calculator");

         for(int i = 0; i < 5; i++){
            System.out.print("Enter the name: ");
            names[i] = input.nextLine();
         }
       
         for(int i = 0; i < 5; i++){
            System.out.print("Enter the marks for " + names[i] + ": ");
            marks[i] = input.nextInt();
         }

         char[] calculatedGrades = gradeCalc(names, marks);

         for(int i = 0; i < calculatedGrades.length; i++){
            System.out.println(names[i].toUpperCase() + " got the grade: " + calculatedGrades[i]);
         }
    }

    public static char[] gradeCalc(String[] studentNames, int[] studentMarks){
        System.out.println("The grade will be caculated for marks out of 500");
        char[] grades = new char[studentNames.length];

        for(int i = 0; i < studentMarks.length; i++){
            if(studentMarks[i] >= 400 && studentMarks[i] <= 500){
                grades[i] = 'A';
            }
            else if(studentMarks[i] >= 300 && studentMarks[i] < 400){
                grades[i] = 'B';
            }
            else if(studentMarks[i] >= 200 && studentMarks[i] < 300){
                grades[i] = 'C';
            }
            else if(studentMarks[i] >= 100 && studentMarks[i] < 200){
                grades[i] = 'D';
            }
            else if(studentMarks[i] >= 0 && studentMarks[i] < 100){
                grades[i] = 'F';
            }
            else {
                grades[i] = 'U';
            }
        }
        return grades;
    }
}
}