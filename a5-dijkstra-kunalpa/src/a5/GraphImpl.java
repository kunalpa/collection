
package a5;

import java.util.*;

public class GraphImpl implements Graph {
    Map<String, Node> nodes; //do not delete, use this field to store your nodes
    // key: name of node. value: a5.Node object associated with name
    ArrayList<Edge> edges;
    int nodesNum = 0;

    public GraphImpl() {
        nodes = new HashMap<>();
        edges = new ArrayList<>();
    }


    @Override
    public boolean addNode(String name) {
        Node addedNode = new NodeImpl(name);
        if (name == null || nodes.containsKey(name)) return false;
        nodes.put(name, addedNode);
        nodesNum++;
        return true;
    }

    @Override
    public boolean addEdge(String src, String dest, double weight) {
        if (nodes.containsKey(src) && nodes.containsKey(dest)) {
            if (nodes.get(src).getNextNode().contains(dest) || weight < 0) return false;
            for(Edge e : nodes.get(src).getOutEdges()){
                if(e.getdest().equals(dest)) return false;
            }
            Edge addedEdge = new EdgeImpl(src, dest, weight);
            nodes.get(src).getNextNode().add(nodes.get(dest));
            edges.add(addedEdge);
            nodes.get(src).getOutEdges().add(addedEdge);
            return true;

        }
        return false;
    }

    @Override
    public boolean deleteNode(String name) {
        if (nodes.containsKey(name)) {
            for(Node n : nodes.values()){
                deleteEdge(name, n.getName());
            }
            int count = 0;
            int size = edges.size();
            for (int i = 0; i < size; i++) {
                if (edges.get(count).getsrc().equals(name) || edges.get(count).getdest().equals(name)) {
                    edges.remove(count);
                } else {
                    count++;
                }
            }
            nodes.get(name).setHandled(true);
            nodes.get(name).getNextNode().clear();
            nodes.remove(name);
            nodesNum--;
            return true;
        }
        return false;
    }

    @Override
    public boolean deleteEdge(String src, String dest) {
        if (src != null && dest != null) {
            if (nodes.containsKey(src) && nodes.containsKey(dest)) {
                if (nodes.get(src).getNextNode().contains(nodes.get(dest))) {
                    int index = nodes.get(src).getNextNode().indexOf(nodes.get(dest));
                    nodes.get(src).getNextNode().remove(nodes.get(dest));
                    nodes.get(src).getOutEdges().remove(index);
                    int size = edges.size();
                    int count = 0;
                    for (int i = 0; i < size; i++) {
                        if (edges.get(count).getdest().equals(dest) && edges.get(count).getsrc().equals(src)) {
                            edges.remove(count);
                        } else count++;
                    }
                    return true;
                }
            }
        }
        return false;
    }

    @Override
    public int numNodes() {
        return nodesNum;
    }

    @Override
    public int numEdges() {
        return edges.size();
    }

    @Override
    public Map<String, Double> dijkstra(String start) {
        Map<String, Double> distanceMap = new HashMap<>();
        PriorityQueue<String> queue = new PriorityQueue<>();
        nodes.get(start).setDistance(0.0);
        distanceMap.put(start, 0.0);
        queue.add(nodes.get(start).getName());
        nodes.get(start).setHandled(true);


        while (!queue.isEmpty()) {
            String u = queue.poll();
            for(Edge e : nodes.get(u).getOutEdges()){
                Node n = nodes.get(e.getdest());
                if(n != null){
                    if(!n.getHandled()) {
                        double newDist = nodes.get(u).getDistance() + e.getWeight();
                        if (!distanceMap.containsKey(n)) {
                            distanceMap.put(e.getdest(), nodes.get(e.getdest()).getDistance());
                        }
                        if (newDist < n.getDistance()) {
                            n.setDistance(newDist);
                            queue.add(n.getName());
                            distanceMap.replace(e.getdest(), newDist);
                        }
                    }
                }
            }
        }

        return distanceMap;
    }
}