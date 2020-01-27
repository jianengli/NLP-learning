# 1. Human language generator based on Syntax Tree
A Rule-based program generates language that is closer to humans. 

## Table of Contents
- [Background](#background)
- [Running result](#running-result1)

## Background
How to generate sentences is a classic problem. From the 1940s, when Turing proposed machine intelligence, he used the ability of humans to communicate with computers smoothly. A prerequisite for talking to a computer is that the computer can generate language.
In the movie "Western World", the method of robotic language generation is the method of using SyntaxTree to generate language. I implemented a rule-based sentence generator via python.

## Running result1
<p align="center">
<img src="https://github.com/jianengli/NLP-learning/blob/master/Lab1/Result.png"/>
</p>

# 2. Human language generator based on Syntax Tree and Language Model
A probability-based program reads the data source and build up a language model, and generates language that is closer to humans. 

## Table of Contents
- [Background](#background)
- [Running result](#running-result2)
- [Maintainers](#maintainers)

## Background
Building the language model: First, clean the text to get all the plain text and cut the text into words. Then, according to the 2-gram principle, the cleaned up text is trained into a language model.

Generate language: Use the semantic tree-based language generator to generate multiple sentences, and then use the language model to calculate the probability of each sentence occurring. The highest is the language closest to humans.

Function: Define the generate_best function, which inputs a grammar and language model, can generate n lines of sentences, and can pick one of the most reasonable sentence. The result is a sentence most likely to be spoken by humans.

## Running result2
Frequency chart of the top 100 words that appear most frequently in the provided dataset：
<p align="center">
<img src="https://github.com/jianengli/NLP-learning/blob/master/Lab1/Plot%20the%20vocabulary%20frequency%20of%20the%20top%20100%20statistical%20results.png"/>
</p>
<p align="center">
<img src="https://github.com/jianengli/NLP-learning/blob/master/Lab1/Result2.png"/>
</p>

## Maintainers
[@Jianeng](https://github.com/jianengli).
