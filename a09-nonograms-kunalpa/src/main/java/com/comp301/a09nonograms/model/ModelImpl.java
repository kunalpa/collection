package com.comp301.a09nonograms.model;

import java.util.ArrayList;
import java.util.List;

public class ModelImpl implements Model {

  private final List<Clues> clues;
  Puzzle currentGame;
  List<Puzzle> puzzles = new ArrayList<>();
  List<ModelObserver> observers = new ArrayList<>();

  public ModelImpl(List<Clues> clues) {
    this.clues = clues;
    for (Clues clue : clues) {
      BoardImpl gameBoard = new BoardImpl(clue.getHeight(), clue.getWidth());
      puzzles.add(new Puzzle(gameBoard, clue));
    }
    currentGame = puzzles.get(0);
  }

  @Override
  public boolean isShaded(int row, int col) {
    return currentGame.getGameBoard().isShaded(row, col);
  }

  @Override
  public boolean isEliminated(int row, int col) {
    return currentGame.getGameBoard().isEliminated(row, col);
  }

  @Override
  public boolean isSpace(int row, int col) {
    return currentGame.getGameBoard().isSpace(row, col);
  }

  @Override
  public void toggleCellShaded(int row, int col) {
    currentGame.getGameBoard().toggleCellShaded(row, col);
    notifyObservers();
  }

  @Override
  public void toggleCellEliminated(int row, int col) {
    currentGame.getGameBoard().toggleCellEliminated(row, col);
    notifyObservers();
  }

  @Override
  public void clear() {
    currentGame.getGameBoard().clear();
    notifyObservers();
  }

  @Override
  public int getWidth() {
    return ((BoardImpl) currentGame.getGameBoard()).getWidth();
  }

  @Override
  public int getHeight() {
    return ((BoardImpl) currentGame.getGameBoard()).getHeight();
  }

  @Override
  public int[] getRowClues(int index) {
    return currentGame.getClues().getRowClues(index);
  }

  @Override
  public int[] getColClues(int index) {
    return currentGame.getClues().getColClues(index);
  }

  @Override
  public int getRowCluesLength() {
    return currentGame.getClues().getRowCluesLength();
  }

  @Override
  public int getColCluesLength() {
    return currentGame.getClues().getColCluesLength();
  }

  @Override
  public int getPuzzleCount() {
    return clues.size();
  }

  @Override
  public int getPuzzleIndex() {
    return this.puzzles.indexOf(currentGame);
  }

  @Override
  public void setPuzzleIndex(int index) {
    if (index < getPuzzleCount() && index >= 0) {
      currentGame = puzzles.get(index);
      notifyObservers();
    }
  }

  @Override
  public void addObserver(ModelObserver observer) {
    observers.add(observer);
  }

  @Override
  public void removeObserver(ModelObserver observer) {
    observers.remove(observer);
  }

  private int sumClues(int[] clues) {
    int sum = 0;
    for (int clue : clues) {
      sum += clue;
    }
    return sum;
  }

  @Override
  public boolean isSolved() {
    // check rows
    for (int row = 0; row < getHeight(); row++) {
      int[] rowClue = currentGame.getClues().getRowClues(row);
      int boardRowIndex = 0;
      for (int j = 0; j < getRowCluesLength(); j++) {
        int count = 0;
        boolean counting = false;
        if (rowClue[j] != 0) {
          while (boardRowIndex < getWidth()) {
            if (currentGame.getGameBoard().isShaded(row, boardRowIndex)) {
              count++;
              counting = true;
              boardRowIndex++;
            } else if (!counting) {
              boardRowIndex++;
            } else {
              boardRowIndex++;
              break;
            }
          }
        }
        if (count != rowClue[j]) {
          return false;
        }
      }
    }

    // check columns
    for (int i = 0; i < getWidth(); i++) {
      int[] colClue = currentGame.getClues().getColClues(i);
      int boardColIndex = 0;
      for (int k : colClue) {
        int count = 0;
        boolean counting = false;
        if (k != 0) {
          while (boardColIndex < getHeight()) {
            if (currentGame.getGameBoard().isShaded(boardColIndex, i)) {
              count++;
              counting = true;
              boardColIndex++;
            } else if (!counting) {
              boardColIndex++;
            } else {
              boardColIndex++;
              break;
            }
          }
        }
        if (count != k) {
          return false;
        }
      }
    }
    return true;
  }

  private void notifyObservers() {
    for (ModelObserver observer : observers) {
      observer.update(this);
    }
  }

  public Puzzle getActivePuzzle() {
    return currentGame;
  }
}
