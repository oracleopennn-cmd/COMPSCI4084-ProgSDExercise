import java.util.ArrayList;
import java.util.List;

public class Bin {
    private int capacity;
    List<Integer> contents;
    public Bin(int c){
        this.capacity = c;
        this.contents = new ArrayList<>();
    }
    public int getSpace(){
        int res = 0;
        for (int t:contents){
            res += t;
        }
        return capacity - res;
    }
    public void store(int value) throws IllegalArgumentException{
        if(value > getSpace()){
            throw new IllegalArgumentException("No space: space " 
+ getSpace() + ", size " + value); 
        }else{
            contents.add(value);
        }
    }
    @Override
    public String toString(){
        return contents.toString();
    }
    
}
