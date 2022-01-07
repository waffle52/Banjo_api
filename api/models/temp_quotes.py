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
