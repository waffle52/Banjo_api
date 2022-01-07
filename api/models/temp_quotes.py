#!/usr/bin/env python3


class quote:
    def __init__(self, person, idx, quote):
        self.person = person
        self.idx = idx
        self.quote = quote

    def read(self):
        return (self.quote)

quotes = []
quotes.append(quote("Space Ghost", 0, "Bears are Crazy. They'll bite your head if you're wearing a steak on it."))
quotes.append(quote("Space Ghost", 1, "Welcome back, stupid viewers! You'll watch anything! Go ahead, change the channel. You'll be back!"))
quotes.append(quote("Space Ghost", 2, "I have a giant brain that is able to reduce any complex machine into a simple yes or no answer."))
quotes.append(quote("Space Ghost", 3, "Chambraigne: It's shampoo for your hair, and your brain."))
