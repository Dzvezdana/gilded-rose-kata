# Gilded Rose Kata

The Gilded Rose is a refactoring Kata and its purpose is to enhance your refactoring skills.
This Kata is based on: 
* [GildedRose](https://github.com/NotMyself/GildedRose) which contains the original implementation and,
* [Goring-Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata) that contain implementation in multiple programming languages.

The goal of this kata is to improve the overall code quality by refactoring the existing code and then including new business rules for a new product called
`Conjured`.

The Gilded Rose Kata contains two classes `Item` and `GildedRose`. Item has `name`, `sell_in` and `quality` attributes. 
`GildedRose` class contains the `update_quality` method responsible for decreasing `sell_in` and updating the `quality` attributes for each product item.

# Constraints

There are some constraints that we have to respect while solving this kata:

* Do not alter the Item class or Items property.
* Certain product increase or decrease their quality with a specific rate. The kata contains business rules for the product quality increase/decrease and rate.
* An item can never have its quality increased above 50.
* The quality of an item is never negative.

You can read the detailed requirements [here](requirements.md).

# Why does this code needs refactoring?

* In its current state the code is inflexible as all the business rules are contained in one class.
* The code has a lot of nested if statements that need to be resolved.
* The code is difficult to read.
* The code contains hardcoded values.
* The introduction of the new product `Conjured` will require class modification. This might break the deeply nested if statements logic.

# Approach

Before refactoring the code, we should write unit tests to preserve the existing behaviour of the `update_quality` method.
By writing unit tests we can gain better understanding of the current legacy code and the business rules.

We can check the test coverage by running [measure_test_coverage](measure_test_coverage.sh) in our terminal:

```bash
./measure_test_coverage
```

After write sufficient number of tests, we can start refactoring.
I refactored the code by creating separate functions for different business rules: 

* `increase_quality_by_day`: Increase quality for products like Brie,
* `decrease_quality_by_day`: Decrease quality for regular products, 
* `update_backstage_passes`: Contains business rules for passes products, 
* `update_conjured`: Contains business rules for conjured products,
* `update_legendary`: Contains business rules for legendary products,

The separate method leads to the code being more readable and easy to understand.

Any new product that follows the existing business rules can make use of the existing methods and new 
products that require new business rules can be easily introduced by creating a new method. 
This leads to the existing code requiring no modification and eliminates the possibility to breaking code used by previous products.


# Dependencies

* Python 3.8

# How to run the tests

Setup virtual environment:

```bash
python3 -m venv rose-venv
source rose-venv/bin/activate
```

To run all tests use:

```python
python -m unittest -v test_gilded_rose.py
```

To run a particular test use:

```python
python  test_gilded_rose.py GildedRoseUpdaterTest.test_normal_with_zero_quality
```