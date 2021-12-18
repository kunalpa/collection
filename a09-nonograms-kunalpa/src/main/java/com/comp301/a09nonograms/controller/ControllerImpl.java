package com.comp301.a09nonograms.controller;

import com.comp301.a09nonograms.model.Clues;
import com.comp301.a09nonograms.model.ModelImpl;

public class ControllerImpl implements Controller {

  private final ModelImpl model;

  public ControllerImpl(ModelImpl model) {
    this.model = model;
  }

  @Override
  public Clues getClues() {
    return model.getActivePuzzle().getClues();
  }

  @Override
  public boolean isSolved() {
    return model.isSolved();
  }

  @Override
  public boolean isShaded(int row, int col) {
    return model.isShaded(row, col);
  }

  @Override
  public boolean isEliminated(int row, int col) {
    return model.isEliminated(row, col);
  }

  @Override
  public void toggleShaded(int row, int col) {
    model.toggleCellShaded(row, col);
  }

  @Override
  public void toggleEliminated(int row, int col) {
    model.toggleCellEliminated(row, col);
  }

  @Override
  public void nextPuzzle() {
    model.setPuzzleIndex(model.getPuzzleIndex() + 1);
  }

  @Override
  public void prevPuzzle() {
    model.setPuzzleIndex(model.getPuzzleIndex() - 1);
  }

  @Override
  public void randPuzzle() {
    while (true) {
      int index = ((int) (Math.random() * 100) % getPuzzleCount());
      if (index != getPuzzleIndex()) {
        model.setPuzzleIndex(index);
        return;
      }
    }
  }

  @Override
  public void clearBoard() {
    model.clear();
  }

  @Override
  public int getPuzzleIndex() {
    return model.getPuzzleIndex();
  }

  @Override
  public int getPuzzleCount() {
    return model.getPuzzleCount();
  }
}
