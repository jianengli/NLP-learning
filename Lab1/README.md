# 1. Sentence generator
Rule-based sentence generator

## Table of Contents
- [Background](#background)
- [Running result 1](#running-result)

## Background
How to generate sentences is a classic problem. From the 1940s, when Turing proposed machine intelligence, he used the ability of humans to communicate with computers smoothly. A prerequisite for talking to a computer is that the computer can generate language.
In the movie "Western World", the method of robotic language generation is the method of using SyntaxTree to generate language. I implemented a rule-based sentence generator via python.

## Running result
<p align="center">
<img src="https://github.com/jianengli/NLP-learning/blob/master/Lab1/Result.png"/>
</p>

# 2. A Dialogue Intelligent System Based on Syntax Tree and Language Model
Model can generate language that is closer to humans

## Table of Contents
- [Background](#background)
- [Running result 2](#running-result)
- [Maintainers](#maintainers)

## Background
Principle: Python text reads the data source and gets the new Language Model. Do text cleaning to get all the plain text and cut the text into words. Finally, the cleaned text is sent to the previously defined language model to determine the reasonableness of the text.
Function: Define the generate_best function, which inputs a grammar and language model, can generate n sentences, and can choose a most reasonable sentence. The result is the highest quality language.

## Running result
<p align="center">
<img src="https://github.com/jianengli/NLP-learning/blob/master/Lab1/Plot%20the%20vocabulary%20frequency%20of%20the%20top%20100%20statistical%20results.png"/>
</p>
<p align="center">
<img src="https://github.com/jianengli/NLP-learning/blob/master/Lab1/Result2.png"/>
</p>

## Maintainers
[@Jianeng](https://github.com/jianengli).
