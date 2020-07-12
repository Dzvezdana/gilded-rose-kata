# Gilded Rose Kata

The Gilded Rose is a refactoring Kata and its purpose is to enhance your refactoring skills.
This Kata is based on: 
* [GildedRose](https://github.com/NotMyself/GildedRose) which contains the original implementation and,
* [Goring-Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata) that contains implementations in multiple programming languages.

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
* The code contains duplicated logic.
* The introduction of the new product `Conjured` will require class modification. This might break the deeply nested if statements logic.

# Approach

Before refactoring the code, we should write unit tests to preserve the existing behaviour of the `update_quality` method.
By writing unit tests we can gain better understanding of the current legacy code and the business rules.

We can check the test coverage by running [measure_test_coverage](measure_test_coverage.sh) in our terminal:

```bash
sh ./measure_test_coverage
```

After writing sufficient number of tests, we can start refactoring.
I refactored the code by creating separate logic for different business rules and splitting the existing code in multiple files.
The refactored code consists of:

* `gilded_rose.py`: Used to update items properties.
* `products.py`: List of products names, separated here to avoid hardcoding in the updater logic.
* `test_guilded_rose.py` and `texttestfixture.py`: Tests.
* `item_updater.py`: Contains the `Item` class and its children classes. The `Item` class is a parent class, which describes and updates regular products.
`AgedBrie`, `BackstagePasses`, `Conjured` and `Sulfuras` inherit from the `Item` class and reimplement the `update_quality` method
based on the specific products' business rules.

The separate product classes lead to the code being more readable and easy to understand.

Any new product that follows the existing business rules can make use of the existing classes. New 
products that require new business rules can easily be introduced by creating a new child class. 
Because of this, adding new products in the future will not require modification of the existing code.
This eliminates the possibility of breaking any code already used by previous products.


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