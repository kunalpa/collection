package com.comp301.a09nonograms.view;

import com.comp301.a09nonograms.PuzzleLibrary;
import com.comp301.a09nonograms.controller.Controller;
import com.comp301.a09nonograms.controller.ControllerImpl;
import com.comp301.a09nonograms.model.Clues;
import com.comp301.a09nonograms.model.Model;
import com.comp301.a09nonograms.model.ModelImpl;
import com.comp301.a09nonograms.model.ModelObserver;
import java.util.List;
import javafx.application.Application;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Paint;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.stage.*;
import javafx.scene.*;

public class AppLauncher extends Application {

  PuzzleView puzzleView;
  ButtonView buttonView;
  Scene scene;
  Controller controller;

  @Override
  public void start(Stage stage) {
    // TODO: Launch your GUI here
    stage.setTitle("Nonograms");
    List<Clues> clues = PuzzleLibrary.create();
    ModelImpl model = new ModelImpl(clues);
    this.controller = new ControllerImpl(model);
    this.puzzleView = new PuzzleView(controller);
    this.buttonView = new ButtonView(controller);

    ModelObserver observer =
        (Model m) -> {
          VBox pane = new VBox();
          pane.getChildren().add(buttonView.render());
          pane.getChildren().add(puzzleView.render());
          pane.setSpacing(20);
          if (controller.isSolved()) {
            Text text = new Text("\t\t\tSolved!");
            text.setScaleX(3);
            text.setScaleY(3);
            text.setFill(Paint.valueOf("Green"));
            pane.getChildren().add(text);
          }
          Scene scene = new Scene(pane, 500, 500);
          scene.setFill(Paint.valueOf("green"));
          stage.setScene(scene);
        };
    model.addObserver(observer);

    Text message =
        new Text(
            " The algorithm only checks the correct number of shaded (black)"
                + "\n cells, thus, eliminated (red) or empty (white) cells are not considered\n");
    message.setFont(Font.font("Veranda", FontWeight.BOLD, 10));
    Text header = new Text("Nonograms");
    header.setFont(Font.font("Veranda", FontWeight.BOLD, 36));
    VBox sceneBox = new VBox();
    sceneBox.getChildren().add(header);
    sceneBox.getChildren().add(message);
    sceneBox.getChildren().add(buttonView.render());
    sceneBox.getChildren().add(puzzleView.render());
    scene = new Scene(sceneBox);
    stage.setScene(scene);
    stage.show();
  }
}
