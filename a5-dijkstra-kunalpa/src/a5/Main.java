package a5;

public class Main {
    public static void main(String[] args) {
        Graph connectedGraph = new GraphImpl();
        connectedGraph.addNode("a");
        connectedGraph.addNode("b");
        connectedGraph.addNode("c");
        connectedGraph.addNode("d");
        connectedGraph.addNode("e");
        connectedGraph.addNode("f");
        connectedGraph.addEdge("d", "c",2);
        connectedGraph.addEdge("a", "b",2);
        connectedGraph.addEdge("a", "c",4);
        connectedGraph.addEdge("c","a",1);
        connectedGraph.addEdge("b", "c",1);
        connectedGraph.addEdge("c", "e",3);
        connectedGraph.addEdge("e", "d",2);
        connectedGraph.addEdge("b", "d",7);
        connectedGraph.addEdge("d", "f",1);
        connectedGraph.addEdge("e", "f",5);
        System.out.println(connectedGraph.deleteEdge("d","f"));
        //connectedGraph.addEdge("hello", "world",3);
        //System.out.println(connectedGraph.addEdge("world", "hello",3));
        //connectedGraph.addEdge("peanut", "world",3);
        //System.out.println(connectedGraph.deleteNode("hello"));
        //System.out.println(connectedGraph.numNodes());
        //System.out.println(connectedGraph.deleteNode("hello"));
        System.out.println(connectedGraph.dijkstra("a"));
        //connectedGraph.deleteNode("peanut");
        //System.out.println(connectedGraph.deleteEdge("world", "hello"));


        //System.out.println(connectedGraph.numEdges());
        //connectedGraph.deleteNode("peanut");
        //System.out.println(connectedGraph.addEdge("hello", "world", 2));
        //System.out.println(connectedGraph.addEdge("hello", "peanut",3));
        //System.out.println(connectedGraph.addEdge("hello", "peanut", 1));
        //System.out.println(connectedGraph.deleteEdge("hello","peanut"));
        System.out.println(connectedGraph.numEdges());
        //System.out.println(connectedGraph.numEdges());
    }
}
