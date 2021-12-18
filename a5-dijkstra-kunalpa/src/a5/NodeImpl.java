
package a5;

import java.util.*;

public class NodeImpl implements Node {
    private final String value;
    private double distance;
    private ArrayList<Node> nextNode = new ArrayList<>();
    private ArrayList<Edge> outEdge = new ArrayList<>();
    private boolean handled = false;

    public NodeImpl(String value){
        this.value = value;
        this.distance = Double.MAX_VALUE;
    }

    @Override
    public String getName() {
        return this.value;
    }

    public double getDistance(){ return this.distance; }

    public void setDistance(double dist){ this.distance = dist; }

    public ArrayList<Node> getNextNode() { return this.nextNode; }

    @Override
    public ArrayList<Edge> getOutEdges() {
        return this.outEdge;
    }

    public boolean getHandled(){
        return this.handled;
    }
    public void setHandled(boolean bool){
        this.handled = bool;
    }

    @Override
    public int compareTo(Node n) {
        if(this.distance < n.getDistance()){
            return -1;
        }
        else if(this.distance > n.getDistance()){
            return 1;
        }
        else{ return 0; }
    }
}