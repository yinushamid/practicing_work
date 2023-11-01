class Card:
    faces = ['ace', '2', '3', '4', '5', '6,', '7', '8', '9', '10', 'jack', 'queen', 'king']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    def __init__(self, faces, suits):
        self.faces =faces
        self.suits = suits
    def faces(self):
        return self.faces
    def suits(self):
        return self.suits
    def image_name(self):

        return str(self).replace(' ', '_') + '.png'
    def __repr__(self):

        return f"Card(face='{self.face}', suit='{self.suit}')"
    def __format__(self, format):
        return f'{str(self):{format}}'
