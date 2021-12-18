package com.comp301.a09nonograms.model;

public class Puzzle {

  private final Board gameBoard;
  private final Clues clues;

  public Puzzle(Board gameBoard, Clues clues) {
    this.gameBoard = gameBoard;
    this.clues = clues;
  }

  public Board getGameBoard() {
    return this.gameBoard;
  }

  public Clues getClues() {
    return this.clues;
  }
}
