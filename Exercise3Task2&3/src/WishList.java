import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class WishList {
    private List<BrickSet> toys;
    public WishList(){
        toys = new ArrayList<>();
    }
    public Collection<BrickSet>getSets(){
        List<Integer> a = new ArrayList<>();
        for(BrickSet s : toys){
            a.add(s.getID());
        } 
        Collections.sort(a);
        List<BrickSet> res = new ArrayList<>();
        for(int s : a){
            for(BrickSet m : toys){
                if(s == m.getID()){
                    res.add(m);
                }
            }
        }
        return res;
    }
    public boolean addSet(BrickSet s){
        for(BrickSet t:toys){
            if(t.equals(s)){return false;}
        }
        toys.add(s);
        return true;
    }
    public boolean removeSet(BrickSet s){
        for (BrickSet t:toys){
            if(t.equals(s)){
                toys.remove(s);
                return true;
            }
        }
        return false;
    }    
}
