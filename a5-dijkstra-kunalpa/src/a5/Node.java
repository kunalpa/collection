
package a5;

import java.util.*;
import java.util.HashMap;

public interface Node extends Comparable<Node> {
     /**
      * @return the name of the node
      */

     String getName();
     double getDistance();
     void setDistance(double dist);
     ArrayList<Node> getNextNode();
     ArrayList<Edge> getOutEdges();
     boolean getHandled();
     void setHandled(boolean bool);
     int compareTo(Node n);
}
