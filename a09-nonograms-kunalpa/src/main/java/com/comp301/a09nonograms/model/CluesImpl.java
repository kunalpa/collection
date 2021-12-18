package com.comp301.a09nonograms.model;

public class CluesImpl implements Clues {

  private final int[][] rows;
  private final int[][] columns;

  public CluesImpl(int[][] rowClues, int[][] colClues) {
    if (rowClues == null || colClues == null) {
      throw new IllegalArgumentException();
    }
    this.rows = rowClues;
    this.columns = colClues;
  }

  @Override
  public int getWidth() {
    return this.columns.length;
  }

  @Override
  public int getHeight() {
    return this.rows.length;
  }

  @Override
  public int[] getRowClues(int index) {
    return this.rows[index];
  }

  @Override
  public int[] getColClues(int index) {
    return this.columns[index];
  }

  @Override
  public int getRowCluesLength() {
    return this.rows[0].length;
  }

  @Override
  public int getColCluesLength() {
    return this.columns[0].length;
  }
}
