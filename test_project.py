import project
import pytest
from project import opponents
from unittest.mock import patch


def test_validate_name():
    assert project.validate_name("Arthur") == "Arthur"

def test_invalid_name():
    with pytest.raises(ValueError):
        project.validate_name("")

def test_validate_char():
    assert project.valid_char("fast") == "fast"

def test_invalid_char():
    with pytest.raises(ValueError):
        project.valid_char("")

def test_invalid_char():
    with pytest.raises(ValueError):
        project.valid_char("k")

def test_char_stats():
    assert project.get_char_stats("brave") == (1, 3, 8)

def test_char_stats():
    with pytest.raises(ValueError):
        project.get_char_stats("k")

def test_choose_opponent():
    length = len(opponents)
    chosen_opponent = project.choose_opponent()
    assert len(opponents) == length - 1
    assert isinstance(chosen_opponent, list)

def test_valid_door():
    assert project.valid_door("l") == "left"

def test_invalid_door():
    assert project.valid_door("q") == None

def test_roll_dice():
    number = project.roll_dice()
    assert number in range(1, 7)

def test_roll_dice_with_input():
    number = project.roll_dice(9)
    assert number in range(1, 9)


def mock_ready_to_fight():
    return 3  # Simulate a dice roll of 3

def mock_monster_attack_strength(attack):
    return 5  # Simulate a monster attack strength of 5

@patch('project.ready_to_fight', side_effect=mock_ready_to_fight)
@patch('project.monster_attack_strength', side_effect=mock_monster_attack_strength)
def test_fight(mock_monster_attack, mock_ready_to_fight):
    # Monster defeated
    attack = 2
    defence = 1
    warrior_health = 10
    still_alive = True
    monster = "Goblin"
    monster_health = 1
    monster_attack = 6

    final_health, still_alive = project.fight(attack, defence, warrior_health, still_alive, monster, monster_health, monster_attack)

    assert final_health == warrior_health
    assert still_alive == True


@patch('project.ready_to_fight', side_effect=mock_ready_to_fight)
@patch('project.monster_attack_strength', side_effect=mock_monster_attack_strength)
def test_fight_2(mock_monster_attack, mock_ready_to_fight):
    # Warrior defeated
    attack = 1
    defence = 0
    warrior_health = 1
    still_alive = True
    monster = "Goblin"
    monster_health = 10
    monster_attack = 10

    final_health, still_alive = project.fight(attack, defence, warrior_health, still_alive, monster, monster_health, monster_attack)

    assert final_health < 1
    assert still_alive == False
