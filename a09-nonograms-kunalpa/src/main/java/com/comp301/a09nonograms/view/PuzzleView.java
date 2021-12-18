package com.comp301.a09nonograms.view;

import com.comp301.a09nonograms.controller.Controller;
import javafx.scene.Parent;
import javafx.scene.control.Button;
import javafx.scene.input.MouseButton;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Paint;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Text;

public class PuzzleView implements FXComponent {

  Controller controller;

  public PuzzleView(Controller controller) {
    this.controller = controller;
  }

  private int getMax(int[] arr) { // helper method
    int max = 0;
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] > max) {
        max = arr[i];
      }
    }
    return max;
  }

  @Override
  public Parent render() {
    GridPane grid = new GridPane();
    for (int i = 0; i < controller.getClues().getHeight(); i++) {
      for (int j = 0; j < controller.getClues().getWidth(); j++) {
        int finalJ = j;
        int finalI = i;
        Rectangle rectangle = new Rectangle(30, 30);
        if (controller.isEliminated(i, j)) {
          rectangle.setFill(Paint.valueOf("red"));
        } else if (controller.isShaded(i, j)) {
          rectangle.setFill(Paint.valueOf("black"));
        } else {
          rectangle.setFill(Paint.valueOf("white"));
        }
        rectangle.setOnMouseClicked(
            event -> {
              if (event.getButton() == MouseButton.SECONDARY) {
                controller.toggleEliminated(finalI, finalJ);
              } else if (event.getButton() == MouseButton.PRIMARY) {
                controller.toggleShaded(finalI, finalJ);
              }
            });

        Button btn = new Button();
        btn.setOnAction(actionEvent -> controller.toggleShaded(finalJ, finalI));
        grid.add(rectangle, j, i);
      }
    }
    grid.setHgap(2);
    grid.setVgap(2);
    grid.setGridLinesVisible(true);

    // create Clues -- Rows, then cols
    GridPane vgrid = new GridPane();
    for (int i = 0; i < controller.getClues().getHeight(); i++) {
      HBox hb = new HBox();
      int[] clues = controller.getClues().getRowClues(i);
      for (int j = 0; j < clues.length; j++) {
        if (clues[j] == 0 && getMax(clues) == 0) {
          Text text = new Text(" 0 ");
          hb.getChildren().add(text);
          break;
        } else if (clues[j] != 0) {
          Text text = new Text(" " + clues[j] + " ");
          hb.getChildren().add(text);
        }
      }
      Rectangle clueSpace = new Rectangle(60, 30, Paint.valueOf("gray"));
      StackPane stack = new StackPane();
      stack.getChildren().addAll(clueSpace, hb);
      vgrid.add(stack, 0, i);
    }
    vgrid.setHgap(2);
    vgrid.setVgap(2);
    vgrid.setGridLinesVisible(true);
    // then Cols
    GridPane hgrid = new GridPane();
    for (int j = 0; j < controller.getClues().getWidth(); j++) {
      VBox vb = new VBox();
      int[] clues = controller.getClues().getColClues(j);
      Text text;
      for (int clue : clues) {
        if (clue == 0 && getMax(clues) == 0) {
          text = new Text(" 0 ");
          vb.getChildren().add(text);
          break;
        } else if (clue != 0) {
          text = new Text(" " + clue + " ");
          vb.getChildren().add(text);
        }
      }
      Rectangle clueSpace = new Rectangle(30, 60, Paint.valueOf("gray"));
      StackPane stack = new StackPane();
      stack.getChildren().addAll(clueSpace, vb);
      hgrid.add(stack, j, 0);
    }
    hgrid.setHgap(2);
    hgrid.setVgap(2);
    hgrid.setGridLinesVisible(true);

    GridPane puzzleGrid = new GridPane();
    puzzleGrid.add(hgrid, 1, 0);
    puzzleGrid.add(vgrid, 0, 1);
    puzzleGrid.add(grid, 1, 1);

    return puzzleGrid;
  }
}
