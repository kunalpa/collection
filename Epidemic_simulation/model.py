"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from typing import List
from random import random
from projects.pj02 import constants
from math import sin, cos, pi, sqrt


__author__ = "730392260"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> float:
        """Returns the distance between two points."""
        x_distance: float = self.x - other.x
        y_distance: float = self.y - other.y
        net_distance: float = sqrt(x_distance**2 + y_distance**2)
        return net_distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location, direction, and sickness quantity."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """This makes the code tick."""
        self.location = self.location.add(self.direction)
        if Cell.is_infected(self):
            self.sickness += 1
        if self.sickness == constants.RECOVERY_PERIOD:
            Cell.immunize(self)

    def color(self) -> str:
        """Return the color representation of a cell."""
        if Cell.is_infected(self):
            color: str = "green"
        if Cell.is_vulnerable(self):
            color = "gray"
        if Cell.is_immune(self):
            color = "light blue"  
        return color

    def contract_disease(self) -> None:
        """Assigns infected constant to sickness."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Returns True if cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        return False
    
    def is_infected(self) -> bool:
        """Returns True if cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        return False
    
    def immunize(self) -> None:
        """Assigns immune constant to sickness."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Returns True if cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        return False

    def contact_with(self, other_cell: Cell) -> None:
        """Contracts disease if a vulnerable cell comes in contact with an infected one."""
        if self.is_infected() and other_cell.is_vulnerable(): 
            other_cell.contract_disease()
        elif self.is_vulnerable() and other_cell.is_infected():
            self.contract_disease()


class Model:
    """The state of the simulation."""
    population: List[Cell]
    time: int = 0
    initial_infected: int = constants.INITIAL_INFECTED
    initial_immune: int = constants.INITIAL_IMMUNE

    def __init__(self, cells: int, speed: float, initial_infected: int, initial_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        self.initial_infected = initial_infected
        self.initial_immune = initial_immune
        if self.initial_infected >= cells or initial_infected <= 0:
            raise ValueError(f"Between 0 and {constants.CELL_COUNT} must be infected for this simulation.")
        if initial_immune >= cells or initial_immune < 0:
            raise ValueError(f"Between 0 and {constants.CELL_COUNT} must be immune for this simulation.")
        for i in range(cells):
            start_loc = self.random_location()
            start_dir = self.random_direction(speed)
            cell = Cell(start_loc, start_dir)
            if i < self.initial_infected:
                cell.contract_disease()
            elif (i < self.initial_infected + self.initial_immune and i >= self.initial_infected):
                cell.immunize()
            elif i >= self.initial_infected + self.initial_immune:
                Cell.sickness = constants.VULNERABLE
            self.population.append(cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle = 2.0 * pi * random()
        dir_x = cos(random_angle) * speed
        dir_y = sin(random_angle) * speed
        return Point(dir_x, dir_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1
    
    def check_contacts(self) -> None:
        """Comparing distances of every cell in the population."""
        for i in range(len(self.population)):
            for j in range(len(self.population)):
                if j != i:
                    point_i: Cell = self.population[i]
                    point_j: Cell = self.population[j]
                    if Point.distance(point_i.location, point_j.location) <= constants.CELL_RADIUS:
                        Cell.contact_with(point_i, point_j)

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True