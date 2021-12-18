package com.comp301.a09nonograms.view;

import com.comp301.a09nonograms.controller.Controller;
import javafx.event.ActionEvent;
import javafx.geometry.Insets;
import javafx.scene.Parent;
import javafx.scene.control.Button;
import javafx.scene.layout.HBox;
import javafx.scene.text.Text;

public class ButtonView implements FXComponent {

  Controller controller;

  public ButtonView(Controller controller) {
    this.controller = controller;
  }

  @Override
  public Parent render() {
    HBox controls = new HBox();
    Button next = new Button("next");
    Button previous = new Button("previous");
    Button random = new Button("random");
    Button clear = new Button("clear");

    next.setOnAction(
        (ActionEvent event) -> {
          controller.nextPuzzle();
        });
    previous.setOnAction(
        (ActionEvent event) -> {
          controller.prevPuzzle();
        });
    random.setOnAction(
        (ActionEvent event) -> {
          controller.randPuzzle();
        });
    clear.setOnAction(
        (ActionEvent event) -> {
          controller.clearBoard();
        });

    // display current puzzle/total puzzles
    HBox message = new HBox();
    message.setPadding(new Insets(0, 0, 0, 70));
    int index = controller.getPuzzleIndex();
    Text indexDisplay = new Text("Puzzle: " + (index + 1) + "/" + controller.getPuzzleCount());
    message.getChildren().add(indexDisplay);

    controls.getChildren().add(next);
    controls.getChildren().add(previous);
    controls.getChildren().add(random);
    controls.getChildren().add(clear);
    controls.getChildren().add(message);
    return controls;
  }
}
