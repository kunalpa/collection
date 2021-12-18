# A5-Dijkstra

For this assignment you will be creating your own Directed Graph and performing Dijkstra's Algorithm
on the graph. This assignment is less structured than others and gives you the freedom to implement
the graph however you choose. The graded portion of the assignment will be the GraphImpl.java class. 
The behind the scenes of your graph are not tested, as long as the methods in GraphImpl.java function correctly.
You are welcome to create a Main class to test your code. 

## Edge.java

The Edge interface is empty. It is your job to come up with the methods that you think an Edge object
should have in order to create a graph and run Dijkstra. Write out the method signatures in
the Edge.java interface and implement those methods in EdgeImpl.java. 
To know what properties an Edge contains, take a look at the createEdge method in GraphImpl.java
 
 
## Node.java

The Node.java interface currently only has one method, getName(). This method should return the name
associated with the Node. Do not remove this method since it is used for testing. Your task is to
add the remaining methods that you think a Node needs in order to complete Dijkstra's Algorithm.
The addNode() method in GraphImpl.java shows what fields a Node has. These fields are the minimum
required, you may add any other fields that you may think are useful. 

## Graph.java

The interface Graph.java has all the methods needed for a graph. This interface is complete, do not 
change any of the methods within it. You may add helper methods if needed in GraphImpl.java. You 
must implement all the methods in this interface.  