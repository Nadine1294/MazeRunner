import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class MazeSolver{

    private int dimCol;
    private int dimRow;
    private int startCol;
    private int startRow;
    private int endCol;
    private int endRow;
    private int [][] grid;
    

    public MazeSolver(int dimCol, int dimRow, int startCol, int startRow, int endCol, int endRow, int [][] grid){
        this.dimCol=dimCol;
        this.dimRow=dimRow;
        this.startCol=startCol;
        this.startRow=startRow;
        this.endCol=endCol;
        this.endRow=endRow; 
        this.grid=grid;
    }
    public MazeSolver(){

    }

    private void loadMaze(String path) {
        File file = new File(path);
        system.out.println(file);
    }

    public static void main(String[] args) {
        //MazeSolver mazeSolver = new MazeSolver();
        try{
        BufferedReader in = new BufferedReader(new FileReader("/Users/nadinedussel/MazeRunner/MazeExamples/Maze1.txt"));
        System.out.println("MazeSolver" + in);
        try {
            String [] array = new String [10];
            String line;
            int i =0;
            while(null!=(line=in.readLine())){
                array [i] = line;
                System.out.println(line);
                i++;
            }
           // System.out.println(array[4]);

        } catch (Exception e) {
            System.out.println("Fehler");
        }
        }
        catch(FileNotFoundException ex){
           System.out.println("Fehler");
        }
        //mazeSolver.loadMaze("/Users/nadinedussel/MazeRunner/MazeExamples/Maze1.txt");
        
    }
}