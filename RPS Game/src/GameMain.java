import java.util.Scanner;

public class GameMain {
    private int CPU_SCORE = 0;
    private int HUM_SCORE = 0;
    public void printScore(){
        System.out.println("人类得分为： "+HUM_SCORE);
        System.out.println("电脑得分为： "+CPU_SCORE);
    }
    public void gameRun(){
        Scanner s = new Scanner(System.in);
        System.out.println("你想玩几轮?");
        int round = s.nextInt();
        GamePlayer CPU = new GamePlayer();
        GamePlayer HUM = new GamePlayer();
        for(int i = 0;i<round;i++){
            Symbol hum = HUM.selectSymbol();
            Symbol cpu = CPU.getSymbol();
            if(hum.getResult(cpu) == GameResult.DROW){
                continue;
            }else if(hum.getResult(cpu) == GameResult.WIN){
                HUM_SCORE++;
            }else{
                CPU_SCORE++;
            }
        }
        printScore();
    }
}
