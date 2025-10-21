import java.util.Random;
import java.util.Scanner;
public class GamePlayer {
    public Symbol selectSymbol(){
        System.out.println("选择你出什么？ 1是剪刀 2是石头 3是布");
        Scanner s = new Scanner(System.in);
        int i = s.nextInt();
        switch (i) {
            case 1:
                return Symbol.SCISSORS;
            case 2:
                return Symbol.ROCK;
            case 3:
                return Symbol.PAPER;
        }
        return null;
    }
    public Symbol getSymbol(){
        int i;
        Random r = new Random();
        i = r.nextInt(3);
        switch (i) {
            case 0:
                return Symbol.PAPER;
            case 1:
                return Symbol.ROCK;
            case 2:
                return Symbol.SCISSORS;
        }
        return null;
    }
}
