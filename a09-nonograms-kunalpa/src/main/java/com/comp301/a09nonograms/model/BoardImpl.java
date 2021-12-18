package com.comp301.a09nonograms.model;

public class BoardImpl implements Board {

  private final int height;
  private final int width;
  public int[][] gameBoard; // 0 is blank, 1 is shaded, 2 is eliminated

  public BoardImpl(int height, int width) {
    this.height = height;
    this.width = width;
    gameBoard = new int[height][width];
    for (int i = 0; i < height; i++) {
      for (int j = 0; j < width; j++) {
        gameBoard[i][j] = 0;
      }
    }
  }

  @Override
  public boolean isShaded(int row, int col) {
    return gameBoard[row][col] == 1;
  }

  @Override
  public boolean isEliminated(int row, int col) {
    return gameBoard[row][col] == 2;
  }

  @Override
  public boolean isSpace(int row, int col) {
    return gameBoard[row][col] == 0;
  }

  @Override
  public void toggleCellShaded(int row, int col) {
    if (gameBoard[row][col] == 1) {
      gameBoard[row][col] = 0;
    } else {
      gameBoard[row][col] = 1;
    }
  }

  @Override
  public void toggleCellEliminated(int row, int col) {
    if (gameBoard[row][col] == 2) {
      gameBoard[row][col] = 0;
    } else {
      gameBoard[row][col] = 2;
    }
  }

  @Override
  public void clear() {
    for (int i = 0; i < this.height; i++) {
      for (int j = 0; j < this.width; j++) {
        gameBoard[i][j] = 0;
      }
    }
  }

  public int getHeight() {
    return this.height;
  }

  public int getWidth() {
    return this.width;
  }
}
