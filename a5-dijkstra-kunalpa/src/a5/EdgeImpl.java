package a5;

public class EdgeImpl implements Edge{
    private final String src;
    private final String dest;
    private final double weight;


    public EdgeImpl(String src, String dest){
        this(src, dest, 1);
    }

    public EdgeImpl(String src, String dest, double weight){
        this.weight = weight;
        this.src = src;
        this.dest = dest;
    }

    @Override
    public double getWeight() { return this.weight; }

    public String getsrc() {return this.src;}

    public String getdest() {return this.dest;}

}