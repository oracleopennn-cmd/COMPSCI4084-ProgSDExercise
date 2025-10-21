//import java.lang.Math as Math;

import java.lang.classfile.instruction.SwitchCase;
import java.util.HashMap;
import java.util.Map;

public class myfirstclass {
    //写一个程序，计算出给定int以下所有的素数,并打印
    public static void printPrimes (int max){
        for (int i = 2; i < max; i++){
            boolean isPrime = true;
            for (int j = 2; j <= Math.sqrt(i); j++){
                if (i % j == 0){
                    isPrime = false;
                    break;
                }
            }
            if (isPrime){
                System.out.println(i);
            }
        }
    }
    //写一个程序，斐波那契数列
    public static int computeFibonacci(int n){
        int res = 0;
        int a = 0;
        int b = 1;
        int i = 2;
        if(n==1)
        {
            res = 0;
        }
        else if(n==1)
        {
            res = 1;
        }
        else{
            while(i<n){
                res = a + b;
                a = b;
                b = res;
                i++;
            }
        }
        return res;
    }
    //写一个程序，根据输入的单词返回分数
    public static int ComputeScore(String word){
        int score = 0;
        //输入“字母：分数”表
        Map<Character,Integer> alphabet = new HashMap<>();
        alphabet.put('A', 1);
        alphabet.put('B', 3);
        alphabet.put('C', 3);
        alphabet.put('D', 2);
        alphabet.put('E', 1);
        alphabet.put('F', 4);
        alphabet.put('G', 2);
        alphabet.put('H', 4);
        alphabet.put('I', 1);
        alphabet.put('J', 8);
        alphabet.put('K', 5);
        alphabet.put('L', 1);
        alphabet.put('M', 3);
        alphabet.put('N', 1);
        alphabet.put('O', 1);
        alphabet.put('P', 3);
        alphabet.put('Q', 10);
        alphabet.put('R', 1);
        alphabet.put('S', 1);
        alphabet.put('T', 1);
        alphabet.put('U', 1);
        alphabet.put('V', 4);
        alphabet.put('W', 4);
        alphabet.put('X', 8);
        alphabet.put('Y', 4);
        alphabet.put('Z', 10);
        for (int i=0;i<word.length();i++){
            char C = Character.toUpperCase(word.charAt(i));
            if(alphabet.containsKey(C)){
                score+=alphabet.get(C);
            }

        }


        return score;
    }
    public static void main(String[] args) {
        int score = ComputeScore("Quit");
        System.out.println(score);
    }
}
