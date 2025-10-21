public class Monster {
    private String type;
    private int hitPoints;
    private int atkPoints;
    private String[] weaknesses = new String[100];
    Monster(String type, int hit_points, int atk_points, String[] weaknesses){
        this.type = type;
        this.hitPoints = hit_points;
        this.atkPoints = atk_points;
        this.weaknesses = weaknesses;
    }
    public String getType(){
        return type;
    }
    public int getHitPoints(){
        return hitPoints;
    }
    public int getAtkPoints(){
        return hitPoints;
    }
    public String[] getWeaknesses(){
        return weaknesses;
    }
    public Boolean isWeakPoint(String otherType){
        boolean isWKPT = false;
        for (String k : weaknesses) {
             if(k.equals(otherType)){
                isWKPT = true;
                break;
             }  
        } 
        return isWKPT;
    }
    public void removeHitPoints (int pointsToRemove) {
        if(hitPoints>0){hitPoints -= pointsToRemove;}
        if(hitPoints<=0){hitPoints = 0;}
    }
    public boolean attack(Monster otherMonster){
        //如果目标是自己
        if(otherMonster==this){
            return false;
        }
        //如果自己或者对方HP为0
        if(this.hitPoints==0 || otherMonster.hitPoints==0){
            return false;
        }
        //是否是弱点攻击并计算移除的HP
        if(otherMonster.isWeakPoint(this.type)){
            otherMonster.removeHitPoints(this.atkPoints + 20);
        }else{
            otherMonster.removeHitPoints(this.atkPoints);
        }
        return true;
    }

}
