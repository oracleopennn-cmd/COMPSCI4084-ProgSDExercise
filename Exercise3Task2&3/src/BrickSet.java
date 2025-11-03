import java.util.Objects;

public class BrickSet {
    private int ID;
    private String name;
    private String theme;
    private int numOfPiece;
    private double retailPrice;
    public BrickSet(int ID, String name,String theme, int numOfPiece, double retailPrice){
        this.ID = ID;
        this.name = name;
        this.theme = theme;
        this.numOfPiece = numOfPiece;
        this.retailPrice = retailPrice;
    }
    public int getID(){
        return ID;
    }
    public String getName(){
        return name;
    }
    public String getTheme(){
        return theme;
    }
    public int getNumOfPiece(){
        return numOfPiece;
    }
    public double getRetailPrice(){
        return retailPrice;
    }
    public void setRetailPrice(double price){
        retailPrice = price;
    }
    @Override
    public boolean equals(Object obj) {
        BrickSet b = (BrickSet) obj;
        if(this.name == b.getName() && this.ID == b.getID() && this.theme == b.getTheme() && this.numOfPiece == b.getNumOfPiece() && this.retailPrice == b.getRetailPrice()){
            return true;
        }else{return false;}
    }
    @Override
    public int hashCode() {
        return Objects.hash(ID, name, theme, numOfPiece, retailPrice);
    }
    @Override
    public String toString() {
          return "BrickSet{" +
           "number=" + ID +
           ", name='" + name + '\'' +
           ", theme='" + theme + '\'' +
           ", pieces=" + numOfPiece +
           ", price=" + retailPrice +
           '}';
    }
    public double getPricePerPiece(){
        double res;
        res = retailPrice/(double)numOfPiece;
        return res;
    }
}
